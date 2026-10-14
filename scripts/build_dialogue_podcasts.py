import asyncio
import os
import sys
import json
import re
import time
import subprocess
import edge_tts

sys.stdout.reconfigure(encoding='utf-8')

VI_AUDIO_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'sentences_vi')
EN_AUDIO_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'sentences')
PODCAST_DIR = os.path.join(os.getcwd(), 'public', 'audio', 'communication', 'podcasts')
TEMP_DIR = os.path.join(os.getcwd(), 'scratch', 'podcast_builder_temp')

os.makedirs(VI_AUDIO_DIR, exist_ok=True)
os.makedirs(PODCAST_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

with open('scratch/dialogue_lectures_data.json', 'r', encoding='utf-8') as f:
    dialogues_data = json.load(f)

FEMALE_SPEAKERS = {'Mrs. Smith', 'Mrs. Lan', 'Girl'}

# Clean minor typos or English interjections in Vietnamese translation so TTS & UI are natural
VI_CLEAN_OVERRIDES = {
    'dial_m4_l1_01_tony_hey_jimmy_where_are_you': 'Này Jimmy, anh đang ở đâu thế?',
    'dial_m4_l1_07_tony_ok_i_see_i_gotta_find': 'Được rồi, tôi hiểu. Vậy thì tôi phải tìm người khác rồi. Tạm biệt Jimmy.',
    'dial_m4_l1_08_jimmy_i_gotta_continue_my_shopping_bye': 'Tôi cũng phải mua sắm tiếp đây. Tạm biệt Tony.',
    'dial_m4_l2_02_jason_oh_im_here_to_take_a': 'Ồ, tôi ở đây để làm bài thi. Tôi rất mệt mỏi và hồi hộp vì mình đã trượt bài thi này trước đây và bên cạnh đó, tôi không quen chịu nhiều áp lực như vậy. Dù sao thì tôi cũng mong ngóng được tốt nghiệp đại học sau lần này.',
    'dial_m4_l3_06_shaj_ah_dont_worry_about_it_it': 'À, đừng lo về điều đó. Dù sao nó cũng quá hạn rồi…',
    'dial_m8l1_02_girl_yeah_im_alright_thank_you_im': 'Vâng, tôi ổn. Cảm ơn anh. Dạo này tôi đang gặp khó khăn trong việc hiểu người bạn trai của mình. Thật khó cho tôi có thể giữ được mối quan hệ với anh ta. Tôi không biết phải làm gì bây giờ…',
    'dial_m8l1_04_girl_ive_heard_that_hes_been_going': 'Tôi nghe nói rằng anh ta đang hò hẹn với một cô gái khác. Anh ấy đáng ra không được làm thế với tôi. Dù sao thì tôi đáng ra phải kết thúc mối quan hệ với anh ta từ lâu rồi…',
    'dial_m8l1_06_girl_hang_on_are_you_trying_to': 'Khoan đã. Anh đang cố tán tỉnh tôi đấy à? Để tôi cảnh báo anh rằng tôi có thể làm anh tổn thương vì tôi không chắc là mình đã sẵn sàng cho một mối quan hệ mới.',
    'dial_m8l1_08_girl_ok_cute_boy_its_my_turn': 'Được rồi anh chàng dễ thương, đến lượt tôi hỏi anh một câu và anh tốt hơn hết hãy trả lời một cách trung thực.',
    'dial_m8l3_04_jason_thank_you_i_appreciate_it_im': 'Cảm ơn, tôi cảm kích vì điều đó. Tôi đang gặp khó khăn trong việc chăm sóc mẹ nhưng điều đó cũng đồng nghĩa sẽ khó cho tôi có thể tập trung vào bài tập.',
    'dial_m12l1_05_mrsmith_right_away_madam_and_by_the': 'Ngay đây thưa bà… và mà này, khi bà gọi Jimmy, hãy nói rằng không có gì đặc biệt về buổi tối ngày mai. Bố nó chỉ muốn chúng ta đi thử cái nhà hàng mới trên phố. Kiểu như lâu lâu lại sum họp gia đình một lần.',
    'dial_m12l1_06_mrssmith_ok_seem_a_good_white_lie': 'Được đấy. Nghe giống một lời nói dối vô hại. Đây chắc chắn sẽ là một bất ngờ lớn với nó.',
}

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

sem = asyncio.Semaphore(4)

async def generate_vi_tts(audio_key, text, speaker):
    out_file = os.path.join(VI_AUDIO_DIR, f"{audio_key}.mp3")
    if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
        return 'already_exists'

    voice = "vi-VN-HoaiMyNeural" if speaker in FEMALE_SPEAKERS else "vi-VN-NamMinhNeural"
    fallback_voice = "vi-VN-NamMinhNeural" if voice == "vi-VN-HoaiMyNeural" else "vi-VN-HoaiMyNeural"

    async with sem:
        for attempt in range(4):
            use_voice = voice if attempt < 2 else fallback_voice
            try:
                comm = edge_tts.Communicate(text, use_voice)
                await asyncio.wait_for(comm.save(out_file), timeout=12.0)
                if os.path.exists(out_file) and os.path.getsize(out_file) > 500:
                    return 'generated'
            except Exception as e:
                await asyncio.sleep(0.5 + attempt * 0.5)
    return 'failed'

async def generate_all_dialogue_vi_audios():
    print("=== Step 1: Generating Vietnamese TTS Audio for all 87 Dialogue Turns ===")
    tasks = []
    meta_list = []
    for d in dialogues_data:
        for t in d['turns']:
            ak = t['audio_key']
            if ak in VI_CLEAN_OVERRIDES:
                t['translation_vi'] = VI_CLEAN_OVERRIDES[ak]
            vi_text = t['translation_vi']
            speaker = t['speaker']
            tasks.append(generate_vi_tts(ak, vi_text, speaker))
            meta_list.append((ak, speaker, vi_text))

    results = await asyncio.gather(*tasks)
    gen_cnt = sum(1 for r in results if r == 'generated')
    ex_cnt = sum(1 for r in results if r == 'already_exists')
    fail_cnt = sum(1 for r in results if r == 'failed')
    print(f"VI Audio Summary: {gen_cnt} generated, {ex_cnt} existed, {fail_cnt} failed (Total: {len(results)})")
    if fail_cnt > 0:
        for (ak, sp, vt), r in zip(meta_list, results):
            if r == 'failed':
                print(f"  FAILED: {ak} ({sp}): {vt}")
        sys.exit(1)

def build_podcasts_for_dialogue(d):
    slug = d['slug']
    clean_title = d['clean_title']
    mod_title = d['module_title']
    turns = d['turns']

    print(f"\n-------------------------------------------------------")
    print(f"Building Shadowing & Reflex Podcasts for [{slug}] {d['lecture_title']} ({len(turns)} turns)...")

    # ==========================================================
    # 1. SHADOWING PODCAST (podcast_shadowing_{slug}.mp3 + .json)
    # ==========================================================
    sh_sentences = []
    sh_concat = []
    sh_time = 0.0

    for t in turns:
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

    sh_patterns = [{
        'pattern_num': d['lecture_order'],
        'pattern_title': clean_title,
        'pattern_translation': mod_title,
        'start_time': 0.0,
        'sentences': sh_sentences
    }]

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
    rf_sentences = []
    rf_concat = []
    rf_time = 0.0

    for t in turns:
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

    rf_patterns = [{
        'pattern_num': d['lecture_order'],
        'pattern_title': clean_title,
        'pattern_translation': mod_title,
        'sentences': rf_sentences
    }]

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
    await generate_all_dialogue_vi_audios()
    # Save updated dialogue_lectures_data.json with cleaned translations
    with open('scratch/dialogue_lectures_data.json', 'w', encoding='utf-8') as f:
        json.dump(dialogues_data, f, ensure_ascii=False, indent=2)

    for d in dialogues_data:
        build_podcasts_for_dialogue(d)

    print("\n🎉 ALL 20 DIALOGUE PODCAST MP3s & TIMELINE JSONs BUILT SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(main())
