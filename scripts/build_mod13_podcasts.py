import asyncio
import os
import sys
import json
import subprocess
import edge_tts

sys.stdout.reconfigure(encoding='utf-8')

VI_AUDIO_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'sentences_vi')
EN_AUDIO_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'sentences')
PODCAST_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'podcasts')
TEMP_DIR = os.path.join(os.getcwd(), 'scratch', 'podcast_builder_temp')

os.makedirs(VI_AUDIO_DIR, exist_ok=True)
os.makedirs(EN_AUDIO_DIR, exist_ok=True)
os.makedirs(PODCAST_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

with open('scratch/mod13_lectures_data.json', 'r', encoding='utf-8') as f:
    mod13_data = json.load(f)

FEMALE_NAMES = {'Jane', 'Mary', 'Jill', 'Nancy', 'Martha', 'Joanne'}
MALE_NAMES = {'Jack', 'Steve', 'John', 'Paul', 'Bob', 'Mark', 'Seth', 'Josh', 'Andy', 'Jackson'}


def get_vi_voice(speaker, role):
    if speaker in FEMALE_NAMES:
        return "vi-VN-HoaiMyNeural"
    if speaker in MALE_NAMES:
        return "vi-VN-NamMinhNeural"
    # For generic roles (A/B, You/Stranger, One/Two, You/Agent), use NamMinh for A and HoaiMy for B so turns contrast clearly
    return "vi-VN-HoaiMyNeural" if role == 'B' else "vi-VN-NamMinhNeural"


def get_duration(path):
    cmd = [
        'ffprobe', '-v', 'quiet', '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    val = res.stdout.strip()
    return float(val) if val else 0.0


silence_cache = {}
def get_silence_file(dur):
    dur = round(dur, 2)
    if dur not in silence_cache:
        s_path = os.path.join(TEMP_DIR, f"silence_{dur:.2f}s.mp3")
        if not os.path.exists(s_path):
            cmd = [
                'ffmpeg', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=24000:cl=mono',
                '-t', str(dur), '-c:a', 'libmp3lame', '-b:a', '64k', s_path
            ]
            subprocess.run(cmd, capture_output=True)
        silence_cache[dur] = s_path
    return silence_cache[dur]


sem = asyncio.Semaphore(5)


async def generate_tts_file(out_file, text, primary_voice, fallback_voice):
    if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
        return 'already_exists'

    async with sem:
        for attempt in range(4):
            use_voice = primary_voice if attempt < 2 else fallback_voice
            try:
                comm = edge_tts.Communicate(text, use_voice)
                await asyncio.wait_for(comm.save(out_file), timeout=15.0)
                if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
                    return 'generated'
            except Exception:
                await asyncio.sleep(0.6 + attempt * 0.5)
    return 'failed'


async def generate_all_missing_audios():
    print("=== Step 1: Checking & Generating Missing EN Audios (3 files) ===")
    en_tasks = []
    for lec in mod13_data:
        for d in lec['dialogues']:
            for t in d['turns']:
                ak = t['audio_key']
                en_path = os.path.join(EN_AUDIO_DIR, f"{ak}.mp3")
                if not os.path.exists(en_path) or os.path.getsize(en_path) <= 500:
                    voice = "en-GB-ThomasNeural" if t['role'] == 'B' else "en-GB-RyanNeural"
                    en_tasks.append((ak, generate_tts_file(en_path, t['sentence'], voice, "en-GB-SoniaNeural")))

    if en_tasks:
        en_res = await asyncio.gather(*(task for _, task in en_tasks))
        for (ak, _), r in zip(en_tasks, en_res):
            print(f"  EN [{ak}]: {r}")
            if r == 'failed':
                sys.exit(1)
    else:
        print("  All 354 EN audio files already exist!")

    print("\n=== Step 2: Generating Vietnamese TTS Audio for all 354 Dialogue Turns ===")
    vi_tasks = []
    vi_meta = []
    for lec in mod13_data:
        for d in lec['dialogues']:
            for t in d['turns']:
                ak = t['audio_key']
                vi_path = os.path.join(VI_AUDIO_DIR, f"{ak}.mp3")
                p_voice = get_vi_voice(t['speaker'], t['role'])
                fb_voice = "vi-VN-NamMinhNeural" if p_voice == "vi-VN-HoaiMyNeural" else "vi-VN-HoaiMyNeural"
                vi_tasks.append(generate_tts_file(vi_path, t['translation_vi'], p_voice, fb_voice))
                vi_meta.append((ak, t['speaker'], t['translation_vi']))

    results = await asyncio.gather(*vi_tasks)
    gen_cnt = sum(1 for r in results if r == 'generated')
    ex_cnt = sum(1 for r in results if r == 'already_exists')
    fail_cnt = sum(1 for r in results if r == 'failed')
    print(f"VI Audio Summary: {gen_cnt} generated, {ex_cnt} existed, {fail_cnt} failed (Total: {len(results)})")
    if fail_cnt > 0:
        for (ak, sp, vt), r in zip(vi_meta, results):
            if r == 'failed':
                print(f"  FAILED VI: {ak} ({sp}): {vt}")
        sys.exit(1)


def build_podcasts_for_lecture(lec):
    slug = lec['slug']
    clean_title = lec['clean_title']
    mod_title = lec['module_title']
    dialogues = lec['dialogues']

    print(f"\n-------------------------------------------------------")
    print(f"Building Shadowing & Reflex Podcasts for [{slug}] {lec['lecture_title']} ({len(dialogues)} dialogues, {lec['turns_count']} turns)...")

    # ==========================================================
    # 1. SHADOWING PODCAST (podcast_shadowing_{slug}.mp3 + .json)
    # ==========================================================
    sh_patterns = []
    sh_concat = []
    sh_time = 0.0

    for d_idx, d in enumerate(dialogues):
        d_start_time = round(sh_time, 2)
        sh_sentences = []
        for t in d['turns']:
            ak = t['audio_key']
            en_file = os.path.join(EN_AUDIO_DIR, f"{ak}.mp3")
            if not os.path.exists(en_file):
                raise FileNotFoundError(f"Missing EN file: {en_file}")

            dur_en = round(get_duration(en_file), 2)
            pause_sh = round(dur_en + 1.5, 2)

            start_t = round(sh_time, 2)
            sh_time = round(sh_time + dur_en + pause_sh, 2)

            sh_concat.append(en_file)
            sh_concat.append(get_silence_file(pause_sh))

            sh_sentences.append({
                'turn_num': t['turn_num'],
                'dialogue_num': d['dialogue_num'],
                'speaker': t['speaker'],
                'role': t['role'],
                'sentence': t['sentence'],
                'audio_key': ak,
                'translation': t['translation_vi'],
                'start_time': start_t,
                'duration': dur_en,
                'pause_duration': pause_sh,
                'end_time': sh_time
            })

        # Add a 1.0s transition silence between dialogues
        if d_idx < len(dialogues) - 1:
            sh_concat.append(get_silence_file(1.0))
            sh_time = round(sh_time + 1.0, 2)

        sh_patterns.append({
            'pattern_num': d['dialogue_num'],
            'pattern_title': d['title_vi'],
            'pattern_translation': d['title_en'],
            'start_time': d_start_time,
            'sentences': sh_sentences
        })

    sh_list_path = os.path.join(TEMP_DIR, f"concat_sh_{slug}.txt")
    with open(sh_list_path, 'w', encoding='utf-8') as f:
        for fp in sh_concat:
            f.write(f"file '{fp.replace(os.sep, '/')}'\n")

    sh_mp3_path = os.path.join(PODCAST_DIR, f"podcast_shadowing_{slug}.mp3")
    cmd_sh = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', sh_list_path,
        '-c:a', 'libmp3lame', '-b:a', '64k', '-ar', '24000', '-ac', '1',
        sh_mp3_path
    ]
    subprocess.run(cmd_sh, check=True, capture_output=True)
    sh_actual_dur = round(get_duration(sh_mp3_path), 2)

    sh_json_path = os.path.join(PODCAST_DIR, f"podcast_shadowing_{slug}.json")
    sh_data = {
        'module': mod_title,
        'slug': slug,
        'title': f"Podcast Luyện Nghe & Đọc Nhại Hội Thoại: {clean_title}",
        'audio_url': f"/audio/communication/podcasts/podcast_shadowing_{slug}.mp3",
        'total_duration': sh_actual_dur,
        'patterns': sh_patterns
    }
    with open(sh_json_path, 'w', encoding='utf-8') as f:
        json.dump(sh_data, f, ensure_ascii=False, indent=2)

    # ==========================================================
    # 2. REFLEX PODCAST (podcast_reflex_vi_en_{slug}.mp3 + .json)
    # ==========================================================
    rf_patterns = []
    rf_concat = []
    rf_time = 0.0

    for d_idx, d in enumerate(dialogues):
        d_start_time = round(rf_time, 2)
        rf_sentences = []
        for t in d['turns']:
            ak = t['audio_key']
            vi_file = os.path.join(VI_AUDIO_DIR, f"{ak}.mp3")
            en_file = os.path.join(EN_AUDIO_DIR, f"{ak}.mp3")

            dur_vi = round(get_duration(vi_file), 2)
            dur_en = round(get_duration(en_file), 2)

            pause_reflex = round(max(dur_en + 2.0, 3.5), 2)
            pause_absorb = 2.0

            vi_start = round(rf_time, 2)
            vi_end = round(vi_start + dur_vi, 2)
            p1_start = vi_end
            p1_end = round(p1_start + pause_reflex, 2)
            en_start = p1_end
            en_end = round(en_start + dur_en, 2)
            p2_start = en_end
            p2_end = round(p2_start + pause_absorb, 2)

            rf_concat.append(vi_file)
            rf_concat.append(get_silence_file(pause_reflex))
            rf_concat.append(en_file)
            rf_concat.append(get_silence_file(pause_absorb))

            rf_sentences.append({
                'turn_num': t['turn_num'],
                'dialogue_num': d['dialogue_num'],
                'speaker': t['speaker'],
                'role': t['role'],
                'audio_key': ak,
                'sentence': t['sentence'],
                'translation_vi': t['translation_vi'],
                'start_time': vi_start,
                'vi_start': vi_start,
                'vi_dur': dur_vi,
                'pause_reflex_start': p1_start,
                'pause_reflex_dur': pause_reflex,
                'en_start': en_start,
                'en_dur': dur_en,
                'pause_absorb_start': p2_start,
                'pause_absorb_dur': pause_absorb,
                'end_time': p2_end
            })
            rf_time = p2_end

        if d_idx < len(dialogues) - 1:
            rf_concat.append(get_silence_file(1.0))
            rf_time = round(rf_time + 1.0, 2)

        rf_patterns.append({
            'pattern_num': d['dialogue_num'],
            'pattern_title': d['title_vi'],
            'pattern_translation': d['title_en'],
            'start_time': d_start_time,
            'sentences': rf_sentences
        })

    rf_list_path = os.path.join(TEMP_DIR, f"concat_rf_{slug}.txt")
    with open(rf_list_path, 'w', encoding='utf-8') as f:
        for fp in rf_concat:
            f.write(f"file '{fp.replace(os.sep, '/')}'\n")

    rf_mp3_path = os.path.join(PODCAST_DIR, f"podcast_reflex_vi_en_{slug}.mp3")
    cmd_rf = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', rf_list_path,
        '-c:a', 'libmp3lame', '-b:a', '64k', '-ar', '24000', '-ac', '1',
        rf_mp3_path
    ]
    subprocess.run(cmd_rf, check=True, capture_output=True)
    rf_actual_dur = round(get_duration(rf_mp3_path), 2)

    rf_json_path = os.path.join(PODCAST_DIR, f"podcast_reflex_vi_en_{slug}.json")
    rf_data = {
        'slug': slug,
        'title': f"Podcast Phản Xạ Dịch Việt - Anh: {clean_title}",
        'mode': 'bilingual_reflex',
        'total_duration': rf_actual_dur,
        'patterns': rf_patterns
    }
    with open(rf_json_path, 'w', encoding='utf-8') as f:
        json.dump(rf_data, f, ensure_ascii=False, indent=2)

    sh_kb = os.path.getsize(sh_mp3_path) / 1024
    rf_kb = os.path.getsize(rf_mp3_path) / 1024
    print(f"  -> Shadowing: {sh_actual_dur:.1f}s ({sh_kb:.0f} KB) | Reflex: {rf_actual_dur:.1f}s ({rf_kb:.0f} KB)")


async def main():
    await generate_all_missing_audios()
    for lec in mod13_data:
        build_podcasts_for_lecture(lec)
    print("\n🎉 ALL 24 MODULE 13 PODCAST MP3s & TIMELINE JSONs BUILT SUCCESSFULLY!")


if __name__ == '__main__':
    asyncio.run(main())
