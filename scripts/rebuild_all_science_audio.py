# -*- coding: utf-8 -*-
"""
Universal Granular Box-Level Bilingual Audio Lecture Builder
for all 4 Cambridge IGCSE Science Courses (76 Topic Lectures):
  - IGCSE Biology (0610): Topics 1..21 -> /audio/lectures/biology/{1..21}/manifest.json
  - IGCSE Chemistry (0620): Topics 1..12 -> /audio/lectures/chemistry/{1..12}/manifest.json
  - IGCSE Physics (0625): Topics 1..6 -> /audio/lectures/physics/{1..6}/manifest.json
  - IGCSE Co-ordinated Sciences (0654): B1..B19, C1..C12, P1..P6 -> /audio/lectures/science/{code}/manifest.json
"""

import os
import sys
import re
import json
import math
import shutil
import hashlib
import asyncio
import argparse
import subprocess
import urllib.parse
import aiohttp
from bs4 import BeautifulSoup, Tag, NavigableString
import edge_tts
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BACKUP_DIR = r'C:\Users\Tony\.gemini\antigravity\brain\9af7d1d2-3038-4306-a751-ab5814450513\scratch\science_html_backup'
CACHE_DIR = r'C:\Users\Tony\.gemini\antigravity\brain\9af7d1d2-3038-4306-a751-ab5814450513\scratch\science_tts_hash_cache'
TEMP_DIR = r'C:\Users\Tony\.gemini\antigravity\brain\9af7d1d2-3038-4306-a751-ab5814450513\scratch\science_tts_tmp'

with open(os.path.join(REPO_ROOT, '.env'), 'r', encoding='utf-8') as _f:
    _env = _f.read()

SUPABASE_URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', _env, re.M).group(1).strip()
SUPABASE_KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', _env, re.M).group(1).strip()
sb = create_client(SUPABASE_URL, SUPABASE_KEY)

EN_VOICE = 'en-GB-RyanNeural'
VI_VOICE = 'vi-VN-HoaiMyNeural'

LECTURE_SPECS = [
    # 0610 Biology (1..21)
    ('biology', '1', '11cfe97d-205e-418b-ae79-e39d7e57e0a8', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '2', '2d2545c0-ccb9-4d04-a6fa-f2eec55cdecc', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '3', '0f5013fb-eaf1-4f79-8f41-c6102d2185a2', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '4', '821ff271-c9ae-493a-b14c-e3f4b074a9d9', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '5', 'a5d1775c-6ecb-4d6c-bc50-8aafbf641c1e', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '6', 'e7d6e813-b7b9-4038-9911-8b886978cd07', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '7', '85f36013-879b-49a8-a531-69c245a9630e', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '8', '37f08657-58e8-4fad-8035-2d935e1259e8', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '9', 'b50dd00a-e2b4-4dba-8b1d-3f679dadae74', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '10', '62278d87-97ea-4fa5-aa46-748bca28db68', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '11', 'da59c2b3-124f-4e25-8537-74059e74f9b0', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '12', 'fb098b77-64fa-463a-9829-64f5c9055de5', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '13', 'b8f0539e-9361-4ba4-a96e-74c106494ebe', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '14', 'c9abc870-7cbd-4c7e-b6c9-2d6237ff7670', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '15', 'f87b29a1-56a3-4668-a249-ed9f118d31d8', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '16', '936affb8-f062-4e39-b415-cc3794fb341e', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '17', '77f1f7b8-f30e-4b0b-89e2-2e2482242791', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '18', '89750884-8439-4cda-916a-56bf5524741b', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '19', '7b2384dd-b79d-47fe-b36b-7abf36784f06', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '20', '7777b4df-68dd-4600-b4ba-a4ce56ecc6ac', 'Cambridge IGCSE Biology (0610)'),
    ('biology', '21', '55023dc0-7fdc-46ea-a3e9-9a049306d086', 'Cambridge IGCSE Biology (0610)'),

    # 0620 Chemistry (1..12)
    ('chemistry', '1', 'b1dca40f-5860-5c18-ad99-6c90ef8c2e50', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '2', '98be89ab-7b9c-5ab0-a4f0-895e6d217990', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '3', '9990ebf7-e6f6-540a-ab78-ae48eeea42ba', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '4', 'eb56f423-98b4-5f5c-a891-1691b4691433', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '5', '4c428cf3-2e0c-5b53-a468-0fadb2bb2b7c', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '6', '5b034453-aeea-5dc5-a643-26da8fada0bc', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '7', '0437e039-b3c2-5779-a402-45907c082ac2', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '8', '137cfd77-d86a-5927-a025-e406191e51fc', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '9', '605ec1ff-ecf8-5cf5-aa6e-84dacd8f091f', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '10', 'a0959822-b499-501b-ad83-4ba423b031ff', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '11', '3c425483-4d1a-5405-a1da-354e3598fe30', 'Cambridge IGCSE Chemistry (0620)'),
    ('chemistry', '12', '2d0a3d84-392a-522a-a3ca-7facf0b97f66', 'Cambridge IGCSE Chemistry (0620)'),

    # 0625 Physics (1..6)
    ('physics', '1', '63711578-24ee-530b-af00-95ffbab36daf', 'Cambridge IGCSE Physics (0625)'),
    ('physics', '2', '8074ead2-53cc-5ebd-ab32-c691b3e8aebf', 'Cambridge IGCSE Physics (0625)'),
    ('physics', '3', '6df06f2c-3b0a-556f-a218-3e4d7a9417e0', 'Cambridge IGCSE Physics (0625)'),
    ('physics', '4', '75e29227-213b-5046-abfa-d0cddc677c7a', 'Cambridge IGCSE Physics (0625)'),
    ('physics', '5', '588803a0-fcc4-5582-a53d-1c1925e0e4cf', 'Cambridge IGCSE Physics (0625)'),
    ('physics', '6', '886cd267-2b7b-59a6-a9f2-3fdb24bf2d35', 'Cambridge IGCSE Physics (0625)'),

    # 0654 Co-ordinated Sciences (b1..b19, c1..c12, p1..p6)
    ('science', 'b1', '1231b474-8a99-4330-b45d-fdda19a802fe', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b2', '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b3', '9a23109e-ad73-4fcf-a599-9605cc4906eb', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b4', '757409b3-5cec-4e1f-8877-18d81e440103', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b5', '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b6', '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b7', 'cbebf582-244c-48bf-a586-c6c1922d8e20', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b8', 'e2819423-13ed-47a2-bd80-9a083989e8bd', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b9', 'a79dd569-671f-4559-84a3-eee1e6018172', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b10', '04d34896-13fb-411b-9e13-2bc3f9725136', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b11', '39003a2f-708e-47fe-b8ad-7aae073273a3', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b12', '58e65add-a67a-4b90-8b84-52de1a2840be', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b13', '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b14', '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b15', 'deb8222d-2b75-42a3-b454-9601fbfa1bd2', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b16', 'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b17', '24f0deeb-3cd9-4b82-b253-5a070ca31275', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b18', 'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'b19', '298327a8-455a-44d5-9a4c-164e2653c456', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c1', '3fc0ef74-3661-4f23-a8a8-9c33d11051f5', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c2', 'ee4f94c2-382b-4dbb-aaf8-981e7b0d7223', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c3', 'f0988036-6fd0-4768-993d-a5ea5fe4eb0b', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c4', '4732621b-f827-4b12-934b-3b53e694cc2a', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c5', '71545c83-4d45-4201-978c-aa58d01b57e5', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c6', '7f2b44b2-ba70-4cfc-85b3-3a0709058b46', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c7', '2c83104c-9413-4ee1-bdf3-2c0da8fd96a6', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c8', '856f20da-80e8-4c6a-9cd1-dbe8a1f40828', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c9', 'd34bbfa2-7449-4192-b471-3a6a8ba49257', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c10', '9d61f516-a24c-4485-8490-8485604130ec', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c11', '69b82c81-05a0-40a8-816f-c21a882cef54', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'c12', 'd51b5192-ff57-48a0-bcd9-d4f8a7d10757', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'p1', '690ff013-5d01-4c1e-8546-25b3cd056e64', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'p2', 'dc33ed9d-e328-4f60-8c47-f0dbd103e8c1', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'p3', 'eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'p4', '2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'p5', 'a6077865-db01-4785-9ec7-e8b0f531fcdc', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
    ('science', 'p6', 'd11f8920-fe86-4cd4-ad9a-e8b669bc687b', 'Cambridge IGCSE Co-ordinated Sciences (0654)'),
]

VI_DIACRITIC_RE = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđÀÁẢÃẠĂẰẮẲẴẶÂẦẤẨẪẬÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴĐ]')
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\uFE0F\u200D"
    "]+",
    flags=re.UNICODE
)

SUBSCRIPT_MAP = str.maketrans('₀₁₂₃₄₅₆₇₈₉₊₋', '0123456789+-')
SUPERSCRIPT_DIGITS = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-', '⁺': '+'}


# ============================================================================
# 1. DOM INSPECTION & CLEANING HELPERS
# ============================================================================

def is_hidden(tag: Tag) -> bool:
    if not isinstance(tag, Tag):
        return False
    st = re.sub(r'\s+', '', (tag.get('style') or '').lower())
    return 'display:none' in st


def has_hidden_ancestor(tag: Tag) -> bool:
    cur = tag
    while isinstance(cur, Tag):
        if is_hidden(cur):
            return True
        cur = cur.parent
    return False


def clean_old_audio_artifacts(soup: BeautifulSoup):
    """Idempotently remove legacy audio badges, classes, data-lecture-section, and stopPropagation."""
    for el in list(soup.find_all(['span', 'div'])):
        if el.attrs is None:
            continue
        if el.get('data-audio-badge'):
            el.decompose()
            continue
        txt = el.get_text(' ', strip=True)
        if '🎧' in txt and len(txt) <= 48:
            if not el.find(['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'table', 'svg', 'img', 'iframe', 'button', 'input']):
                el.decompose()
                continue

    for el in soup.find_all(True):
        if el.has_attr('data-lecture-section'):
            del el['data-lecture-section']
        if el.has_attr('class'):
            cls = [c for c in el['class'] if c not in ('lecture-interactive-card', 'active-lecture-highlight')]
            if cls:
                el['class'] = cls
            else:
                del el['class']
        if el.has_attr('onclick'):
            oc = el['onclick'].strip()
            if oc in ('event.stopPropagation()', 'event.stopPropagation();'):
                del el['onclick']
        if el.has_attr('style') and 'cursor: default' in el['style']:
            el['style'] = el['style'].replace('cursor: default;', '').replace('cursor: default', '').strip()


def visible_text_len(tag: Tag) -> int:
    if not isinstance(tag, Tag) or is_hidden(tag):
        return 0
    total = 0
    for s in tag.descendants:
        if isinstance(s, NavigableString):
            p = s.parent
            hid = False
            while p and p is not tag:
                if isinstance(p, Tag) and (p.name in ('style', 'script', 'svg') or is_hidden(p)):
                    hid = True
                    break
                p = p.parent
            if not hid and p and p.name not in ('style', 'script', 'svg'):
                total += len(s.strip())
    # Fallback if box is mostly an SVG diagram with short label
    if total < 35 and tag.find('svg'):
        svg_txt = ' '.join(tag.get_text().split())
        total = max(total, min(len(svg_txt), 80))
    return total


def has_box_style(tag: Tag) -> bool:
    if not isinstance(tag, Tag):
        return False
    if tag.name in ('table', 'details', 'blockquote'):
        return True
    st = (tag.get('style') or '').lower()
    if any(k in st for k in ('background:', 'background-color:', 'border:', 'border-left:', 'border-top:', 'box-shadow:')):
        if 'background: transparent' in st or 'background:transparent' in st:
            if 'border' not in st and 'box-shadow' not in st:
                return False
        return True
    return False


def is_interactive_widget(tag: Tag) -> bool:
    if not isinstance(tag, Tag):
        return False
    if tag.find(['button', 'input', 'select']):
        return True
    for attr in ('onclick', 'onmouseover', 'onmouseenter', 'onchange', 'oninput'):
        if tag.find(attrs={attr: True}):
            return True
    for d in tag.find_all(True):
        if d.name != 'svg' and is_hidden(d):
            return True
    return False


def is_skip_utility_block(tag: Tag) -> bool:
    if not isinstance(tag, Tag):
        return True
    if tag.name in ('style', 'script'):
        return True
    if is_hidden(tag):
        return True
    if tag.find('iframe'):
        return True
    tid = (tag.get('id') or '').lower()
    if tid in ('sec-nav', 'nav-quiz'):
        return True
    txt = tag.get_text(' ', strip=True)
    # Skip external FlashQuiz link grids & headings
    fq_links = [a for a in tag.find_all('a') if 'flashquiz' in (a.get('href') or '').lower()]
    if fq_links and not tag.find(['h1', 'h2', 'table', 'svg']):
        return True
    if tag.name in ('h3', 'h4') and any(k in txt.lower() for k in ('quiz', 'bài tập trắc nghiệm')):
        return True
    if len(txt) < 1600:
        if txt.lstrip().startswith('📍') and not tag.find(['h1', 'h2', 'table', 'svg']):
            return True
        anchor_links = [a for a in tag.find_all('a') if (a.get('href') or '').strip().startswith('#')]
        if len(anchor_links) >= 2 and not tag.find(['h1', 'h2', 'table', 'svg']):
            return True
    return False


def get_normalized_top_blocks(soup: BeautifulSoup) -> list:
    r_tags = [c for c in soup.contents if isinstance(c, Tag) and c.name not in ('style', 'script')]
    raw_blocks = []
    for rt in r_tags:
        if rt.get('id') == 'sec-header' or (rt.find('h1') and not rt.find('h2') and not rt.find('iframe')):
            raw_blocks.append(rt)
        else:
            ch = [c for c in rt.children if isinstance(c, Tag) and c.name not in ('style', 'script')]
            if len(ch) == 2 and (ch[0].get('id') == 'sec-header' or ch[0].find('h1')) and not ch[1].find('h1') and not ch[1].find('h2', recursive=False):
                raw_blocks.append(ch[0])
                raw_blocks.extend([x for x in ch[1].children if isinstance(x, Tag) and x.name not in ('style', 'script')])
            else:
                raw_blocks.extend(ch)

    # Unwrap any top container that groups #sec-header + FlashQuiz iframe together (e.g. physics 1..3, science p1..3)
    blocks = []
    for b in raw_blocks:
        if b.get('id') != 'sec-header' and (b.find(id='sec-header') or b.find('h1')) and b.find('iframe'):
            blocks.extend([x for x in b.children if isinstance(x, Tag) and x.name not in ('style', 'script')])
        else:
            blocks.append(b)
    return blocks


def is_multi_card_grid(node: Tag) -> list:
    if not isinstance(node, Tag) or has_box_style(node) or is_interactive_widget(node):
        return []
    st = (node.get('style') or '').lower()
    if 'grid' in st or 'flex' in st:
        cards = [c for c in node.children if isinstance(c, Tag) and not is_skip_utility_block(c) and has_box_style(c) and visible_text_len(c) >= 40]
        if len(cards) >= 2:
            return cards
    return []


# ============================================================================
# 2. DOM WRAPPING & BADGE INJECTION
# ============================================================================

def ensure_div_target(soup: BeautifulSoup, target) -> Tag:
    """
    Given either a single Tag or a list of contiguous sibling Tags,
    return a single <div> Tag suitable for .lecture-interactive-card and a child badge <div>.
    Never modifies existing IDs inside wrapped headings/tables.
    """
    if isinstance(target, list):
        nodes = [t for t in target if isinstance(t, Tag)]
        if len(nodes) == 1 and nodes[0].name == 'div':
            return nodes[0]
        wrapper = soup.new_tag('div')
        wrapper['style'] = 'position: relative; border-radius: 10px; padding: 6px 10px; margin-bottom: 10px;'
        nodes[0].insert_before(wrapper)
        for n in nodes:
            wrapper.append(n.extract())
        return wrapper

    if target.name == 'div':
        return target

    # Single non-div tag (e.g. <table>, <h2>, <h3>, <details>, <blockquote>)
    wrapper = soup.new_tag('div')
    wrapper['style'] = 'position: relative; border-radius: 10px; padding: 4px 6px; margin-bottom: 10px;'
    target.insert_before(wrapper)
    wrapper.append(target.extract())
    return wrapper


def decorate_clickable_box(soup: BeautifulSoup, div_el: Tag, sec_id: str, badge_label: str, is_major_hdr: bool = False):
    """Attach data-lecture-section, lecture-interactive-card class, cursor/position styles, and clean badge."""
    div_el['data-lecture-section'] = sec_id
    classes = list(div_el.get('class') or [])
    if 'lecture-interactive-card' not in classes:
        classes.append('lecture-interactive-card')
    div_el['class'] = classes

    st = (div_el.get('style') or '').strip()
    if st and not st.endswith(';'):
        st += ';'
    if 'position:' not in st.lower():
        st += ' position: relative;'
    if 'cursor:' not in st.lower():
        st += ' cursor: pointer;'
    div_el['style'] = st.strip()

    st_low = st.lower().replace(' ', '')
    clips = 'overflow:hidden' in st_low

    badge = soup.new_tag('div')
    badge['data-audio-badge'] = '1'
    if clips:
        pos_css = 'position: absolute; top: 10px; right: 12px;'
    else:
        pos_css = 'position: absolute; top: -10px; right: 12px;'

    if is_major_hdr:
        badge['style'] = (
            f"{pos_css} z-index: 15; background: #ecfeff; color: #0e7490; "
            "border: 1px solid #67e8f9; border-radius: 999px; padding: 2px 10px; "
            "font-size: 11px; font-weight: 700; line-height: 1.4; pointer-events: none; "
            "box-shadow: 0 1px 3px rgba(0,0,0,0.06); white-space: nowrap;"
        )
    else:
        badge['style'] = (
            f"{pos_css} z-index: 15; background: #f0f9ff; color: #0369a1; "
            "border: 1px solid #bae6fd; border-radius: 999px; padding: 1px 8px; "
            "font-size: 10.5px; font-weight: 700; line-height: 1.4; pointer-events: none; "
            "box-shadow: 0 1px 2px rgba(0,0,0,0.05); white-space: nowrap;"
        )
    badge.string = badge_label
    div_el.insert(0, badge)


# ============================================================================
# 3. SECTION BOX EXTRACTION (DOM-PRESERVING)
# ============================================================================

def extract_section_units(soup: BeautifulSoup, sec: Tag) -> dict:
    """
    Decompose a major section into structured slots:
      - 'sec_hdr': Tag (compact div wrapping leading section title + intro p)
      - 'intuition': {'hdr': Tag | None, 'cards': [Tag, ...]} | None
      - 'body': [{'kind': 'sub_hdr' | 'card' | 'interactive', 'el': Tag}, ...]
      - 'wex': {'hdr': Tag | None, 'cards': [Tag, ...]} | None
    """
    result = {
        'sec_hdr': None,
        'intuition': None,
        'body': [],
        'wex': None,
    }

    # Hoist any data-addon block accidentally nested inside a compact h2 header card
    for top_c in list(sec.children):
        if isinstance(top_c, Tag) and top_c.name == 'div' and not top_c.get('data-addon') and top_c.find('h2'):
            nested_ads = top_c.find_all('div', attrs={'data-addon': True})
            if nested_ads:
                rem_txt = visible_text_len(top_c) - sum(visible_text_len(ad) for ad in nested_ads)
                if rem_txt < 560:
                    for ad in reversed(nested_ads):
                        top_c.insert_after(ad.extract())

    has_any_h2 = bool(sec.find('h2'))
    hdr_heading_tags = ('h2', 'p') if has_any_h2 else ('h2', 'h3', 'p')

    sec_children = [c for c in sec.children if isinstance(c, Tag) and not is_skip_utility_block(c)]
    hdr_nodes = []
    rem_nodes = []
    started = False

    for c in sec_children:
        if not started:
            if c.name in hdr_heading_tags and not has_box_style(c):
                hdr_nodes.append(c)
                continue
            if c.name == 'div' and not c.get('data-addon') and c.find('h2'):
                # Check chemistry_11 P2 case where intuition was nested inside #sec-polymers
                nested_addons = [x for x in c.find_all('div', recursive=False) if x.get('data-addon')]
                if nested_addons:
                    started = True
                    inner_hdr = []
                    for subc in [x for x in c.children if isinstance(x, Tag) and not is_skip_utility_block(x)]:
                        if not subc.get('data-addon') and (subc.name in ('h2', 'p') or (subc.name == 'div' and subc.find('h2'))):
                            inner_hdr.append(subc)
                        else:
                            rem_nodes.append(subc)
                    if inner_hdr:
                        hdr_nodes.extend(inner_hdr)
                    continue
                if visible_text_len(c) < 560 and not c.find(['table', 'svg']):
                    hdr_nodes.append(c)
                    continue
            if c.name == 'div' and visible_text_len(c) < 45 and not c.find(['p', 'table', 'ul', 'svg']):
                hdr_nodes.append(c)
                continue
            started = True
        rem_nodes.append(c)

    if hdr_nodes:
        result['sec_hdr'] = ensure_div_target(soup, hdr_nodes)
    else:
        # Fallback if entire section is a single card without separate h2
        result['sec_hdr'] = ensure_div_target(soup, sec)
        return result

    def is_pure_subheading(nodes: list) -> bool:
        if not nodes:
            return False
        has_h = any(b.name in ('h3', 'h4') or b.find(['h3', 'h4']) for b in nodes)
        has_prose = any(b.name in ('p', 'ul', 'ol', 'table') or b.find(['p', 'ul', 'ol', 'table']) for b in nodes)
        tot = sum(visible_text_len(b) for b in nodes)
        return has_h and not has_prose and tot < 120

    def walk_sequence(tag_list: list):
        bare_buf = []

        def flush_bare():
            nonlocal bare_buf
            if not bare_buf:
                return
            tot = sum(visible_text_len(b) for b in bare_buf)
            has_h = any(b.name in ('h2', 'h3', 'h4') or b.find(['h2', 'h3', 'h4']) for b in bare_buf)
            joined_txt = ' '.join(b.get_text(' ', strip=True) for b in bare_buf).strip()
            # Skip standalone 1-line UI hover/click prompt paragraphs above interactive diagrams
            if not has_h and tot < 180 and re.match(r'^(?:Hover|Click|Tap|Di chuột|Lướt chuột|Bấm|Chạm)\b', joined_txt, re.I):
                bare_buf = []
                return
            if is_pure_subheading(bare_buf):
                el = ensure_div_target(soup, bare_buf)
                result['body'].append({'kind': 'sub_hdr', 'el': el})
            elif has_h or tot >= 45:
                el = ensure_div_target(soup, bare_buf)
                result['body'].append({'kind': 'card', 'el': el})
            bare_buf = []

        for c in tag_list:
            if is_skip_utility_block(c):
                continue
            if c.name in ('h3', 'h4', 'p', 'ul', 'ol') and not has_box_style(c):
                bare_buf.append(c)
            else:
                flush_bare()
                walk_block(c)
        flush_bare()

    def walk_block(node: Tag):
        if is_skip_utility_block(node):
            return
        addon = node.get('data-addon') or ''
        nid = (node.get('id') or '').lower()

        if addon == 'intuition' and result['intuition'] is None:
            dch = [c for c in node.children if isinstance(c, Tag) and not is_skip_utility_block(c)]
            hdr_el = None
            cards = []
            for idx_c, c in enumerate(dch):
                gcards = is_multi_card_grid(c)
                if gcards:
                    cards.extend([ensure_div_target(soup, gc) for gc in gcards])
                elif idx_c == 0 and visible_text_len(c) < 220 and not has_box_style(c):
                    hdr_el = ensure_div_target(soup, c)
                elif visible_text_len(c) >= 50 and has_box_style(c):
                    cards.append(ensure_div_target(soup, c))
            if cards:
                result['intuition'] = {'hdr': hdr_el, 'cards': cards}
            else:
                result['body'].append({'kind': 'card', 'el': ensure_div_target(soup, node)})
            return

        if (addon == 'worked-examples' or nid == 'sub-worked-examples') and result['wex'] is None:
            dch = [c for c in node.children if isinstance(c, Tag) and not is_skip_utility_block(c)]
            hdr_el = ensure_div_target(soup, dch[0]) if len(dch) >= 2 else None
            card_ch = dch[1:] if len(dch) >= 2 else dch
            if len(card_ch) == 1 and not has_box_style(card_ch[0]):
                card_ch = [c for c in card_ch[0].children if isinstance(c, Tag) and not is_skip_utility_block(c)]
            wcards = [ensure_div_target(soup, c) for c in card_ch if visible_text_len(c) >= 55]
            if wcards:
                result['wex'] = {'hdr': hdr_el, 'cards': wcards}
            else:
                result['body'].append({'kind': 'card', 'el': ensure_div_target(soup, node)})
            return

        if is_interactive_widget(node):
            result['body'].append({'kind': 'interactive', 'el': ensure_div_target(soup, node)})
            return

        vlen = visible_text_len(node)
        if vlen < 35:
            return

        direct_tags = [c for c in node.children if isinstance(c, Tag) and not is_skip_utility_block(c)]
        if not has_box_style(node):
            gcards = is_multi_card_grid(node)
            if gcards:
                for gc in gcards:
                    walk_block(gc)
                return
            has_child_boxes = any(has_box_style(c) or is_multi_card_grid(c) or c.get('data-addon') for c in direct_tags)
            if has_child_boxes:
                walk_sequence(direct_tags)
            else:
                if is_pure_subheading([node]):
                    result['body'].append({'kind': 'sub_hdr', 'el': ensure_div_target(soup, node)})
                else:
                    result['body'].append({'kind': 'card', 'el': ensure_div_target(soup, node)})
            return

        if node.name == 'div':
            if any(c.get('data-addon') for c in direct_tags):
                walk_sequence(direct_tags)
                return
            child_grids = [c for c in direct_tags if is_multi_card_grid(c)]
            titled_subboxes = [c for c in direct_tags if has_box_style(c) and c.find(['h3', 'h4', 'table']) and visible_text_len(c) >= 140]
            if child_grids or len(titled_subboxes) >= 2:
                walk_sequence(direct_tags)
                return

        result['body'].append({'kind': 'card', 'el': ensure_div_target(soup, node)})

    walk_sequence(rem_nodes)
    return result


# ============================================================================
# 4. STRUCTURED TEXT EXTRACTION & TTS FORMULA NORMALIZATION
# ============================================================================

UI_NOISE_PATTERNS = [
    r'🎧\s*(?:Listen to Section(?:\s*\d+)?|Listen Section|Listen to Intro|Listen to Subtopic|Listen|Overview Audio|Exam Trap Audio|Audio|Click any card to listen)',
    r'🎧\s*(?:Nghe toàn bộ mục(?:\s*\d+)?|Nghe phần mở đầu|Nghe phần giới thiệu|Nghe phần này|Nghe mục(?:\s*\d+)?|Nghe tiểu mục|Nghe giảng)',
    r'\bStudent-Friendly Guide\b',
    r'\bDễ Hiểu Nhất\b',
    r'\bCambridge Mark-Scheme Ready\b',
    r'\bChuẩn Mark Scheme Cambridge\b',
    r'(?:Hover|Click|Tap)\s+(?:or\s+(?:click|tap|hover)\s+)?(?:over|on|any)\s+[^.!\n]{5,95}(?:below|above|inspect|explore|view|see details)[^.!\n]*[.!]?',
    r'(?:Di chuột|Lướt chuột|Bấm|Chạm)\s+(?:hoặc\s+(?:bấm|chạm|nhấp)\s+)?(?:vào|qua)\s+[^.!\n]{5,110}[.!]?',
]


def format_table_to_sentences(tbl: Tag) -> str:
    rows = tbl.find_all('tr')
    if not rows:
        return ''
    headers = [ ' '.join(th.get_text(' ', strip=True).split()) for th in rows[0].find_all(['th', 'td']) ]
    has_th = bool(rows[0].find('th'))
    start_idx = 1 if has_th else 0
    lines = []
    for r in rows[start_idx:]:
        cells = [ ' '.join(td.get_text(' ', strip=True).split()) for td in r.find_all(['td', 'th']) ]
        cells = [c for c in cells if c]
        if not cells:
            continue
        if has_th and len(headers) == len(cells) and len(cells) >= 2:
            parts = [f"{headers[i]}: {cells[i]}" for i in range(len(cells))]
            lines.append('; '.join(parts) + '.')
        else:
            lines.append(' — '.join(cells) + '.')
    return ' '.join(lines)


def extract_box_text(el: Tag, include_hidden_templates: bool = False) -> str:
    """Extract clean, structured, readable sentences from a box Tag."""
    chunks = []

    def rec(node):
        if isinstance(node, NavigableString):
            t = ' '.join(str(node).split())
            if t:
                chunks.append(t)
            return
        if not isinstance(node, Tag):
            return
        if node.name in ('style', 'script'):
            return
        if node.get('data-audio-badge'):
            return
        if node.name == 'svg':
            return
        if is_hidden(node) and not include_hidden_templates:
            return
        if node.name == 'table':
            chunks.append(' ' + format_table_to_sentences(node) + ' ')
            return
        is_block = node.name in ('h1', 'h2', 'h3', 'h4', 'p', 'li', 'div', 'blockquote', 'summary', 'tr')
        is_inline_spaced = node.name in ('strong', 'b', 'em', 'i', 'span', 'a', 'code', 'mark', 'u', 'label')
        if is_block or is_inline_spaced:
            chunks.append(' ')
        for ch in node.children:
            rec(ch)
        if node.name in ('h1', 'h2', 'h3', 'h4', 'p', 'li', 'blockquote', 'summary'):
            chunks.append('. ')
        elif is_block or is_inline_spaced:
            chunks.append(' ')

    # First extract visible content
    rec_flag = include_hidden_templates
    include_hidden_templates = False
    rec(el)

    vis_text = ' '.join(''.join(chunks).split())

    # If interactive widget, append capped hidden template store text inside el
    if rec_flag:
        hid_chunks = []
        for d in el.find_all(True):
            if d.name != 'svg' and is_hidden(d) and not has_hidden_ancestor(d.parent if d.parent is not el else el):
                # Only top-level hidden panels inside el
                p = d.parent
                nested_hid = False
                while p and p is not el:
                    if is_hidden(p):
                        nested_hid = True
                        break
                    p = p.parent
                if not nested_hid:
                    t = extract_box_text(d, include_hidden_templates=False)
                    if t:
                        hid_chunks.append(t)
        if hid_chunks:
            joined_hid = ' '.join(hid_chunks)
            if len(joined_hid) > 700:
                # Truncate cleanly at sentence boundary
                cut = joined_hid[:700]
                last_dot = max(cut.rfind('. '), cut.rfind('! '), cut.rfind('? '))
                if last_dot > 250:
                    cut = cut[:last_dot + 1]
                joined_hid = cut
            vis_text = (vis_text + ' ' + joined_hid).strip()

    # Fallback if SVG-only box had minimal prose
    if len(vis_text) < 25 and el.find('svg'):
        svg_labels = []
        for tnode in el.find('svg').find_all('text'):
            lbl = ' '.join(tnode.get_text(' ', strip=True).split())
            if len(lbl) >= 2 and lbl not in svg_labels:
                svg_labels.append(lbl)
        if svg_labels:
            vis_text = (vis_text + ' ' + ', '.join(svg_labels[:12]) + '.').strip()

    # Clean noise patterns & double punctuation
    for pat in UI_NOISE_PATTERNS:
        vis_text = re.sub(pat, ' ', vis_text, flags=re.IGNORECASE)

    vis_text = re.sub(r'\s*\.\s*\.', '.', vis_text)
    vis_text = re.sub(r'([:?!])\s*\.', r'\1', vis_text)
    vis_text = re.sub(r'\s+', ' ', vis_text).strip()

    # Cap max box length at ~1550 chars at sentence boundary so no single card exceeds ~85s
    if len(vis_text) > 1550:
        cut = vis_text[:1550]
        last_dot = max(cut.rfind('. '), cut.rfind('! '), cut.rfind('? '))
        if last_dot > 600:
            vis_text = cut[:last_dot + 1].strip()
        else:
            vis_text = cut.strip() + '.'

    return vis_text


def extract_box_title(el: Tag, fallback: str) -> str:
    for h in el.find_all(['h1', 'h2', 'h3', 'h4', 'strong']):
        if h.get('data-audio-badge') or has_hidden_ancestor(h):
            continue
        t = ' '.join(h.get_text(' ', strip=True).split())
        for pat in UI_NOISE_PATTERNS:
            t = re.sub(pat, '', t, flags=re.IGNORECASE).strip()
        if len(t) >= 3:
            return t[:95]
    raw = extract_box_text(el, include_hidden_templates=False)
    return (raw[:80] + '...') if len(raw) > 80 else (raw or fallback)


def clean_vi_bilingual_duplicates(vi_text: str) -> str:
    """
    Remove full duplicate English sentences immediately followed by their Vietnamese
    translation in parentheses on Page 2 (e.g. Worked Examples), so vi-VN-HoaiMyNeural
    speaks natural Vietnamese without reading whole English paragraphs first.
    """
    text = vi_text

    # Pattern 1: English prompt sentence(s) (allowing short markers like (a), (b), (25 °C)) followed by (Vietnamese translation >= 20 chars with diacritics)
    def _unwrap_vi_paren(m):
        eng_part = m.group(1).strip()
        vi_part = m.group(2).strip()
        # Strip short markers like (a), (25 °C) when checking if eng_part has zero Vietnamese diacritics
        if not VI_DIACRITIC_RE.search(eng_part) and VI_DIACRITIC_RE.search(vi_part) and len(vi_part) >= 18:
            eng_words = re.findall(r'[A-Za-z]{3,}', eng_part)
            if len(eng_words) >= 5:
                return ' ' + vi_part + ' '
        return m.group(0)

    text = re.sub(
        r'(?:^|(?<=[.!?:;\]]))(\s*(?:\([a-z0-9°C\s]{1,10}\)\s*)?[A-Z][^()]{25,550}?(?:\([a-z0-9°C\s]{1,12}\)[^()]{5,350}?)*)\s*\(([^()]{18,700})\)',
        _unwrap_vi_paren,
        text
    )

    # Pattern 2: Remove 3+ word pure-ASCII parenthetical glosses after Vietnamese words
    def _strip_long_en_gloss(m):
        inner = m.group(1).strip()
        if not VI_DIACRITIC_RE.search(inner):
            words = re.findall(r'[A-Za-z]{2,}', inner)
            if len(words) >= 3 and '=' not in inner and '×' not in inner:
                return ''
        return m.group(0)

    text = re.sub(r'\s*\(([^()]{14,180})\)', _strip_long_en_gloss, text)
    text = re.sub(r'\[\s*\d+\s*m?\s*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def normalize_for_tts(text: str, lang: str = 'en') -> str:
    """Convert scientific formulas, subscripts, superscripts, and symbols into crisp spoken form."""
    t = EMOJI_RE.sub(' ', text)
    t = re.sub(r'\bEASY INTUITION\s*&\s*SYLLABUS MENTAL MODEL\b', ' ', t, flags=re.I)

    # Strip bare syllabus codes like (16.3.9–16.3.12), (B6.2.1 Core), [4 marks]
    t = re.sub(r'\(\s*[BCP]?\d{1,2}\.\d{1,2}(?:\.\d{1,2})?(?:\s*[–\-—]\s*[BCP]?\d{1,2}(?:\.\d{1,2})*)?\s*(?:Core|Supplement|Extended)?\s*\)', ' ', t, flags=re.I)
    t = re.sub(r'\b\d{1,2}\.\d{1,2}\.\d{1,2}(?:\s*[–\-]\s*\d{1,2}(?:\.\d{1,2})*)?\b', ' ', t)
    t = re.sub(r'\[\s*(\d+)\s*marks?\s*\]', lambda m: f" ({m.group(1)} marks) " if lang == 'en' else f" ({m.group(1)} điểm) ", t, flags=re.I)
    t = re.sub(r'#(\d+)\b', lambda m: f"Number {m.group(1)}" if lang == 'en' else f"Số {m.group(1)}", t)

    # Contextual reaction arrow vs bullet/step arrow
    def _arrow_repl(m):
        before = m.group(1)
        if '+' in before:
            return before + (' produces ' if lang == 'en' else ' tạo thành ')
        return before + ': '

    t = re.sub(r'([^.!?\n]{0,65}?)\s*(?:→|➔|⟶|⇒)\s*', _arrow_repl, t)

    # Common multi-character units & powers BEFORE general subscript/superscript pass
    if lang == 'en':
        unit_repls = [
            (r'm\s*/\s*s²|m\s*s⁻²', ' metres per second squared '),
            (r'm\s*s⁻¹', ' metres per second '),
            (r'g\s*/\s*cm³|g\s*cm⁻³', ' grams per cubic centimetre '),
            (r'kg\s*/\s*m³|kg\s*m⁻³', ' kilograms per cubic metre '),
            (r'mol\s*/\s*dm³|mol\s*dm⁻³', ' moles per cubic decimetre '),
            (r'\bcm³\b', ' cubic centimetres '),
            (r'\bdm³\b', ' cubic decimetres '),
            (r'\bm³\b', ' cubic metres '),
            (r'\bcm²\b', ' square centimetres '),
            (r'\bm²\b', ' square metres '),
            (r'10⁻(\d+)', r'10 to the power of minus \1'),
            (r'10([⁰¹²³⁴⁵⁶₇₈₉]+)', lambda m: '10 to the power of ' + ''.join(SUPERSCRIPT_DIGITS.get(ch, ch) for ch in m.group(1))),
            (r'([A-Za-z])²⁺', r'\1 2 plus '),
            (r'([A-Za-z])³⁺', r'\1 3 plus '),
            (r'([A-Za-z])²⁻', r'\1 2 minus '),
            (r'([A-Za-z])³⁻', r'\1 3 minus '),
            (r'([A-Za-z₀-₉])⁺', r'\1 plus '),
            (r'([A-Za-z₀-₉])⁻', r'\1 minus '),
            (r'([vutrIR])²\b', r'\1 squared'),
            (r'°C', ' degrees Celsius '),
            (r'ΔT|Δθ', ' change in temperature '),
            (r'ΔE', ' change in energy '),
            (r'ΔH', ' enthalpy change '),
            (r'⇌|⇄', ' is in reversible reaction with '),
            (r'μm\b', ' micrometres '),
            (r'Ω', ' ohms '),
            (r'λ', ' lambda '),
            (r'ρ', ' rho '),
            (r'×', ' times '),
            (r'÷', ' divided by '),
            (r'≈', ' approximately '),
            (r'≤', ' less than or equal to '),
            (r'≥', ' greater than or equal to '),
        ]
    else:
        t = clean_vi_bilingual_duplicates(t)
        unit_repls = [
            (r'm\s*/\s*s²|m\s*s⁻²', ' mét trên giây bình phương '),
            (r'm\s*s⁻¹', ' mét trên giây '),
            (r'g\s*/\s*cm³|g\s*cm⁻³', ' gam trên xen-ti-mét khối '),
            (r'kg\s*/\s*m³|kg\s*m⁻³', ' ki-lô-gam trên mét khối '),
            (r'mol\s*/\s*dm³|mol\s*dm⁻³', ' mol trên đề-xi-mét khối '),
            (r'\bcm³\b', ' xen-ti-mét khối '),
            (r'\bdm³\b', ' đề-xi-mét khối '),
            (r'\bm³\b', ' mét khối '),
            (r'\bcm²\b', ' xen-ti-mét vuông '),
            (r'\bm²\b', ' mét vuông '),
            (r'10⁻(\d+)', r'10 mũ trừ \1'),
            (r'10([⁰¹²³⁴⁵⁶₇₈₉]+)', lambda m: '10 mũ ' + ''.join(SUPERSCRIPT_DIGITS.get(ch, ch) for ch in m.group(1))),
            (r'([A-Za-z])²⁺', r'\1 2 cộng '),
            (r'([A-Za-z])³⁺', r'\1 3 cộng '),
            (r'([A-Za-z])²⁻', r'\1 2 trừ '),
            (r'([A-Za-z])³⁻', r'\1 3 trừ '),
            (r'([A-Za-z₀-₉])⁺', r'\1 cộng '),
            (r'([A-Za-z₀-₉])⁻', r'\1 trừ '),
            (r'([vutrIR])²\b', r'\1 bình phương'),
            (r'°C', ' độ C '),
            (r'ΔT|Δθ', ' độ biến thiên nhiệt độ '),
            (r'ΔE', ' độ biến thiên năng lượng '),
            (r'ΔH', ' biến thiên entanpi '),
            (r'⇌|⇄', ' phản ứng thuận nghịch tạo ra '),
            (r'μm\b', ' mi-crô-mét '),
            (r'Ω', ' ôm '),
            (r'λ', ' lam-đa '),
            (r'ρ', ' rô '),
            (r'×', ' nhân '),
            (r'÷', ' chia '),
            (r'≈', ' xấp xỉ '),
            (r'≤', ' nhỏ hơn hoặc bằng '),
            (r'≥', ' lớn hơn hoặc bằng '),
        ]

    for pat, rep in unit_repls:
        t = re.sub(pat, rep, t)

    # Chemical formulas with unicode subscripts: e.g. H₂SO₄ -> H 2 S O 4, CO₂ -> C O 2
    def _expand_chem(m):
        formula = m.group(0).translate(SUBSCRIPT_MAP)
        tokens = re.findall(r'[A-Z][a-z]?|\d+|\(|\)', formula)
        return ' ' + ' '.join(tokens) + ' '

    t = re.sub(r'(?:[A-Z][a-z]?[₀₁₂₃₄₅₆₇₈₉]*|\([A-Za-z₀₁₂₃₄₅₆₇₈₉]+\)[₀₁₂₃₄₅₆₇₈₉]+)+[₀₁₂₃₄₅₆₇₈₉]+', _expand_chem, t)
    t = t.translate(SUBSCRIPT_MAP)
    for sup_k, sup_v in SUPERSCRIPT_DIGITS.items():
        t = t.replace(sup_k, sup_v)

    t = t.replace('•', '. ').replace('—', ', ').replace('–', ', ')
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def split_text_proportionally(text: str, k: int) -> list:
    """Split text cleanly into k non-empty parts along sentence boundaries."""
    if k <= 1:
        return [text]
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    if len(sents) < k:
        words = text.split()
        if len(words) < k:
            return [text] * k
        step = max(1, len(words) // k)
        parts = [' '.join(words[i * step:(i + 1) * step if i < k - 1 else len(words)]) for i in range(k)]
        return [p or text for p in parts]

    total_chars = sum(len(s) for s in sents)
    target = total_chars / k
    parts = []
    cur = []
    cur_len = 0
    rem_sents = len(sents)
    for s in sents:
        cur.append(s)
        cur_len += len(s)
        rem_sents -= 1
        rem_groups = k - len(parts) - 1
        if rem_groups > 0 and (cur_len >= target * 0.75 or rem_sents == rem_groups) and rem_sents >= rem_groups:
            parts.append(' '.join(cur))
            cur = []
            cur_len = 0
    if cur:
        if len(parts) < k:
            parts.append(' '.join(cur))
        else:
            parts[-1] = parts[-1] + ' ' + ' '.join(cur)
    while len(parts) < k:
        parts.append(parts[-1])
    return parts


def similarity_score(e_txt: str, v_txt: str) -> float:
    e_toks = set(re.findall(r'[a-z0-9]{3,}', e_txt.lower()))
    v_toks = set(re.findall(r'[a-z0-9]{3,}', v_txt.lower()))
    overlap = len(e_toks & v_toks)
    len_ratio = min(len(e_txt) + 1, len(v_txt) + 1) / max(len(e_txt) + 1, len(v_txt) + 1)
    return overlap * 2.0 + len_ratio * 3.0


def partition_monotonic(m_items: list, n_items: list, m_is_en: bool = True) -> list:
    """
    Given len(m_items) >= len(n_items) >= 1, partition indices 0..M-1 into N non-empty
    contiguous ranges [(s0, e0), ..., (s_{N-1}, e_{N-1})] maximizing similarity.
    """
    M, N = len(m_items), len(n_items)
    if N == 1:
        return [(0, M - 1)]
    if M == N:
        return [(i, i) for i in range(M)]

    dp = [[(-1e9, -1)] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = (0.0, 0)
    for j in range(1, N + 1):
        for i in range(j, M - (N - j) + 1):
            best_val = -1e9
            best_prev = j - 1
            for p in range(j - 1, i):
                grp_txt = ' '.join(m_items[x] for x in range(p, i))
                sc = similarity_score(grp_txt, n_items[j - 1]) if m_is_en else similarity_score(n_items[j - 1], grp_txt)
                val = dp[j - 1][p][0] + sc
                if val > best_val:
                    best_val = val
                    best_prev = p
            dp[j][i] = (best_val, best_prev)

    ranges = []
    cur = M
    for j in range(N, 0, -1):
        prev = dp[j][cur][1]
        ranges.append((prev, cur - 1))
        cur = prev
    ranges.reverse()
    return ranges


# ============================================================================
# 5. FULL LECTURE SEGMENTATION & ALIGNMENT ENGINE
# ============================================================================

def build_lecture_plan(subj: str, code: str, lid: str, course_title: str, lecture_title: str, raw_p1: str, raw_p2: str) -> dict:
    soup1 = BeautifulSoup(raw_p1, 'html.parser')
    soup2 = BeautifulSoup(raw_p2, 'html.parser')

    clean_old_audio_artifacts(soup1)
    clean_old_audio_artifacts(soup2)

    blocks1 = [b for b in get_normalized_top_blocks(soup1) if not is_skip_utility_block(b)]
    blocks2 = [b for b in get_normalized_top_blocks(soup2) if not is_skip_utility_block(b)]
    assert len(blocks1) == len(blocks2), f"Top block mismatch on {subj}/{code}: P1={len(blocks1)} vs P2={len(blocks2)}"

    segments = []
    major_sections = {}

    # --- 0. Top Hero Banner (intro) ---
    hero1 = ensure_div_target(soup1, blocks1[0])
    hero2 = ensure_div_target(soup2, blocks2[0])
    decorate_clickable_box(soup1, hero1, 'intro', '🎧 Listen to Intro', is_major_hdr=True)
    decorate_clickable_box(soup2, hero2, 'intro', '🎧 Nghe mở đầu', is_major_hdr=True)

    intro_en = extract_box_text(hero1, include_hidden_templates=False)
    intro_vi = clean_vi_bilingual_duplicates(extract_box_text(hero2, include_hidden_templates=False))
    segments.append({
        'id': 'intro',
        'title': extract_box_title(hero2, lecture_title),
        'selector': '[data-lecture-section="intro"]',
        'en': intro_en,
        'vi': intro_vi,
        'en_tts': normalize_for_tts(intro_en, 'en'),
        'vi_tts': normalize_for_tts(intro_vi, 'vi'),
    })
    major_sections['intro'] = {'start': 0, 'end': 0}

    # --- 1..K. Major Sections ---
    for s_idx in range(1, len(blocks1)):
        sec_tag = f"s{s_idx:02d}"
        u1 = extract_section_units(soup1, blocks1[s_idx])
        u2 = extract_section_units(soup2, blocks2[s_idx])

        sec_start_seg_idx = len(segments)

        # A. Major Section Header Segment
        hdr_id = f"{sec_tag}_hdr"
        decorate_clickable_box(soup1, u1['sec_hdr'], hdr_id, '🎧 Listen to Section', is_major_hdr=True)
        decorate_clickable_box(soup2, u2['sec_hdr'], hdr_id, '🎧 Nghe phần này', is_major_hdr=True)

        hdr_en = extract_box_text(u1['sec_hdr'], include_hidden_templates=False)
        hdr_vi = clean_vi_bilingual_duplicates(extract_box_text(u2['sec_hdr'], include_hidden_templates=False))
        segments.append({
            'id': hdr_id,
            'title': extract_box_title(u2['sec_hdr'], f"Section {s_idx}"),
            'selector': f'[data-lecture-section="{hdr_id}"]',
            'en': hdr_en,
            'vi': hdr_vi,
            'en_tts': normalize_for_tts(hdr_en, 'en'),
            'vi_tts': normalize_for_tts(hdr_vi, 'vi'),
        })

        box_counter = 1

        def add_paired_cards(cards1: list, cards2: list, is_interactive_flags1=None, is_interactive_flags2=None, sub_range_hdr1=None, sub_range_hdr2=None, sub_range_id=None, hdr_en_label='🎧 Listen', hdr_vi_label='🎧 Nghe phần này'):
            nonlocal box_counter
            if not cards1 and not cards2:
                return
            range_start = len(segments)

            if len(cards1) == len(cards2):
                for k in range(len(cards1)):
                    cid = f"{sec_tag}_b{box_counter:02d}"
                    box_counter += 1
                    c1, c2 = cards1[k], cards2[k]
                    f1 = is_interactive_flags1[k] if is_interactive_flags1 else False
                    f2 = is_interactive_flags2[k] if is_interactive_flags2 else False
                    decorate_clickable_box(soup1, c1, cid, '🎧 Audio')
                    decorate_clickable_box(soup2, c2, cid, '🎧 Nghe giảng')
                    en_txt = extract_box_text(c1, include_hidden_templates=f1)
                    vi_txt = clean_vi_bilingual_duplicates(extract_box_text(c2, include_hidden_templates=f2))
                    segments.append({
                        'id': cid,
                        'title': extract_box_title(c2, extract_box_title(c1, cid)),
                        'selector': f'[data-lecture-section="{cid}"]',
                        'en': en_txt,
                        'vi': vi_txt,
                        'en_tts': normalize_for_tts(en_txt, 'en'),
                        'vi_tts': normalize_for_tts(vi_txt, 'vi'),
                    })
            elif len(cards1) > 0 and len(cards2) == 0:
                # Fold into P1 cards using hdr_vi fallback
                for c1 in cards1:
                    cid = f"{sec_tag}_b{box_counter:02d}"
                    box_counter += 1
                    decorate_clickable_box(soup1, c1, cid, '🎧 Audio')
                    en_txt = extract_box_text(c1, include_hidden_templates=is_interactive_widget(c1))
                    segments.append({
                        'id': cid,
                        'title': extract_box_title(c1, cid),
                        'selector': f'[data-lecture-section="{cid}"], [data-lecture-section="{hdr_id}"]',
                        'en': en_txt,
                        'vi': hdr_vi,
                        'en_tts': normalize_for_tts(en_txt, 'en'),
                        'vi_tts': normalize_for_tts(hdr_vi, 'vi'),
                    })
            elif len(cards2) > 0 and len(cards1) == 0:
                for c2 in cards2:
                    cid = f"{sec_tag}_b{box_counter:02d}"
                    box_counter += 1
                    decorate_clickable_box(soup2, c2, cid, '🎧 Nghe giảng')
                    vi_txt = clean_vi_bilingual_duplicates(extract_box_text(c2, include_hidden_templates=is_interactive_widget(c2)))
                    segments.append({
                        'id': cid,
                        'title': extract_box_title(c2, cid),
                        'selector': f'[data-lecture-section="{cid}"], [data-lecture-section="{hdr_id}"]',
                        'en': hdr_en,
                        'vi': vi_txt,
                        'en_tts': normalize_for_tts(hdr_en, 'en'),
                        'vi_tts': normalize_for_tts(vi_txt, 'vi'),
                    })
            elif len(cards1) > len(cards2):
                txts1 = [extract_box_text(c, include_hidden_templates=is_interactive_widget(c)) for c in cards1]
                txts2 = [extract_box_text(c, include_hidden_templates=is_interactive_widget(c)) for c in cards2]
                groups = partition_monotonic(txts1, txts2, m_is_en=True)
                for j, (ga, gb) in enumerate(groups):
                    c2 = cards2[j]
                    vi_full = clean_vi_bilingual_duplicates(txts2[j])
                    k_cnt = gb - ga + 1
                    if k_cnt == 1:
                        cid = f"{sec_tag}_b{box_counter:02d}"
                        box_counter += 1
                        decorate_clickable_box(soup1, cards1[ga], cid, '🎧 Audio')
                        decorate_clickable_box(soup2, c2, cid, '🎧 Nghe giảng')
                        segments.append({
                            'id': cid,
                            'title': extract_box_title(c2, extract_box_title(cards1[ga], cid)),
                            'selector': f'[data-lecture-section="{cid}"]',
                            'en': txts1[ga],
                            'vi': vi_full,
                            'en_tts': normalize_for_tts(txts1[ga], 'en'),
                            'vi_tts': normalize_for_tts(vi_full, 'vi'),
                        })
                    else:
                        vi_parts = split_text_proportionally(vi_full, k_cnt)
                        grp_id = f"{sec_tag}_grp{box_counter:02d}"
                        grp_start = len(segments)
                        decorate_clickable_box(soup2, c2, grp_id, '🎧 Nghe giảng')
                        for offset, i_idx in enumerate(range(ga, gb + 1)):
                            cid = f"{sec_tag}_b{box_counter:02d}"
                            box_counter += 1
                            decorate_clickable_box(soup1, cards1[i_idx], cid, '🎧 Audio')
                            segments.append({
                                'id': cid,
                                'title': extract_box_title(cards1[i_idx], extract_box_title(c2, cid)),
                                'selector': f'[data-lecture-section="{cid}"], [data-lecture-section="{grp_id}"]',
                                'en': txts1[i_idx],
                                'vi': vi_parts[offset],
                                'en_tts': normalize_for_tts(txts1[i_idx], 'en'),
                                'vi_tts': normalize_for_tts(vi_parts[offset], 'vi'),
                            })
                        major_sections[grp_id] = {'start': grp_start, 'end': len(segments) - 1}
            else:
                # len(cards2) > len(cards1)
                txts1 = [extract_box_text(c, include_hidden_templates=is_interactive_widget(c)) for c in cards1]
                txts2 = [extract_box_text(c, include_hidden_templates=is_interactive_widget(c)) for c in cards2]
                groups = partition_monotonic(txts2, txts1, m_is_en=False)
                for i_idx, (ga, gb) in enumerate(groups):
                    c1 = cards1[i_idx]
                    en_full = txts1[i_idx]
                    k_cnt = gb - ga + 1
                    if k_cnt == 1:
                        cid = f"{sec_tag}_b{box_counter:02d}"
                        box_counter += 1
                        decorate_clickable_box(soup1, c1, cid, '🎧 Audio')
                        decorate_clickable_box(soup2, cards2[ga], cid, '🎧 Nghe giảng')
                        vi_clean = clean_vi_bilingual_duplicates(txts2[ga])
                        segments.append({
                            'id': cid,
                            'title': extract_box_title(cards2[ga], extract_box_title(c1, cid)),
                            'selector': f'[data-lecture-section="{cid}"]',
                            'en': en_full,
                            'vi': vi_clean,
                            'en_tts': normalize_for_tts(en_full, 'en'),
                            'vi_tts': normalize_for_tts(vi_clean, 'vi'),
                        })
                    else:
                        en_parts = split_text_proportionally(en_full, k_cnt)
                        grp_id = f"{sec_tag}_grp{box_counter:02d}"
                        grp_start = len(segments)
                        decorate_clickable_box(soup1, c1, grp_id, '🎧 Audio')
                        for offset, j_idx in enumerate(range(ga, gb + 1)):
                            cid = f"{sec_tag}_b{box_counter:02d}"
                            box_counter += 1
                            decorate_clickable_box(soup2, cards2[j_idx], cid, '🎧 Nghe giảng')
                            vi_clean = clean_vi_bilingual_duplicates(txts2[j_idx])
                            segments.append({
                                'id': cid,
                                'title': extract_box_title(cards2[j_idx], extract_box_title(c1, cid)),
                                'selector': f'[data-lecture-section="{cid}"], [data-lecture-section="{grp_id}"]',
                                'en': en_parts[offset],
                                'vi': vi_clean,
                                'en_tts': normalize_for_tts(en_parts[offset], 'en'),
                                'vi_tts': normalize_for_tts(vi_clean, 'vi'),
                            })
                        major_sections[grp_id] = {'start': grp_start, 'end': len(segments) - 1}

            range_end = len(segments) - 1
            if sub_range_id and range_end >= range_start:
                if sub_range_hdr1 is not None:
                    decorate_clickable_box(soup1, sub_range_hdr1, sub_range_id, hdr_en_label, is_major_hdr=True)
                if sub_range_hdr2 is not None:
                    decorate_clickable_box(soup2, sub_range_hdr2, sub_range_id, hdr_vi_label, is_major_hdr=True)
                if sub_range_hdr1 is not None or sub_range_hdr2 is not None:
                    major_sections[sub_range_id] = {'start': range_start, 'end': range_end}

        # B. Intuition Addon Box (Mental Model Cards)
        if u1['intuition'] or u2['intuition']:
            ic1 = u1['intuition']['cards'] if u1['intuition'] else []
            ic2 = u2['intuition']['cards'] if u2['intuition'] else []
            ih1 = u1['intuition']['hdr'] if u1['intuition'] else None
            ih2 = u2['intuition']['hdr'] if u2['intuition'] else None
            add_paired_cards(
                ic1, ic2,
                sub_range_hdr1=ih1, sub_range_hdr2=ih2,
                sub_range_id=f"{sec_tag}_int",
                hdr_en_label='🎧 Listen to Mental Model',
                hdr_vi_label='🎧 Nghe bản chất'
            )

        # C. Section Body Content Boxes + Pure Sub-Headings (<h3>)
        body1_cards = [x for x in u1['body'] if x['kind'] != 'sub_hdr']
        body2_cards = [x for x in u2['body'] if x['kind'] != 'sub_hdr']
        body_start_seg_idx = len(segments)

        # Map each card Tag -> its assigned segment index range so pure sub_hdrs can bind to the cards right below them!
        add_paired_cards(
            [x['el'] for x in body1_cards],
            [x['el'] for x in body2_cards],
            is_interactive_flags1=[x['kind'] == 'interactive' for x in body1_cards],
            is_interactive_flags2=[x['kind'] == 'interactive' for x in body2_cards],
        )

        # Bind any pure sub-headings (<h3>) on P1 and P2 to the contiguous card span beneath them!
        def bind_sub_headers(body_items: list, soup_obj: BeautifulSoup, page_tag: str, badge_txt: str):
            sub_counter = 1
            for idx_item, item in enumerate(body_items):
                if item['kind'] != 'sub_hdr':
                    continue
                # Find cards following this sub_hdr until the next sub_hdr
                following_dls = []
                for nxt in body_items[idx_item + 1:]:
                    if nxt['kind'] == 'sub_hdr':
                        break
                    dls = nxt['el'].get('data-lecture-section')
                    if dls:
                        following_dls.append(dls)
                if not following_dls:
                    continue
                # Resolve start..end segment indices
                seg_indices = []
                for dls in following_dls:
                    if dls in major_sections:
                        seg_indices.append(major_sections[dls]['start'])
                        seg_indices.append(major_sections[dls]['end'])
                    else:
                        for si_k, sg in enumerate(segments):
                            if sg['id'] == dls:
                                seg_indices.append(si_k)
                                break
                if seg_indices:
                    sub_id = f"{sec_tag}_{page_tag}_sub{sub_counter:02d}"
                    sub_counter += 1
                    decorate_clickable_box(soup_obj, item['el'], sub_id, badge_txt, is_major_hdr=True)
                    major_sections[sub_id] = {'start': min(seg_indices), 'end': max(seg_indices)}

        bind_sub_headers(u1['body'], soup1, 'p1', '🎧 Listen')
        bind_sub_headers(u2['body'], soup2, 'p2', '🎧 Nghe mục nhỏ')

        # D. Worked Exam Examples Addon Box
        if u1['wex'] or u2['wex']:
            wc1 = u1['wex']['cards'] if u1['wex'] else []
            wc2 = u2['wex']['cards'] if u2['wex'] else []
            wh1 = u1['wex']['hdr'] if u1['wex'] else None
            wh2 = u2['wex']['hdr'] if u2['wex'] else None
            add_paired_cards(
                wc1, wc2,
                sub_range_hdr1=wh1, sub_range_hdr2=wh2,
                sub_range_id=f"{sec_tag}_wex",
                hdr_en_label='🎧 Listen to Examples',
                hdr_vi_label='🎧 Nghe bài mẫu'
            )

        sec_end_seg_idx = len(segments) - 1
        major_sections[hdr_id] = {'start': sec_start_seg_idx, 'end': sec_end_seg_idx}

    out_p1 = str(soup1)
    out_p2 = str(soup2)

    return {
        'subject': subj,
        'code': code,
        'lectureId': lid,
        'courseTitle': course_title,
        'lectureTitle': lecture_title,
        'p1_html': out_p1,
        'p2_html': out_p2,
        'segments': segments,
        'majorSections': major_sections,
    }


# ============================================================================
# 6. STRICT VERIFICATION SUITE (PRE- & POST-TTS)
# ============================================================================

def verify_lecture_plan(plan: dict, raw_p1: str, raw_p2: str):
    key = f"{plan['subject']}/{plan['code']}"
    p1, p2 = plan['p1_html'], plan['p2_html']

    # 1. Div balance check
    d1 = len(re.findall(r'<div\b', p1, re.I)) - len(re.findall(r'</div>', p1, re.I))
    d2 = len(re.findall(r'<div\b', p2, re.I)) - len(re.findall(r'</div>', p2, re.I))
    assert d1 == 0, f"[{key}] P1 div imbalance: {d1}"
    assert d2 == 0, f"[{key}] P2 div imbalance: {d2}"

    s1 = BeautifulSoup(p1, 'html.parser')
    s2 = BeautifulSoup(p2, 'html.parser')
    orig1 = BeautifulSoup(raw_p1, 'html.parser')
    orig2 = BeautifulSoup(raw_p2, 'html.parser')

    # 2. Interactive preservation check (scripts, svgs, hidden template stores)
    assert len(s1.find_all('script')) == len(orig1.find_all('script')), f"[{key}] P1 script count changed"
    assert len(s2.find_all('script')) == len(orig2.find_all('script')), f"[{key}] P2 script count changed"
    assert len(s1.find_all('svg')) == len(orig1.find_all('svg')), f"[{key}] P1 svg count changed"
    assert len(s2.find_all('svg')) == len(orig2.find_all('svg')), f"[{key}] P2 svg count changed"

    hid1_before = sum(1 for t in orig1.find_all(True) if t.name != 'svg' and is_hidden(t))
    hid1_after = sum(1 for t in s1.find_all(True) if t.name != 'svg' and is_hidden(t))
    hid2_before = sum(1 for t in orig2.find_all(True) if t.name != 'svg' and is_hidden(t))
    hid2_after = sum(1 for t in s2.find_all(True) if t.name != 'svg' and is_hidden(t))
    assert hid1_before == hid1_after, f"[{key}] P1 display:none count changed ({hid1_before} -> {hid1_after})"
    assert hid2_before == hid2_after, f"[{key}] P2 display:none count changed ({hid2_before} -> {hid2_after})"

    # 3. Every segment selector matches visible element on BOTH P1 and P2, and non-empty TTS text
    seg_ids = {sg['id'] for sg in plan['segments']}
    major_ids = set(plan['majorSections'].keys())

    for sg in plan['segments']:
        sel = sg['selector']
        m1 = [el for el in s1.select(sel) if not has_hidden_ancestor(el)]
        m2 = [el for el in s2.select(sel) if not has_hidden_ancestor(el)]
        assert len(m1) >= 1, f"[{key}] Selector {sel} missing or hidden on P1"
        assert len(m2) >= 1, f"[{key}] Selector {sel} missing or hidden on P2"
        assert len(sg['en_tts']) >= 3, f"[{key}] Empty en_tts on {sg['id']}"
        assert len(sg['vi_tts']) >= 3, f"[{key}] Empty vi_tts on {sg['id']}"

    # 4. Every [data-lecture-section] on P1 and P2 resolves in segments or majorSections & is visible
    for pn, sp in [('P1', s1), ('P2', s2)]:
        for el in sp.find_all(attrs={'data-lecture-section': True}):
            dls = el['data-lecture-section']
            assert not has_hidden_ancestor(el), f"[{key}] {pn} data-lecture-section={dls} placed inside display:none!"
            assert dls in seg_ids or dls in major_ids, f"[{key}] {pn} unresolved data-lecture-section={dls}"

    # 5. Page 1 badges contain zero Vietnamese diacritics
    for b in s1.find_all(attrs={'data-audio-badge': True}):
        assert not VI_DIACRITIC_RE.search(b.get_text()), f"[{key}] Vietnamese leaked into P1 badge: {b.get_text()}"


# ============================================================================
# 7. CONCURRENT CONTENT-HASH CACHED TTS & FFMPEG SYNTHESIS
# ============================================================================

def get_audio_duration(file_path: str) -> float:
    cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        file_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return round(float(res.stdout.strip()), 2)


# Global rate-pacing gates & shared HTTP session
_EN_SEM = None
_VI_SEM = None
_EN_PACING_LOCK = None
_VI_PACING_LOCK = None
_LAST_EN_TS = 0.0
_LAST_VI_TS = 0.0
_VI_COOLDOWN_UNTIL = 0.0
_HTTP_SESSION = None
_GTTS_RR_IDX = 0

GTTS_ENDPOINTS = [
    ('https://translate.googleapis.com/translate_tts', 'tw-ob'),
    ('https://translate.google.com/translate_tts', 'tw-ob'),
    ('https://translate.googleapis.com/translate_tts', 'gtx'),
]


def _split_tts_chunks(text: str, max_chars: int = 750) -> list:
    """
    Split text at sentence/clause/word boundaries into chunks <= max_chars
    with zero empty/punctuation-only chunks.
    """
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if re.search(r'[A-Za-z0-9À-ỹ]', text) else []

    raw_sents = re.split(r'(?<=[.!?;:])\s+', text)
    chunks = []
    cur = ''
    for s in raw_sents:
        s = s.strip()
        if not s or not re.search(r'[A-Za-z0-9À-ỹ]', s):
            continue
        if len(s) > max_chars:
            parts = re.split(r'(?<=,)\s+', s)
        else:
            parts = [s]
        for p in parts:
            p = p.strip()
            if not p:
                continue
            if len(p) > max_chars:
                words = p.split()
                wcur = ''
                for w in words:
                    if len(wcur) + len(w) + 1 <= max_chars:
                        wcur = f"{wcur} {w}".strip()
                    else:
                        if re.search(r'[A-Za-z0-9À-ỹ]', wcur):
                            chunks.append(wcur)
                        wcur = w
                if re.search(r'[A-Za-z0-9À-ỹ]', wcur):
                    p = wcur
                else:
                    continue
            if cur and len(cur) + len(p) + 1 > max_chars:
                if re.search(r'[A-Za-z0-9À-ỹ]', cur):
                    chunks.append(cur)
                cur = p
            else:
                cur = f"{cur} {p}".strip()
    if cur and re.search(r'[A-Za-z0-9À-ỹ]', cur):
        chunks.append(cur)
    return chunks or [text[:max_chars]]


async def _acquire_paced_slot(is_vi: bool):
    global _LAST_EN_TS, _LAST_VI_TS, _VI_COOLDOWN_UNTIL
    loop = asyncio.get_running_loop()
    if is_vi:
        async with _VI_PACING_LOCK:
            now = loop.time()
            if now < _VI_COOLDOWN_UNTIL:
                await asyncio.sleep(_VI_COOLDOWN_UNTIL - now)
                now = loop.time()
            wait = (_LAST_VI_TS + 0.08) - now
            if wait > 0:
                await asyncio.sleep(wait)
            _LAST_VI_TS = loop.time()
    else:
        async with _EN_PACING_LOCK:
            now = loop.time()
            wait = (_LAST_EN_TS + 0.14) - now
            if wait > 0:
                await asyncio.sleep(wait)
            _LAST_EN_TS = loop.time()


async def _gtts_fetch_chunk(chunk_text: str, tl: str = 'vi', max_retries: int = 12) -> bytes:
    """Fetch 24kHz mono neural MP3 audio chunk via round-robin Google TTS endpoints."""
    global _GTTS_RR_IDX, _VI_COOLDOWN_UNTIL
    is_vi = tl.startswith('vi')
    sem = _VI_SEM if is_vi else _EN_SEM

    for attempt in range(1, max_retries + 1):
        try:
            async with sem:
                await _acquire_paced_slot(is_vi)
                base_url, client_id = GTTS_ENDPOINTS[(_GTTS_RR_IDX + attempt) % len(GTTS_ENDPOINTS)]
                _GTTS_RR_IDX += 1
                q_enc = urllib.parse.quote(chunk_text)
                url = f"{base_url}?ie=UTF-8&client={client_id}&tl={tl}&q={q_enc}"
                async with _HTTP_SESSION.get(
                    url,
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'},
                    timeout=aiohttp.ClientTimeout(total=15.0)
                ) as resp:
                    if resp.status != 200:
                        raise RuntimeError(f"HTTP {resp.status}")
                    data = await resp.read()
                    if len(data) > 300:
                        return data
                    raise RuntimeError(f"Tiny gTTS payload ({len(data)} B)")
        except Exception as e:
            if attempt == max_retries:
                raise
            if is_vi and '429' in str(e):
                loop = asyncio.get_running_loop()
                _VI_COOLDOWN_UNTIL = max(_VI_COOLDOWN_UNTIL, loop.time() + min(5.0 * attempt, 25.0))
            wait = min(attempt * 1.5, 12.0)
            print(f"    [GTTS RETRY {attempt}/{max_retries}] {tl} ({len(chunk_text)}c): {e} -> wait {wait:.1f}s", flush=True)
            await asyncio.sleep(wait)


async def _edge_en_chunk_with_fallback(chunk_text: str, voice: str = EN_VOICE) -> bytes:
    """Synthesize English chunk via Edge TTS RyanNeural, with automatic en-GB fallback after 5 retries."""
    for attempt in range(1, 7):
        try:
            async with _EN_SEM:
                await _acquire_paced_slot(is_vi=False)
                comm = edge_tts.Communicate(chunk_text, voice, boundary='WordBoundary')
                buf = bytearray()
                async def _collect():
                    async for msg in comm.stream():
                        if msg['type'] == 'audio':
                            buf.extend(msg['data'])
                await asyncio.wait_for(_collect(), timeout=22.0)
                if len(buf) > 300:
                    return bytes(buf)
                raise RuntimeError(f"Empty Edge EN buffer ({len(buf)} B)")
        except Exception as e:
            if attempt >= 5:
                print(f"    [EN FALLBACK->en-GB] Edge EN failed 5x ({e!r}), using en-GB neural HTTP fallback", flush=True)
                sub_chunks = _split_tts_chunks(chunk_text, max_chars=175)
                fb_buf = bytearray()
                for sc in sub_chunks:
                    fb_buf.extend(await _gtts_fetch_chunk(sc, tl='en-GB'))
                return bytes(fb_buf)
            wait = attempt * 1.5
            print(f"    [EN RETRY {attempt}/5] {voice} ({len(chunk_text)}c): {e!r} -> wait {wait:.1f}s", flush=True)
            await asyncio.sleep(wait)


async def _tts_save_en(text: str, out_file: str):
    chunks = _split_tts_chunks(text, max_chars=750)
    merged = bytearray()
    for ch in chunks:
        merged.extend(await _edge_en_chunk_with_fallback(ch, EN_VOICE))
    with open(out_file, 'wb') as f:
        f.write(merged)


async def _tts_save_vi(text: str, out_file: str):
    chunks = _split_tts_chunks(text, max_chars=175)
    merged = bytearray()
    for ch in chunks:
        merged.extend(await _gtts_fetch_chunk(ch, tl='vi'))
    with open(out_file, 'wb') as f:
        f.write(merged)


def compute_tts_hash(en_tts: str, vi_tts: str) -> str:
    payload = f"{EN_VOICE}|||{en_tts}|||{VI_VOICE}|||{vi_tts}".encode('utf-8')
    return hashlib.sha256(payload).hexdigest()[:24]


def get_or_cache_duration_sync(mp3_path: str) -> float:
    dur_file = mp3_path + '.dur'
    if os.path.exists(dur_file):
        try:
            val = float(open(dur_file, 'r', encoding='utf-8').read().strip())
            if val > 0.2:
                return val
        except Exception:
            pass
    dur = get_audio_duration(mp3_path)
    with open(dur_file, 'w', encoding='utf-8') as df:
        df.write(f"{dur}\n")
    return dur


async def synthesize_unique_hash(hkey: str, en_tts: str, vi_tts: str, progress: dict, hash_durations: dict):
    cached_mp3 = os.path.join(CACHE_DIR, f"{hkey}.mp3")
    if os.path.exists(cached_mp3) and os.path.getsize(cached_mp3) > 1500:
        hash_durations[hkey] = await asyncio.to_thread(get_or_cache_duration_sync, cached_mp3)
        progress['done'] += 1
        return

    en_tmp = os.path.join(TEMP_DIR, f"{hkey}_en.mp3")
    vi_tmp = os.path.join(TEMP_DIR, f"{hkey}_vi.mp3")
    out_tmp = os.path.join(TEMP_DIR, f"{hkey}_merged.mp3")

    sub_tasks = []
    if not (os.path.exists(en_tmp) and os.path.getsize(en_tmp) > 400):
        sub_tasks.append(_tts_save_en(en_tts, en_tmp))
    if not (os.path.exists(vi_tmp) and os.path.getsize(vi_tmp) > 400):
        sub_tasks.append(_tts_save_vi(vi_tts, vi_tmp))
    if sub_tasks:
        await asyncio.gather(*sub_tasks)

    def _merge_and_probe():
        filter_cmd = [
            'ffmpeg', '-y',
            '-i', en_tmp,
            '-f', 'lavfi', '-t', '0.35', '-i', 'anullsrc=r=24000:cl=mono',
            '-i', vi_tmp,
            '-filter_complex', '[2:a]atempo=1.08[vi_s];[0:a][1:a][vi_s]concat=n=3:v=0:a=1[out]',
            '-map', '[out]',
            '-ac', '1', '-ar', '24000', '-b:a', '48k',
            out_tmp
        ]
        subprocess.run(filter_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        os.replace(out_tmp, cached_mp3)
        for ftmp in (en_tmp, vi_tmp):
            if os.path.exists(ftmp):
                try:
                    os.remove(ftmp)
                except Exception:
                    pass
        return get_or_cache_duration_sync(cached_mp3)

    hash_durations[hkey] = await asyncio.to_thread(_merge_and_probe)

    progress['done'] += 1
    done = progress['done']
    tot = progress['total']
    if done % 40 == 0 or done == tot:
        print(f"  [TTS PROGRESS] {done}/{tot} unique segments ready ({done*100.0/tot:.1f}%)", flush=True)


def update_supabase_with_retry(lid: str, page_num: int, html: str, max_retries: int = 8):
    import time
    for attempt in range(1, max_retries + 1):
        try:
            res = sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', page_num).execute()
            assert len(res.data) >= 1, f"0 rows updated for {lid} p{page_num}"
            return
        except Exception as e:
            if attempt == max_retries:
                raise
            time.sleep(attempt * 1.5)


def is_lecture_already_deployed(plan: dict, out_dir: str) -> bool:
    manifest_path = os.path.join(out_dir, 'manifest.json')
    if not os.path.exists(manifest_path):
        return False
    try:
        man = json.load(open(manifest_path, 'r', encoding='utf-8'))
        if man.get('lectureId') != plan['lectureId']:
            return False
        man_segs = man.get('segments', [])
        if len(man_segs) != len(plan['segments']):
            return False
        for ms, ps in zip(man_segs, plan['segments']):
            if ms.get('id') != ps['id'] or ms.get('selector') != ps['selector']:
                return False
            src_mp3 = os.path.join(CACHE_DIR, f"{ps['tts_hash']}.mp3")
            dst_mp3 = os.path.join(out_dir, f"{ps['id']}.mp3")
            if not (os.path.exists(src_mp3) and os.path.exists(dst_mp3)):
                return False
            if os.path.getsize(src_mp3) != os.path.getsize(dst_mp3):
                return False
        return True
    except Exception:
        return False


def deploy_lecture_sync(plan: dict, hash_durations: dict, force_deploy: bool = False) -> tuple:
    subj = plan['subject']
    code = plan['code']
    lid = plan['lectureId']
    out_dir = os.path.join(REPO_ROOT, 'public', 'audio', 'lectures', subj, code)
    os.makedirs(out_dir, exist_ok=True)

    if not force_deploy and is_lecture_already_deployed(plan, out_dir):
        man = json.load(open(os.path.join(out_dir, 'manifest.json'), 'r', encoding='utf-8'))
        return (True, len(plan['segments']), man.get('totalDuration', 0.0))

    expected_mp3s = {f"{sg['id']}.mp3" for sg in plan['segments']}
    for fname in os.listdir(out_dir):
        if fname.endswith('.mp3') and fname not in expected_mp3s:
            os.remove(os.path.join(out_dir, fname))

    curr_time = 0.0
    manifest_segments = []
    for sg in plan['segments']:
        hkey = sg['tts_hash']
        src_mp3 = os.path.join(CACHE_DIR, f"{hkey}.mp3")
        dst_mp3 = os.path.join(out_dir, f"{sg['id']}.mp3")
        shutil.copy2(src_mp3, dst_mp3)

        dur = hash_durations.get(hkey)
        if dur is None:
            dur = get_or_cache_duration_sync(src_mp3)
            hash_durations[hkey] = dur

        st_time = round(curr_time, 2)
        curr_time += dur
        end_time = round(curr_time, 2)

        manifest_segments.append({
            'id': sg['id'],
            'title': sg['title'],
            'selector': sg['selector'],
            'en': sg['en'],
            'vi': sg['vi'],
            'duration': dur,
            'startTime': st_time,
            'endTime': end_time,
            'audioUrl': f"/audio/lectures/{subj}/{code}/{sg['id']}.mp3",
        })

    manifest = {
        'lectureId': lid,
        'courseTitle': plan['courseTitle'],
        'lectureTitle': plan['lectureTitle'],
        'totalDuration': round(curr_time, 2),
        'majorSections': plan['majorSections'],
        'segments': manifest_segments,
    }
    with open(os.path.join(out_dir, 'manifest.json'), 'w', encoding='utf-8') as mf:
        json.dump(manifest, mf, indent=2, ensure_ascii=False)

    update_supabase_with_retry(lid, 1, plan['p1_html'])
    update_supabase_with_retry(lid, 2, plan['p2_html'])
    return (False, len(manifest_segments), round(curr_time, 2))


# ============================================================================
# 8. MAIN ENTRYPOINT
# ============================================================================

async def async_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Verify all 76 lectures without TTS or DB writes')
    parser.add_argument('--execute', action='store_true', help='Synthesize all MP3s, write manifests, and update Supabase')
    parser.add_argument('--force-deploy', action='store_true', help='Re-write manifest and Supabase even if already deployed')
    parser.add_argument('--concurrency', type=int, default=5, help='Max concurrent segment workers')
    parser.add_argument('--only', type=str, default='', help='Optional comma-separated filter e.g. biology/1,chemistry/1')
    args = parser.parse_args()

    if not args.dry_run and not args.execute:
        args.dry_run = True

    only_set = {x.strip() for x in args.only.split(',') if x.strip()}

    os.makedirs(CACHE_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)

    plans = []
    unique_tts_jobs = {}
    ordered_hashes = []
    total_segs = 0

    print(f"Building & verifying granular box plans for {len(LECTURE_SPECS)} Science lectures...", flush=True)

    for subj, code, lid, course_title in LECTURE_SPECS:
        tag = f"{subj}/{code}"
        if only_set and tag not in only_set:
            continue

        bdir = os.path.join(BACKUP_DIR, f"{subj}_{code}")
        if os.path.exists(os.path.join(bdir, 'meta.json')):
            meta = json.load(open(os.path.join(bdir, 'meta.json'), encoding='utf-8'))
            lecture_title = meta['lectureTitle']
            raw_p1 = open(os.path.join(bdir, 'p1.html'), encoding='utf-8').read()
            raw_p2 = open(os.path.join(bdir, 'p2.html'), encoding='utf-8').read()
        else:
            lec = sb.table('lectures').select('title').eq('id', lid).execute().data[0]
            lecture_title = lec['title']
            pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).in_('page_number', [1, 2]).execute().data
            pmap = {p['page_number']: p['content_html'] or '' for p in pages}
            raw_p1, raw_p2 = pmap[1], pmap[2]

        plan = build_lecture_plan(subj, code, lid, course_title, lecture_title, raw_p1, raw_p2)
        verify_lecture_plan(plan, raw_p1, raw_p2)
        plans.append(plan)

        for sg in plan['segments']:
            total_segs += 1
            hkey = compute_tts_hash(sg['en_tts'], sg['vi_tts'])
            sg['tts_hash'] = hkey
            if hkey not in unique_tts_jobs:
                unique_tts_jobs[hkey] = (sg['en_tts'], sg['vi_tts'])
                ordered_hashes.append(hkey)

    cached_already = sum(
        1 for hk in unique_tts_jobs
        if os.path.exists(os.path.join(CACHE_DIR, f"{hk}.mp3")) and os.path.getsize(os.path.join(CACHE_DIR, f"{hk}.mp3")) > 1500
    )

    print("\n=====================================================================")
    print(f"VERIFICATION PASSED ON ALL {len(plans)} LECTURES (0 errors, 0 div imbalances)!")
    print(f"  Total granular segments across {len(plans)} lectures : {total_segs} (avg {total_segs/max(1,len(plans)):.1f}/lecture)")
    print(f"  Unique (en_tts, vi_tts) audio hashes            : {len(unique_tts_jobs)} ({total_segs - len(unique_tts_jobs)} reused via content-hash!)")
    print(f"  Already present in local hash cache             : {cached_already}/{len(unique_tts_jobs)}")
    print("=====================================================================\n", flush=True)

    if args.dry_run and not args.execute:
        for sample_plan in plans[:2] + [p for p in plans if p['subject'] == 'chemistry'][:1] + [p for p in plans if p['subject'] == 'physics'][:1]:
            print(f"--- SAMPLE LECTURE: {sample_plan['subject']}/{sample_plan['code']} ({sample_plan['lectureTitle']}) | segments={len(sample_plan['segments'])} | majorRanges={len(sample_plan['majorSections'])} ---")
            for sg in sample_plan['segments'][:5]:
                print(f"  [{sg['id']}] title={sg['title']}")
                print(f"     EN_TTS: {sg['en_tts'][:140]}...")
                print(f"     VI_TTS: {sg['vi_tts'][:140]}...")
        return

    # --- EXECUTE MODE (CONTINUOUS STREAMING TTS + PIPELINED LECTURE DEPLOYMENT) ---
    global _EN_SEM, _VI_SEM, _EN_PACING_LOCK, _VI_PACING_LOCK, _HTTP_SESSION
    _EN_SEM = asyncio.Semaphore(5)
    _VI_SEM = asyncio.Semaphore(6)
    _EN_PACING_LOCK = asyncio.Lock()
    _VI_PACING_LOCK = asyncio.Lock()

    progress = {'done': 0, 'total': len(ordered_hashes)}
    hash_durations = {}
    hash_events = {hk: asyncio.Event() for hk in ordered_hashes}
    hash_errors = {}

    job_queue = asyncio.Queue()
    for hk in ordered_hashes:
        job_queue.put_nowait(hk)

    async def tts_worker():
        while True:
            try:
                hk = job_queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            try:
                en_t, vi_t = unique_tts_jobs[hk]
                await synthesize_unique_hash(hk, en_t, vi_t, progress, hash_durations)
            except Exception as err:
                hash_errors[hk] = err
                raise
            finally:
                hash_events[hk].set()
                job_queue.task_done()

    async def deploy_pipeline():
        for idx_p, plan in enumerate(plans, 1):
            for sg in plan['segments']:
                hk = sg['tts_hash']
                await hash_events[hk].wait()
                if hk in hash_errors:
                    raise hash_errors[hk]
            skipped, n_boxes, tot_dur = await asyncio.to_thread(
                deploy_lecture_sync, plan, hash_durations, args.force_deploy
            )
            status_lbl = "SKIP-DEPLOYED" if skipped else "DEPLOYED"
            print(
                f"  [{status_lbl} {idx_p}/{len(plans)}] {plan['subject']}/{plan['code']}: "
                f"{n_boxes} boxes, {tot_dur:.1f}s total ({progress['done']}/{progress['total']} unique TTS)",
                flush=True
            )

    print(f"Starting continuous streaming TTS + pipelined deployment across {len(plans)} lectures...", flush=True)
    n_workers = max(4, args.concurrency)
    connector = aiohttp.TCPConnector(limit=16, keepalive_timeout=30)
    async with aiohttp.ClientSession(connector=connector) as session:
        _HTTP_SESSION = session
        workers = [asyncio.create_task(tts_worker()) for _ in range(n_workers)]
        deployer = asyncio.create_task(deploy_pipeline())
        await asyncio.gather(*workers, deployer)
        _HTTP_SESSION = None

    print("\nALL DONE! All Science audio files, manifests, and Supabase pages updated successfully!", flush=True)


if __name__ == '__main__':
    asyncio.run(async_main())
