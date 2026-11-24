# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Real Past Exam — May 2025 Int. Ver 2 Reading & Writing (54 Questions)
- Module 1: 27 Real Questions (32 minutes)
- Module 2: 27 Real Questions (32 minutes, mirrored to module2_hard & module2_lower with routingThreshold=0)
- Source: SAT May 2025 v2 (Int.) verbal — loaded dynamically at runtime from
  `scripts/ocr_data/may_v2_rw_raw.json` via `scripts.sat_rw_ocr_parser.build_rw_questions_from_ocr`,
  with surgical patches for 3 HTML data tables, 4 underlined spans, italics, bullet formatting,
  and visual-verified OCR typo cleanup.
- Independent 2-Pass Answer Audit completed across all 54 R&W items with rich Vietnamese explanations.
"""

import copy
import json
import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.sat_rw_ocr_parser import build_rw_questions_from_ocr

TEST_CODE = 'real_may2025_v2_rw'
FOLDER_KEY = 'real_rw'
ORDER_INDEX = 6
TEST_TITLE = '🏛️ Real Exam — May 2025 Int. Ver 2 Reading & Writing (54 Qs)'

RAW_JSON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'ocr_data',
    'may_v2_rw_raw.json',
)


def html_table(caption, headers, rows, footnote=''):
    """Builds a clean College Board-style data table for Bluebook split-pane rendering."""
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''.join(
        '<tr>' + ''.join(
            f'<td style="font-weight:700;">{c}</td>' if idx == 0 else f'<td>{c}</td>'
            for idx, c in enumerate(r)
        ) + '</tr>'
        for r in rows
    )
    fn_html = (
        f'<div style="font-family:\'Segoe UI\',system-ui,sans-serif;font-size:12px;'
        f'color:#475569;margin-top:4px;font-style:italic;">{footnote}</div>'
        if footnote else ''
    )
    return (
        f'<div style="margin-bottom:14px;">'
        f'<div style="font-family:\'Segoe UI\',system-ui,sans-serif;font-size:13.5px;'
        f'font-weight:800;color:#0f172a;text-align:center;margin-bottom:6px;">{caption}</div>'
        f'<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'
        f'{fn_html}</div>'
    )


def _meta(domain, skill, difficulty, answer, summary_vi, takeaway, analysis):
    """Builds a verified metadata + Vietnamese explanation entry for one SAT R&W item."""
    labels = ['A', 'B', 'C', 'D']
    assert answer in labels, f'Invalid answer {answer}'
    assert len(analysis) == 4, f'Expected 4 optionAnalysis entries, got {len(analysis)}'
    return {
        'domain': domain,
        'skill': skill,
        'difficulty': difficulty,
        'answer': answer,
        'explanation': {
            'summaryVi': summary_vi,
            'keyTakeaway': takeaway,
            'optionAnalysis': {
                labels[i]: {
                    'status': 'correct' if labels[i] == answer else 'trap',
                    'trapTag': analysis[i][0],
                    'reasonVi': analysis[i][1],
                }
                for i in range(4)
            },
        },
    }


def _clone_module_questions(questions, old_prefix, new_prefix):
    cloned = copy.deepcopy(questions)
    for q in cloned:
        q['id'] = q['id'].replace(old_prefix, new_prefix, 1)
    return cloned


# ============================================================================
# VISUAL-VERIFIED PATCHES (TABLES, UNDERLINES, ITALICS, OCR CLEANUP)
# ============================================================================

M1_PATCHES = {
    1: {
        'replace': [
            ('The Gleaners,', '<i>The Gleaners</i>,'),
            ('Jean-Francois Millet', 'Jean-François Millet'),
            ('realists’emphasis', 'realists’ emphasis'),
            ('subjects’beauty', 'subjects’ beauty'),
        ],
    },
    2: {
        'replace': [
            ('<p>Sal The minor', '<p>The minor'),
            ('1061 Paconia', '1061 Paeonia'),
            ('500, 000', '500,000'),
            ('(3x) Which choice', 'Which choice'),
        ],
    },
    3: {
        'replace': [
            ('<p>& The term', '<p>The term'),
        ],
    },
    4: {
        'replace': [
            ('<p>& In the decades', '<p>In the decades'),
        ],
    },
    5: {
        'replace': [
            ('surface, Although', 'surface. Although'),
            ('ammonia— both', 'ammonia—both'),
            (
                'Additionally, the shape and appearance of the crater did not suggest that it was formed by impact.',
                '<u>Additionally, the shape and appearance of the crater did not suggest that it was formed by impact.</u>',
            ),
        ],
    },
    6: {
        'replace': [
            ('<p>Text 1 In the past', '<p><strong>Text 1</strong></p>\n<p>In the past'),
            ('decades past. Text 2 Intoday’s', 'decades past.</p>\n<p><strong>Text 2</strong></p>\n<p>In today’s'),
            ('once were,', 'once were.'),
        ],
    },
    8: {
        'replace': [
            ('tank wall, Cuttlefish', 'tank wall. Cuttlefish'),
            ('Wardill’ steam’ s', 'Wardill’s team’s'),
            ('Wardill’ s', 'Wardill’s'),
        ],
    },
    9: {
        'replace': [
            ('Anthony Trollope” s 1855 novel The Warden.', 'Anthony Trollope’s 1855 novel <i>The Warden</i>.'),
            ('newspaper The Jupiter. It is true', 'newspaper <i>The Jupiter</i>.</p>\n<p>It is true'),
            ('read The Jupiter,', 'read <i>The Jupiter</i>,'),
            ('without The Jupiter life', 'without <i>The Jupiter</i> life'),
        ],
    },
    10: {
        'replace': [
            ('<p>[54] Life Among the Paiutes', '<p><i>Life Among the Paiutes</i>'),
            ('customs, writing</p>', 'customs, writing _______</p>'),
            ('(36) Which quotation from Life Among the Paiutes', 'Which quotation from <i>Life Among the Paiutes</i>'),
            ('“ During', '“During'),
            ('] ill after', '] till after'),
            ('“ Now', '“Now'),
            ('and hat is why', 'and that is why'),
            ('mother. *', 'mother.”'),
            ('“ But', '“But'),
            ('readers, an imagine', 'readers, can imagine'),
            ('were set in bloom', 'were yet in bloom'),
        ],
    },
    11: {
        'prependStimulusHtml': html_table(
            'Effect of Neighboring Species on Pollinator Visits to Target Species',
            ['Neighboring species', 'Target species', 'Effect value'],
            [
                ['leafy spurge', 'Lewis flax', '-0.3238'],
                ['Himalayan balsam', 'marsh woundwort', '0.7905'],
                ['Canadian wood betony', 'mayapple', '0.4729'],
            ],
        ),
        'replace': [
            (
                '<p>&] Effect of Neighboring Species on Pollinator Visits to Target Species '
                'Himalayan balsam 0.7905 Canadian wood ‘mayapple 0.4729 betony</p>\n',
                '',
            ),
            ('one plantas a', 'one plant as a'),
            ('nearby plantasa', 'nearby plant as a'),
            ('effect value of</p>', 'effect value of _______</p>'),
            ('(3x¢) Which choice', 'Which choice'),
        ],
    },
    12: {
        'prependStimulusHtml': html_table(
            'Impact of Four Key Industries on Oklahoma Economy in 2017',
            [
                'Industry',
                'Approximate total contribution by industry',
                'Number of people employed by industry',
                'Average contribution per employee by industry',
            ],
            [
                ['Accommodation/food services', '$5,242,100,000', '150,373', '$34,861'],
                ['Tribal economic activity', '$7,312,400,000', '51,674', '$141,510'],
                ['Health care', '$13,727,300,000', '193,514', '$70,937'],
                ['Retail', '$10,738,800,000', '179,208', '$59,924'],
            ],
        ),
        'replace': [
            (
                '<p>& Impact of Four Key Industries on Oklahoma Economy in 2017 | Number of Average '
                'Approximate total ha. oo people contribution per Industry contribution by loved b 1 b '
                'employe employee industry. ployed by | ployee by industry industry Accommodation/. '
                '$5,242,100,000 150,373 $34,861 food services “Tribal economic $7,312,400,000 51,674 '
                '$141,510 activity Health care $13,727,300,000 193,514 $70,937 $10,738,800,000 179,208 '
                '$59,924 The nearly',
                '<p>The nearly',
            ),
            ('tribes’collective', 'tribes’ collective'),
            ('itabove', 'it above'),
            ('accommodation/ food', 'accommodation/food'),
            (
                'nealth care, retail, and accommodation; food services.',
                'health care, retail, and accommodation/food services.',
            ),
        ],
    },
    13: {
        'replace': [
            ('removes. epicuticular', 'removes epicuticular'),
            ('canopies’capacity', 'canopies’ capacity'),
            (
                "(3%q) ‘Which detail, if true, would most directly support the team's",
                'Which detail, if true, would most directly support the team’s',
            ),
            ('the pplication of', 'the application of'),
            ('treatments -ather than', 'treatments rather than'),
        ],
    },
    14: {
        'replace': [
            ('<p>&</p>\n', ''),
            ('Pedro Simdes Coelho', 'Pedro Simões Coelho'),
            ('music- streaming', 'music-streaming'),
            ('users’intentions', 'users’ intentions'),
            ('such as</p>\n<p>“Using', 'such as “Using'),
            (') Which choice', 'Which choice'),
            ('t may be advantageous', 'it may be advantageous'),
            ('the 2xtent to which', 'the extent to which'),
            ('pleasant to Ise.', 'pleasant to use.'),
            ('“ Using paid music streaming services is pleasant 7', '“Using paid music streaming services is pleasant”'),
            (
                'he statement * Using paid music streaming services is pleasant ” is not a “eliable',
                'the statement “Using paid music streaming services is pleasant” is not a reliable',
            ),
            ("1sers' intentions", 'users’ intentions'),
            ('probably anaffected', 'probably unaffected'),
        ],
    },
    15: {
        'replace': [
            ('<p>& On August 15, 2013, the Navajo Times', '<p>On August 15, 2013, the <i>Navajo Times</i>'),
            ('(Kin Hozhoni)', '(<i>Kín Hózhóní</i>)'),
            ('(Naabeeho Bindhdsdzo)', '(<i>Naabeehó Bináhásdzo</i>)'),
            ('Exploring the Navajo Nation Chapter by Chapter.', '<i>Exploring the Navajo Nation Chapter by Chapter</i>.'),
            ('BB 0 vark for Review Which choice', 'Which choice'),
        ],
    },
    16: {
        'replace': [
            ('Thel2th', 'The 12th'),
        ],
    },
    17: {
        'replace': [
            ('as a child,</p>', 'as a child.</p>'),
            ('‘Which choice', 'Which choice'),
            ('artist’ s over 160 year’ s', 'artist’s over 160 year’s'),
            ('artists” over 160 years', 'artists’ over 160 years'),
        ],
    },
    18: {
        'replace': [
            (
                '<p>55} The editors of Home Ground: A Guide to the American Landscape',
                '<p>The editors of <i>Home Ground: A Guide to the American Landscape</i>',
            ),
            ('Of Landscape and Longing.', '<i>Of Landscape and Longing</i>.'),
        ],
    },
    19: {
        'replace': [
            ('<p>& A groundbreaking', '<p>A groundbreaking'),
            ('occured', 'occurred'),
        ],
    },
    20: {
        'replace': [
            ('<p>5} The small', '<p>The small'),
            ('astronomer’ s', 'astronomer’s'),
            ('object’ s', 'object’s'),
        ],
    },
    21: {
        'replace': [
            ('De gente populi Romani,', '<i>De gente populi Romani</i>,'),
            ('Rerum rusticarum libra tres,', '<i>Rerum rusticarum libra tres</i>,'),
            ('BY [1 ark for Review ‘Which choice', 'Which choice'),
        ],
    },
    22: {
        'replace': [
            ('Tikal” s', 'Tikal’s'),
            ('LIDAR" s', 'LiDAR’s'),
        ],
    },
    24: {
        'replace': [
            ('Karman line', 'Kármán line'),
            ('Theodore von Karmén', 'Theodore von Kármán'),
        ],
    },
    25: {
        'replace': [
            ('following notes: The Schomburg Center', 'following notes:</p>\n<ul><li>The Schomburg Center'),
            ('New York City. “Tt was named', 'New York City.</li><li>It was named'),
            ('Schomburg. “It was founded in 1925.</p>', 'Schomburg.</li><li>It was founded in 1925.</li></ul>'),
            ('‘Which choice', 'Which choice'),
        ],
    },
    26: {
        'replace': [
            ('<p>‘While researching', '<p>While researching'),
            ('following notes: Brussels sprouts', 'following notes:</p>\n<ul><li>Brussels sprouts'),
            ('humans. -Apples', 'humans.</li><li>Apples'),
            ('acid. “There is 80', 'acid.</li><li>There is 80'),
            (
                'sprouts. “There is 6 mg of ascorbic acid in every 100g of apple.',
                'sprouts.</li><li>There is 6 mg of ascorbic acid in every 100 g of apple.',
            ),
            ('apple. “Humans', 'apple.</li><li>Humans'),
            (
                'vegetables. “Ascorbic acid is also known as vitamin C.</p>',
                'vegetables.</li><li>Ascorbic acid is also known as vitamin C.</li></ul>',
            ),
            ('BA 0 ark for Review The student', 'The student'),
            ('acid) —80 mg in every100g', 'acid)—80 mg in every 100 g'),
        ],
    },
    27: {
        'replace': [
            ('<p>[2a] While researching', '<p>While researching'),
            ('following notes: “Merle Oberon (1911-1979)', 'following notes:</p>\n<ul><li>Merle Oberon (1911–1979)'),
            ('India. “She was of', 'India.</li><li>She was of'),
            ('heritage. “She was the first', 'heritage.</li><li>She was the first'),
            ('Award. “Early in her career', 'Award.</li><li>Early in her career'),
            ('The Three Passions (1928). “Later, she played', '<i>The Three Passions</i> (1928).</li><li>Later, she played'),
            ('Empress Josephine in Désirée (1954).</p>', 'Empress Josephine in <i>Désirée</i> (1954).</li></ul>'),
            ('(580) The student', 'The student'),
            ('The Three Passions and Désirée', '<i>The Three Passions</i> and <i>Désirée</i>'),
            ('the irst Indian-born', 'the first Indian-born'),
            ('The Three Passions (1928)', '<i>The Three Passions</i> (1928)'),
            ('Oberon’ s:areer', 'Oberon’s career'),
            ('whereas Désirée (1954)', 'whereas <i>Désirée</i> (1954)'),
            ('nameless, ancredited role', 'nameless, uncredited role'),
            ('in Désirée (1954)', 'in <i>Désirée</i> (1954)'),
            ('Farly in her career', 'Early in her career'),
            ('wasn’ t listed', 'wasn’t listed'),
            ('such as he credits', 'such as the credits'),
            ('film The Three Passions,', 'film <i>The Three Passions</i>,'),
        ],
    },
}

M2_PATCHES = {
    2: {
        'replace': [
            ('_______byarich', '_______ by a rich'),
            ('Kanaka Maoli,', '<i>Kanaka Maoli</i>,'),
        ],
    },
    3: {
        'replace': [
            ('<p>& Archaeologists', '<p>Archaeologists'),
            ('Tritia gibbosula', '<i>Tritia gibbosula</i>'),
            ('etal.', 'et al.'),
            ('artifacts’_______', 'artifacts’ _______'),
            ('T. gibbosula', '<i>T. gibbosula</i>'),
        ],
    },
    4: {
        'replace': [
            ('Svante Paibo', 'Svante Pääbo'),
            ('colleagues’2017', 'colleagues’ 2017'),
            ('genus Chasechloa', 'genus <i>Chasechloa</i>'),
            ('historical DNA — genomic', 'historical DNA—genomic'),
            ('are house d in', 'are housed in'),
            (
                'collections — thus capitalizing on the research potential offered by a vast but '
                'hitherto relatively underutilized source of insight into the biological past.',
                'collections—<u>thus capitalizing on the research potential offered by a vast but '
                'hitherto relatively underutilized source of insight into the biological past.</u>',
            ),
        ],
    },
    5: {
        'replace': [
            ('Murillo- Barroso', 'Murillo-Barroso'),
            ('This relative scarcity', '<u>This relative scarcity</u>'),
        ],
    },
    6: {
        'replace': [
            ('In a Flight of Starlings,', '<i>In a Flight of Starlings</i>,'),
            ('J Mack for Review Which choice', 'Which choice'),
            ('Kean’ s', 'Kean’s'),
            ('Parisi’ s', 'Parisi’s'),
        ],
    },
    7: {
        'replace': [
            ('<p>& The following', '<p>The following'),
            ('The Winter” s Tale.', '<i>The Winter’s Tale</i>.'),
            ('return to Sicily. POLIXENES:', 'return to Sicily.</p>\n<p>POLIXENES:'),
            ('Tis a sickness', '’Tis a sickness'),
            ('to grant this. CAMILLO:', 'to grant this.</p>\n<p>CAMILLO:'),
            ('abroad, 1 desire', 'abroad, I desire'),
            (
                'to whose feeling sorrows I might be some allay— or [ 0’_erween [presume] to think so— which',
                '<u>to whose feeling sorrows I might be some allay—or I o’erween [presume] to think so</u>—which',
            ),
            ('Camillo” s', 'Camillo’s'),
            ('Camillo’ s', 'Camillo’s'),
            ('Sicily’ s', 'Sicily’s'),
            ('is’ t departing', 'isn’t departing'),
        ],
    },
    8: {
        'replace': [
            ('To- Day', 'To-Day'),
            (
                'disrepair. How long ago, by summer breezes fanned, Here stood the newborn Venus, '
                'fresh and fair; All palpitating from the master’s hand, The last touch of his chisel '
                'lingering there.</p>\n<p>“And surely this shall last!” he proudly thought;</p>\n'
                '<p>“Fixed in immortal marble is my fame!” Just here, where human hand has surely '
                'wrought, Some crumbling letters may have spelled his name.</p>',
                'disrepair.</p>\n<p>How long ago, by summer breezes fanned,<br/>'
                'Here stood the newborn Venus, fresh and fair;<br/>'
                'All palpitating from the master’s hand,<br/>'
                'The last touch of his chisel lingering there.</p>\n'
                '<p>“And surely this shall last!” he proudly thought;<br/>'
                '“Fixed in immortal marble is my fame!”<br/>'
                'Just here, where human hand has surely wrought,<br/>'
                'Some crumbling letters may have spelled his name.</p>',
            ),
        ],
    },
    9: {
        'prependStimulusHtml': html_table(
            'Ranking of Environmental and Sociocultural Benefits of Urban Agriculture (scale of 1 to 25; 1 = highest)',
            ['Social or ecological service', 'Project leaders', 'Stakeholders', 'General public'],
            [
                ['provision of medicinal plants', '22', '21', '5'],
                ['enhancement of pollination', '1', '7', '12'],
                ['enhancement of carbon sequestration', '17', '22', '21'],
                ['preservation of cultural knowledge and heritage', '8', '15', '13'],
                ['prevention of soil erosion', '13', '11', '23'],
            ],
        ),
        'replace': [
            (
                '<p>‘Ranking of Environmental and Sociocultural Benefits of Urban Agriculture '
                '(scale of 1 to 25; 1= highest) E———</p>\n'
                '<p>Social or ecological service leaders rs public</p>\n'
                '<p>eT NT ETN ICR</p>\n'
                '<p>preservation of cultural knowledge and I IE NE EN Esther',
                '<p>Esther',
            ),
            ('Italy — leaders', 'Italy—leaders'),
            ('general public — to', 'general public—to'),
            ('planner” s', 'planner’s'),
            ('public han it was', 'public than it was'),
        ],
    },
    10: {
        'replace': [
            ('variants of IGF,', 'variants of <i>IGF1</i>,'),
            ('IGFI', '<i>IGF1</i>'),
            ('related to IGF affects', 'related to <i>IGF1</i> affects'),
            ('(Canis rufus)', '(<i>Canis rufus</i>)'),
            ('(Canis lupus campestris)', '(<i>Canis lupus campestris</i>)'),
        ],
    },
    11: {
        'replace': [
            ('database of ‘materials', 'database of materials'),
            ('provided ‘more specificity', 'provided more specificity'),
            ('Bl J vark for Review Which finding', 'Which finding'),
            ('team’ s', 'team’s'),
        ],
    },
    12: {
        'replace': [
            ('<p>Joi) Soil thawing', '<p>Soil thawing'),
            ('(CO:)', '(CO<sub>2</sub>)'),
            ('artic bramble (Rubus arcticus)', 'arctic bramble (<i>Rubus arcticus</i>)'),
            ('CO.output', 'CO<sub>2</sub> output'),
            ('(CO: generated', '(CO<sub>2</sub> generated'),
            ('inputs— years', 'inputs—years'),
            ('among them — to', 'among them—to'),
            ('the CO: balance', 'the CO<sub>2</sub> balance'),
            ('net CO: is', 'net CO<sub>2</sub> is'),
            ('seterotrophic respiration', 'heterotrophic respiration'),
            ('snow “over than', 'snow cover than'),
            ('available for he growth', 'available for the growth'),
            ('R. arcticus', '<i>R. arcticus</i>'),
            ('rate of aeterotrophic', 'rate of heterotrophic'),
            ('seasonal snow cover tends', 'Seasonal snow cover tends'),
            ('areas of -elatively', 'areas of relatively'),
            ('respiration o continue', 'respiration to continue'),
            ('are ypically not growing.', 'are typically not growing.'),
        ],
    },
    13: {
        'replace': [
            ('<p>& Over 600', '<p>Over 600'),
            ('New York Gity', 'New York City'),
            ('English — one', 'English—one'),
            ('City” s', 'City’s'),
        ],
    },
    14: {
        'replace': [
            ('Black Swan Green', '<i>Black Swan Green</i>'),
            ('Mitchell” s', 'Mitchell’s'),
            ('own life — there', 'own life—there'),
            ('of Mitchell — and', 'of Mitchell—and'),
            ('may conclude that</p>', 'may conclude that _______</p>'),
        ],
    },
    15: {
        'replace': [
            ('<p>[24] Since the nineteenth', '<p>Since the nineteenth'),
            ('(2700-2200', '(2700–2200'),
            ('(2050-1800', '(2050–1800'),
            ('(1550-1100', '(1550–1100'),
        ],
    },
    17: {
        'replace': [
            ('<p>I=) B The allocation', '<p>The allocation'),
            ('‘was', 'was'),
        ],
    },
    18: {
        'replace': [
            ('factors — namely', 'factors—namely'),
            ('meteoroids — their', 'meteoroids—their'),
        ],
    },
    19: {
        'replace': [
            ('Hafez’s Divan,', 'Hafez’s <i>Dīvān</i>,'),
        ],
    },
    20: {
        'replace': [
            ('<p>5 B In 2018,', '<p>In 2018,'),
            ('Maria Svarbova', 'Mária Svarbová'),
            ('Maria Svarbovd', 'Mária Svarbová'),
        ],
    },
    22: {
        'replace': [
            ('<p>[54] French mathematician', '<p>French mathematician'),
        ],
    },
    25: {
        'replace': [
            ('<p>= BE In the Southeast', '<p>In the Southeast'),
            ('53. 3%', '53.3%'),
            ('56. 6%', '56.6%'),
            ('2. 8 percentage', '2.8 percentage'),
        ],
    },
    26: {
        'replace': [
            ('<p>‘While researching', '<p>While researching'),
            ('following notes: ‘Linguistic typologists', 'following notes:</p>\n<ul><li>Linguistic typologists'),
            ('features. -One such structure', 'features.</li><li>One such structure'),
            ('objects (0)', 'objects (O)'),
            (
                'sentence. “English employs an SVO word order (e. g., Cows eat grass). '
                '+Bengali employs an SOV word order (e. g., Cows grass eat). '
                '“Filipino employs a VSO word order (e. g., Eat cows grass). '
                '-879% of the world’s languages are classified as either SVO or SOV.</p>',
                'sentence.</li><li>English employs an SVO word order (e.g., <i>Cows eat grass</i>).</li>'
                '<li>Bengali employs an SOV word order (e.g., <i>Cows grass eat</i>).</li>'
                '<li>Filipino employs a VSO word order (e.g., <i>Eat cows grass</i>).</li>'
                '<li>87% of the world’s languages are classified as either SVO or SOV.</li></ul>',
            ),
            ('Bl C0 vor for Review The student', 'The student'),
            ('world” s', 'world’s'),
        ],
    },
    27: {
        'replace': [
            ('following notes: “Producing', 'following notes:</p>\n<ul><li>Producing'),
            ('L. maxima', '<i>L. maxima</i>'),
            ('DNA. -Yirlis Yadeth Pineda-Rodriguez', 'DNA.</li><li>Yirlis Yadeth Pineda-Rodriguez'),
            ('University of Cordoba', 'University of Córdoba'),
            (
                'kits. -CTAB 2X (kit 1) had a DNA yield of 2, 134 nanograms per microliter (ng/uL) '
                'and a purity ratio of 2. 2. “Pbact (kit 2) had a DNA yield of 157 ng/uL and a purity '
                'ratio of 1.6. Pplant (kit 3) had a DNA yield of 12. 5 ng/uL and a purity ratio of 1.5. '
                '-According to the researchers, Phact',
                'kits.</li><li>CTAB 2X (kit 1) had a DNA yield of 2,134 nanograms per microliter (ng/µL) '
                'and a purity ratio of 2.2.</li><li>Pbact (kit 2) had a DNA yield of 157 ng/µL and a '
                'purity ratio of 1.6.</li><li>Pplant (kit 3) had a DNA yield of 12.5 ng/µL and a purity '
                'ratio of 1.5.</li><li>According to the researchers, Pbact',
            ),
            ('ideal of 1.8.</p>', 'ideal of 1.8.</li></ul>'),
            ('two of the kits Which choice', 'two of the kits. Which choice'),
            ('2,134 ng/ut, both Phact', '2,134 ng/µL, both Pbact'),
        ],
    },
}


# ============================================================================
# MODULE 1 METADATA & 2-PASS AUDITED VIETNAMESE EXPLANATIONS (27 QUESTIONS)
# ============================================================================

M1_META = {
    1: _meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'B',
        'Đoạn văn đối lập phong cách hiện thực (“accurately portraying” — khắc họa chân thực người lao động bình thường) với phong cách lãng mạn của Paul Delaroche (“instead _______ their subjects’ beauty or heroism while hiding all imperfection” — giấu mọi khuyết điểm để tô hồng vẻ đẹp hay khí phách anh hùng). Từ cần điền mang nghĩa “phóng đại, thổi phồng” → Chọn B (“exaggerate”).',
        'Khi thấy cấu trúc tương phản “rejection of ... which instead” cùng vế song hành “while hiding all imperfection”, hãy tìm động từ đối nghĩa với “accurately portraying”.',
        [
            ('Opposite Tone', 'mock = chế giễu — trái ngược với việc che giấu khuyết điểm để tôn vinh vẻ đẹp/anh hùng.'),
            ('Đáp án đúng', 'exaggerate = phóng đại, tô hồng — khớp hoàn hảo với việc giấu mọi khuyết điểm và trái ngược với lối vẽ chân thực.'),
            ('Wrong Context', 'correct = sửa chữa — không đi tự nhiên với “beauty or heroism” trong bối cảnh đối lập chủ nghĩa hiện thực.'),
            ('Opposite Tone', 'undermine = làm suy yếu — mang sắc thái hạ thấp, trái ngược ý lý tưởng hóa nhân vật.'),
        ],
    ),
    2: _meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'C',
        'Liên từ tương phản “while” đặt hai thời điểm đối lập nhau: hiện nay có hơn 500.000 tiểu hành tinh nên việc đặt tên riêng đã trở nên “nearly impossible” (gần như bất khả thi); ngược lại, khi xưa mới phát hiện ít thì việc này từng **khả thi / làm được** → Chọn C (“feasible”).',
        'Với cấu trúc “while X was ___ when..., [now] X has become nearly impossible”, đáp án phải là từ trái nghĩa trực tiếp với “nearly impossible”.',
        [
            ('Wrong Meaning', 'substantial = đáng kể, lớn — không tạo tương phản trực tiếp với “nearly impossible”.'),
            ('Opposite Meaning', 'insurmountable = không thể vượt qua — đồng nghĩa thay vì trái nghĩa với “nearly impossible”.'),
            ('Đáp án đúng', 'feasible = khả thi, có thể thực hiện được — tạo cặp tương phản chuẩn xác với “nearly impossible”.'),
            ('Wrong Meaning', 'ambiguous = mơ hồ — không liên quan đến mức độ khó/dễ của việc đặt tên.'),
        ],
    ),
    3: _meta(
        'Craft and Structure', 'Words in Context', 'Medium', 'C',
        'Câu ví dụ giải thích ngay sau đó: “firms that locate near one another” (các doanh nghiệp đóng gần nhau), đồng thời thuật ngữ “agglomeration economies” (kinh tế tích tụ) chỉ lợi ích của các công ty cùng ngành **tập trung** tại một khu vực → Chọn C (“concentrate”).',
        'Câu mở đầu bằng “For example” trong dạng Words in Context luôn chứa manh mối định nghĩa trực tiếp cho chỗ trống ngay trước nó (“locate near one another” = “concentrate”).',
        [
            ('Wrong Context', 'recur = tái diễn theo thời gian — chỉ tần suất thời gian, không diễn tả việc tập trung về địa lý.'),
            ('Opposite Meaning', 'dissipate = phân tán, tiêu tan — trái nghĩa hoàn toàn với “locate near one another”.'),
            ('Đáp án đúng', 'concentrate = tập trung, quy tụ tại một khu vực — khớp chính xác với “agglomeration” và “locate near one another”.'),
            ('Wrong Meaning', 'terminate = chấm dứt — sai nghĩa hoàn toàn.'),
        ],
    ),
    4: _meta(
        'Craft and Structure', 'Words in Context', 'Medium', 'B',
        'Sau khi Mexico giành độc lập, văn học trở thành phương tiện giúp quốc gia mới **hiện thực hóa / định hình trọn vẹn** bản sắc tự chủ của mình, thể hiện qua cụm bổ trợ “helping to shape what would become a distinctly Mexican literary tradition” → Chọn B (“realized” = biến thành hiện thực, đạt được).',
        'Trên SAT, động từ “realize” rất hay được dùng theo nghĩa học thuật “make real / achieve / bring into being” (hiện thực hóa), chứ không chỉ nghĩa “nhận ra”.',
        [
            ('Opposite Tone', 'overcame = vượt qua (một trở ngại) — Mexico đang xây dựng chứ không vượt qua bản sắc tự chủ của chính mình.'),
            ('Đáp án đúng', 'realized = hiện thực hóa, thành hình — khớp logic với “helping to shape” một truyền thống văn học đậm chất Mexico.'),
            ('Opposite Tone', 'decried = kịch liệt chỉ trích — mang nghĩa tiêu cực, trái hoàn toàn giọng điệu đoạn văn.'),
            ('Opposite Tone', 'evaded = né tránh — trái ngược ý định hình bản sắc dân tộc.'),
        ],
    ),
    5: _meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Medium', 'B',
        'Câu gạch chân “Additionally, the shape and appearance of the crater did not suggest that it was formed by impact” bổ sung bằng chứng thứ hai cho thấy nhóm của Dale Cruikshank đã loại trừ giả thuyết miệng hố hình thành do va chạm thiên thạch dựa trên hình dạng và diện mạo quan sát được, từ đó củng cố giả thuyết núi lửa băng → Chọn B.',
        'Với câu hỏi chức năng câu gạch chân bắt đầu bằng “Additionally,... did not suggest that [X]”, hãy xác định giả thuyết thay thế nào đang bị loại bỏ để nâng đỡ kết luận ở câu cuối.',
        [
            ('Off-Topic Detail', 'Câu gạch chân không hề nhắc đến các phát hiện trước đây hay phương pháp nghiên cứu nào.'),
            ('Đáp án đúng', 'Loại trừ lời giải thích thay thế (“formed by impact”) dựa trên bằng chứng sẵn có (“shape and appearance”).'),
            ('Wrong Focus', 'New Horizons chỉ được nhắc ở câu đầu; câu gạch chân tập trung vào hình dạng miệng hố chứ không nhấn mạnh vai trò con tàu.'),
            ('Unsupported Claim', 'Đoạn văn không nói bản thân nhóm nghiên cứu từng có hiểu lầm về miệng hố.'),
        ],
    ),
    6: _meta(
        'Craft and Structure', 'Cross-Text Connections', 'Easy', 'C',
        'Text 1 khẳng định: “many of today’s artists are making albums that are much longer than albums from decades past.” Text 2 cũng nêu: “many new albums are longer and have more songs than albums crafted for physical formats.” Điểm đồng thuận trực tiếp của cả hai tác giả là nhiều album mới dài hơn trước đây → Chọn C.',
        'Trong câu Cross-Text tìm điểm chung, hãy đối chiếu mệnh đề xuất hiện tường minh ở cả hai văn bản và bỏ qua các chi tiết đánh giá riêng (như “lack of focus” chỉ có ở Text 2).',
        [
            ('Not Mentioned', 'Không văn bản nào đề cập đến bìa/hình ảnh minh họa (“artwork”) của album.'),
            ('Not Mentioned', 'Doanh số bán đĩa (“sell more copies”) không xuất hiện ở cả Text 1 lẫn Text 2.'),
            ('Đáp án đúng', 'Cả hai văn bản đều khẳng định rõ nhiều album mới hiện nay dài hơn album trước kia do không còn giới hạn định dạng vật lý.'),
            ('Not Mentioned', 'Độ lớn âm thanh (“quieter”) hoàn toàn không được nhắc đến.'),
        ],
    ),
    7: _meta(
        'Information and Ideas', 'Central Ideas and Details', 'Easy', 'D',
        'Đoạn văn kể lâu nay người ta cho rằng Francis Bellamy là tác giả gốc viết lời Tuyên thệ Trung thành vào tháng 8/1892, nhưng một bài báo xuất bản vài tháng trước đó đã ghi lại cảnh học sinh đọc đúng lời tuyên thệ này (“Bellamy may not have created the pledge after all”). Do đó thông tin trở nên không chắc chắn là **danh tính người đầu tiên viết lời tuyên thệ** → Chọn D.',
        'Đọc kỹ câu kết luận bắt đầu bằng “This means that...” — nó tóm gọn trực tiếp câu trả lời cho câu hỏi chi tiết.',
        [
            ('Not Mentioned', 'Đoạn văn không đề cập đến số lần chỉnh sửa lời tuyên thệ trong thế kỷ 20.'),
            ('Not Mentioned', 'Không có thông tin nào về phần lời tuyên thệ mà học sinh yêu thích nhất.'),
            ('Misread Detail', 'Tên tờ báo đăng bài không phải điều bị đặt nghi vấn; điều chưa chắc chắn là tác giả thực sự.'),
            ('Đáp án đúng', 'Khớp trực tiếp với kết luận “Bellamy may not have created the pledge after all”.'),
        ],
    ),
    8: _meta(
        'Information and Ideas', 'Central Ideas and Details', 'Easy', 'D',
        'Toàn bài giới thiệu rằng cừu và khỉ macaque có thị giác 3D, còn bạch tuộc/mực ống thì không; nhóm của Trevor Wardill kiểm chứng giả định tương tự về mực nang bằng kính 3D và phát hiện mực nang điều chỉnh vị trí tấn công theo ảnh 3D — gợi ý mực nang có thể cũng có thị giác 3D giống cừu và khỉ macaque → Chọn D.',
        'Ý chính (Main Idea) phải bao quát cả đối tượng nghiên cứu (nhóm Wardill & mực nang) lẫn kết luận cốt lõi ở câu cuối, không chọn chi tiết quy trình nhỏ lẻ.',
        [
            ('Unsupported Comparison', 'Đoạn văn không so sánh độ phức tạp của mắt mực nang với mắt cừu hay khỉ macaque.'),
            ('Contradicts Text', 'Câu đầu khẳng định rõ cả cừu lẫn khỉ macaque đều có thị giác 3D, và đây là kiến thức có sẵn chứ không phải kết quả trước đó của nhóm Wardill.'),
            ('Too Narrow', 'Chi tiết đeo kính 3D chỉ là phương pháp thí nghiệm, không nêu được kết luận chính của nghiên cứu.'),
            ('Đáp án đúng', 'Tóm gọn đầy đủ phát hiện trọng tâm của nghiên cứu nhóm Wardill về khả năng nhìn 3D của mực nang.'),
        ],
    ),
    9: _meta(
        'Information and Ideas', 'Central Ideas and Details', 'Medium', 'B',
        'Đoạn trích mô tả dù dân các tỉnh xa không nhắc tên Tom Towers hằng ngày nhưng họ coi tờ *The Jupiter* là không thể thiếu, và “This kind of hidden but still conscious glory suited the nature of the man” — ông thích ngồi im lặng một góc câu lạc bộ nghe các chính trị gia huyên thuyên và tự đắc rằng mình có quyền lực hạ gục họ chỉ bằng ngòi bút. Điều này cho thấy ông **hài lòng một cách kín đáo với khả năng tác động đến dư luận của mình** → Chọn B.',
        'Trong trích đoạn văn học thế kỷ 19, hãy chú ý các cụm khóa bộc lộ tâm lý nhân vật như “hidden but still conscious glory” và “loved to sit silent... think how they all were in his power”.',
        [
            ('Contradicts Text', 'Đoạn văn nói người ta “did not talk daily of Tom Towers” và vinh quang của ông là “hidden”, nên không thể nói ông nhận được nhiều lời ca tụng trực tiếp.'),
            ('Đáp án đúng', '“private satisfaction” khớp với “hidden... glory / loved to sit silent”, còn “capacity to influence public opinion” khớp với quyền lực qua tờ báo *The Jupiter*.'),
            ('Misread Detail', 'Các tỉnh xa chỉ là ví dụ cho tầm ảnh hưởng âm thầm, không phải mục tiêu chính ông theo đuổi.'),
            ('Unsupported Claim', 'Độc giả đọc tờ báo chứ không bàn tán về ông; đoạn văn không nói ông ảo tưởng độc giả quan tâm đến mình hơn chính trị gia.'),
        ],
    ),
    10: _meta(
        'Information and Ideas', 'Command of Evidence (Textual)', 'Easy', 'B',
        'Yêu cầu đề bài gồm **2 điều kiện bắt buộc**: (1) trò chuyện trực tiếp với độc giả (“directly addresses the reader”) và (2) giải thích một phong tục (“explain certain customs”). Chỉ câu B vừa gọi trực tiếp “Now, my dear reader,” vừa giải thích phong tục gọi người tốt là cha hoặc mẹ (“that is why [my people] call all good people father or mother”) → Chọn B.',
        'Luôn tách nhận định cần chứng minh thành từng tiêu chí nhỏ (A + B) và loại bỏ ngay các phương án chỉ đáp ứng 1 trong 2 tiêu chí (như C chỉ gọi độc giả, D chỉ giải thích phong tục).',
        [
            ('Missing Both Criteria', 'Chỉ kể sự kiện gia đình có bé gái ra đời; không gọi độc giả và không giải thích phong tục.'),
            ('Đáp án đúng', 'Đáp ứng trọn vẹn cả 2 vế: gọi trực tiếp “my dear reader” và giải thích nguồn gốc phong tục xưng hô của người Paiute.'),
            ('Half-Right Trap', 'Có gọi trực tiếp “dear readers” nhưng không giải thích bất kỳ phong tục nào.'),
            ('Half-Right Trap', 'Có giải thích phong tục đặt tên con gái theo loài hoa nhưng không trực tiếp trò chuyện với độc giả.'),
        ],
    ),
    11: _meta(
        'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy', 'A',
        'Đối chiếu trực tiếp trong bảng ở hàng thứ hai: Neighboring species = **Himalayan balsam** → Target species = marsh woundwort → **Effect value = 0.7905** → Chọn A.',
        'Với câu hỏi tra cứu số liệu trực tiếp, luôn dò đúng tên hàng (“Himalayan balsam”) và tên cột (“Effect value”) để tránh đọc nhầm sang loài kế bên.',
        [
            ('Đáp án đúng', '0.7905 là đúng giá trị Effect value ở hàng Himalayan balsam trong bảng.'),
            ('Wrong Row', '-0.3238 là Effect value của hàng “leafy spurge”, không phải Himalayan balsam.'),
            ('Not in Table', '-3.2570 không xuất hiện trong bảng (số nhiễu đảo chữ số từ -0.3238).'),
            ('Wrong Row', '0.4729 là Effect value của hàng “Canadian wood betony”.'),
        ],
    ),
    12: _meta(
        'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy', 'B',
        'Xét cột **Approximate total contribution by industry** (tổng đóng góp vào nền kinh tế Oklahoma năm 2017): Health care ($13,727,300,000) > Retail ($10,738,800,000) > Tribal economic activity ($7,312,400,000) > Accommodation/food services ($5,242,100,000). Vậy Tribal economic activity xếp **trên accommodation/food services nhưng dưới cả health care và retail** → Chọn B.',
        'Cẩn thận bẫy đọc nhầm cột: đề so sánh tổng đóng góp (“totaled over $7.3 billion”) ở cột 2, không phải đóng góp bình quân trên mỗi lao động ở cột 4 (nơi Tribal economic activity đứng đầu $141,510).',
        [
            ('Misread Data', 'Sai: Tribal economic activity ($7.31B) thấp hơn Retail ($10.74B), không cao hơn.'),
            ('Đáp án đúng', 'Chính xác: $7.31B cao hơn Accommodation/food services ($5.24B) và thấp hơn cả Health care ($13.73B) lẫn Retail ($10.74B).'),
            ('Wrong Column Trap', 'Đây là thứ hạng của cột “Average contribution per employee” ($141,510 cao nhất), không phải cột tổng đóng góp.'),
            ('Misread Data', 'Sai: $7.31B thấp hơn rất xa chứ không hề “nearly equal” so với $10.74B và $13.73B.'),
        ],
    ),
    13: _meta(
        'Information and Ideas', 'Command of Evidence (Textual)', 'Medium', 'A',
        'Nhóm Miyazaki phát hiện phương pháp rửa nước (7,6%) và sóng siêu âm (38,4%) thu hồi được ít vi nhựa hơn hẳn dung dịch kiềm làm tan lớp sáp biểu bì lá (53,8%), từ đó kết luận các đánh giá trước đây đã **đánh giá thấp** khả năng giữ vi nhựa của tán rừng. Để kết luận này đứng vững, cần cầu nối logic rằng **phần lớn nghiên cứu trước kia sử dụng phương pháp chiết xuất không tác động đáng kể đến lớp sáp biểu bì** (nên bỏ sót lượng vi nhựa bám trong lớp sáp) → Chọn A.',
        'Trong dạng Strengthen/Support, hãy tìm giả định ngầm nối thí nghiệm hiện tại (“alkaline removes epicuticular wax → 53.8%”) với nhận định về “previous assessments”.',
        [
            ('Đáp án đúng', 'Nếu các nghiên cứu trước không xử lý lớp sáp biểu bì, họ sẽ bỏ sót lượng lớn vi nhựa bám vào sáp và do đó đánh giá thấp sức chứa của tán rừng.'),
            ('Irrelevant Detail', 'Việc các nghiên cứu trước khảo sát nhiều loài cây có lượng sáp khác nhau không chứng minh họ đã đánh giá thấp.'),
            ('Weakens Conclusion', 'Nếu các nghiên cứu trước đã tìm thấy nồng độ vượt xa 53,8% thì họ không hề đánh giá thấp — điều này phản bác kết luận.'),
            ('Weakens/Irrelevant', 'Nếu nghiên cứu trước dùng dung dịch kiềm ngay từ đầu thì họ đã thu hồi được phần vi nhựa bám sáp rồi, không giải thích được việc đánh giá thấp.'),
        ],
    ),
    14: _meta(
        'Information and Ideas', 'Inferences', 'Medium', 'A',
        'Nghiên cứu xác nhận “hedonic motivation” (mức độ người dùng cảm nhận việc dùng dịch vụ là dễ chịu/thú vị, đo bằng phát biểu “Using paid music streaming services is pleasant”) tác động tích cực đến ý định đăng ký gói trả phí. Suy ra hợp lý nhất: **các công ty nghe nhạc trực tuyến có lợi thế nếu tìm cách tác động để người dùng tiềm năng cảm nhận bản trả phí dễ chịu khi sử dụng** → Chọn A.',
        'Câu Inference đúng trên SAT luôn bám sát biến số đã kiểm chứng trong bài (cảm nhận “pleasant” → ý định trả phí) và tránh các tuyên bố cực đoan (“unaffected by other factors”) hoặc thu hẹp sai đối tượng (“Apple Music”).',
        [
            ('Đáp án đúng', 'Suy luận trực tiếp, chặt chẽ từ mối tương quan thuận giữa cảm nhận dễ chịu (“pleasant”) và ý định chọn gói trả phí.'),
            ('Unsupported Comparison', 'Apple Music chỉ được nêu làm ví dụ minh họa; bài không so sánh mức độ trung thành giữa Apple Music với nền tảng khác.'),
            ('Contradicts Text', 'Nhóm nghiên cứu dùng chính phát biểu này để đo hedonic motivation và xác nhận giả thuyết, không bác bỏ độ tin cậy của nó.'),
            ('Extreme Language', 'Tìm thấy một yếu tố ảnh hưởng tích cực không có nghĩa là các yếu tố khác đều không tác động (“unaffected by factors other than”).'),
        ],
    ),
    15: _meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Easy', 'B',
        'Mốc thời gian quá khứ xác định “On August 15, 2013” cùng động từ câu sau ở thì quá khứ đơn (“was later included”) yêu cầu động từ chính chia ở thì **quá khứ đơn (simple past)** → Chọn B (“published”).',
        'Khi câu có mốc ngày tháng cụ thể trong quá khứ (“On August 15, 2013”), luôn chia thì quá khứ đơn trừ khi có dấu hiệu hoàn thành hoặc sự thật hiển nhiên.',
        [
            ('Wrong Tense', '“will publish” là thì tương lai, mâu thuẫn với mốc quá khứ 2013.'),
            ('Đáp án đúng', '“published” (quá khứ đơn) khớp hoàn toàn với mốc “On August 15, 2013” và động từ “was later included”.'),
            ('Wrong Tense', '“publishes” là thì hiện tại đơn, sai với sự kiện đã xảy ra năm 2013.'),
            ('Wrong Tense', '“is publishing” là hiện tại tiếp diễn, không phù hợp mốc thời gian quá khứ cụ thể.'),
        ],
    ),
    16: _meta(
        'Standard English Conventions', 'Boundaries', 'Easy', 'A',
        'Cụm phân từ bổ ngữ không thiết yếu “, ratified in 1804,” nằm giữa chủ ngữ “The 12th amendment” và động từ chính “separated”. Vì cụm này được mở bằng **dấu phẩy** trước “ratified”, bắt buộc phải đóng lại bằng **dấu phẩy tương ứng** sau “1804” → Chọn A (“1804,”).',
        'Quy tắc cặp dấu câu cho thành phần xen giữa (nonessential modifier): mở bằng phẩy phải đóng bằng phẩy, mở bằng gạch ngang phải đóng bằng gạch ngang — tuyệt đối không ghép lệch.',
        [
            ('Đáp án đúng', 'Đóng cụm bổ ngữ xen giữa “, ratified in 1804,” bằng dấu phẩy khớp với dấu phẩy mở trước “ratified”.'),
            ('Mismatched Punctuation', 'Không thể mở bằng dấu phẩy mà đóng bằng dấu gạch ngang dài (em-dash).'),
            ('Unclosed Modifier', 'Thiếu dấu phẩy đóng khiến cụm bổ ngữ dính liền vào động từ chính “separated”.'),
            ('Invalid Semicolon', 'Không bao giờ dùng dấu chấm phẩy để ngăn cách chủ ngữ với động từ chính.'),
        ],
    ),
    17: _meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Easy', 'D',
        'Cụm “developed by Navajo Nation artists over 160 years ago” gồm hai danh từ số nhiều thông thường, **không có quan hệ sở hữu**: “artists” (những nghệ nhân) và “160 years ago” (160 năm trước). Do đó không từ nào có dấu nháy sở hữu → Chọn D (“artists over 160 years”).',
        'Trước khi thêm dấu nháy (’s / s’), hãy kiểm tra xem ngay sau danh từ đó có một danh từ thuộc sở hữu của nó không; “over” và “ago” không phải danh từ bị sở hữu!',
        [
            ('Wrong Possessive', 'Sai cả hai dấu sở hữu: “artist’s” (số ít sở hữu) và “year’s” (sai hoàn toàn trước “ago”).'),
            ('Wrong Possessive', '“years’” dùng dấu sở hữu sai vì “ago” là trạng từ, không phải danh từ thuộc sở hữu của “years”.'),
            ('Wrong Possessive', '“artists’” dùng dấu sở hữu sai vì ngay sau đó là cụm trạng ngữ thời gian “over 160 years ago”.'),
            ('Đáp án đúng', 'Cả “artists” và “years” đều là danh từ số nhiều không sở hữu, đúng chuẩn ngữ pháp.'),
        ],
    ),
    18: _meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'C',
        'Xét cụm “the essayist Carolyn Servid, author of *Of Landscape and Longing*”: danh xưng nghề nghiệp đi liền tên riêng (“the essayist Carolyn Servid”) là thông tin **thiết yếu** giúp xác định nhà tiểu luận nào được chọn (chưa từng nhắc trước đó) nên **không có dấu phẩy** giữa “essayist” và “Carolyn Servid”. Ngược lại, cụm đồng vị bổ sung phía sau “author of *Of Landscape and Longing*” là bổ ngữ không thiết yếu nên **bắt buộc có dấu phẩy** sau “Servid” → Chọn C.',
        'Khi giới thiệu lần đầu theo mẫu “the [nghề nghiệp] [Tên riêng], [cụm đồng vị mô tả thêm]”, không tách nghề nghiệp với tên riêng bằng dấu phẩy, nhưng phải đặt dấu phẩy trước cụm đồng vị bổ sung phía sau.',
        [
            ('Missing Comma', 'Thiếu dấu phẩy ngăn cách tên riêng “Carolyn Servid” với cụm đồng vị bổ sung “author of Of Landscape and Longing”.'),
            ('Wrong Comma Placement', 'Đặt sai dấu phẩy giữa “essayist” và “Carolyn Servid”, đồng thời thiếu dấu phẩy trước “author of...”.'),
            ('Đáp án đúng', 'Giữ liền cụm thiết yếu “the essayist Carolyn Servid” và dùng dấu phẩy mở cụm đồng vị “author of Of Landscape and Longing”.'),
            ('Unnecessary Comma', 'Tách “Carolyn Servid” bằng cặp phẩy biến tên riêng thành thông tin thừa, khiến câu còn lại “chose the essayist, author of...” mất xác định tự nhiên.'),
        ],
    ),
    19: _meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Medium', 'B',
        'Câu này kiểm tra **cả 2 đầu bổ ngữ (double modifier)**: (1) Cụm mở đầu “A groundbreaking visual artist of her day,” phải bổ nghĩa ngay cho người họa sĩ (**Hilma af Klint**), loại C và D; (2) Cụm kết thúc sau chỗ trống “, including artists Vasily Kandinsky and Piet Mondrian” nêu ví dụ cho **những người đương thời với bà (“many of her contemporaries”)** chứ không phải ví dụ cho “abstract modes of painting”, nên “many of her contemporaries” phải đứng ngay trước dấu phẩy → Chọn B.',
        'Đừng chỉ kiểm tra chủ ngữ ngay sau bổ ngữ đầu câu — hãy nhìn cả phần chữ phía sau chỗ trống (“including artists...”) để đảm bảo cụm ví dụ đứng sát danh từ nó minh họa!',
        [
            ('Misplaced Modifier', 'Đặt “abstract modes of painting” ngay trước “, including artists Vasily Kandinsky...” khiến câu hiểu nhầm hai họa sĩ là trường phái hội họa.'),
            ('Đáp án đúng', '“Hilma af Klint” đứng ngay sau bổ ngữ mở đầu và “many of her contemporaries” đứng ngay trước “, including artists...”.'),
            ('Dangling Modifier', 'Đặt “well before many of her contemporaries” ngay sau “A groundbreaking visual artist of her day,” — lỗi bổ ngữ lơ lửng.'),
            ('Dangling Modifier', '“the explorations of Hilma af Klint” là sự vật, không thể làm chủ ngữ cho “A groundbreaking visual artist of her day”.'),
        ],
    ),
    20: _meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Medium', 'C',
        'Phân tích hai vị trí sở hữu: (1) Danh từ đứng trước danh động từ/danh từ “modeling of...” cần ở dạng sở hữu. Vì không có mạo từ “an/the” trước danh từ đếm được nên phải dùng **sở hữu số nhiều “astronomers’”** (không thể viết “according to astronomer’s” thiếu mạo từ); (2) “trajectory” thuộc về một thiên thể duy nhất (2010 BL4 — “The small celestial body”) nên dùng **sở hữu số ít “the object’s”** → Chọn C.',
        'Mẹo vàng: Danh từ đếm được số ít ở dạng sở hữu (“astronomer’s”) không bao giờ đứng trơ trụi không có mạo từ (“an/the”) phía trước; và cấu trúc “[Noun]’s modeling of [X]” bắt buộc dùng sở hữu trước “modeling of”.',
        [
            ('Missing Possessives', 'Thiếu cả hai dấu sở hữu; hơn nữa 2010 BL4 là một thiên thể duy nhất nên “objects” số nhiều là sai.'),
            ('Missing Article', '“astronomer’s” là danh từ đếm được số ít nên không thể đứng sau “according to” mà thiếu mạo từ “an/the”.'),
            ('Đáp án đúng', '“astronomers’ modeling” (sở hữu số nhiều, không cần mạo từ) + “the object’s trajectory” (sở hữu số ít của 2010 BL4).'),
            ('Wrong Form Before Gerund', 'Thiếu sở hữu ở “astronomers”: không thể viết “astronomers modeling of...” khi có giới từ “of”.'),
        ],
    ),
    21: _meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'C',
        'Hai mệnh đề độc lập đứng cạnh nhau: Mệnh đề 1 là “Scholars wishing to read a work written by the Roman scholar needn’t despair, though” (trạng từ cuối câu “, though” nối tương phản với câu trước nói nhiều tác phẩm đã thất lạc) và Mệnh đề 2 là “they can still procure a copy of Varro’s *Rerum rusticarum libra tres*, a treatise on agriculture.” Để nối hai mệnh đề độc lập, bắt buộc dùng **dấu chấm phẩy** sau “despair, though” → Chọn C.',
        'Cảnh giác bẫy “though”: khi “though” mang nghĩa “tuy nhiên” bổ sung cho vế trước, nó nằm cuối mệnh đề 1 với mẫu **“, though; [Mệnh đề 2]”** (không phải liên từ phụ thuộc nối vào vế sau vì nghĩa “dù họ vẫn tìm được sách nên đừng tuyệt vọng” là ngược logic!).',
        [
            ('Logical/Boundary Error', 'Thiếu dấu ngắt sau “though” biến “though” thành liên từ phụ thuộc (“mặc dù họ vẫn có thể mua bản sao”), làm đảo ngược hoàn toàn quan hệ nhân quả.'),
            ('Comma Splice', 'Đặt dấu phẩy sau “though” tạo lỗi nối hai mệnh đề độc lập chỉ bằng dấu phẩy (comma splice).'),
            ('Đáp án đúng', '“, though;” kết thúc trọn vẹn mệnh đề độc lập thứ nhất và mở mệnh đề độc lập thứ hai giải thích lý do không cần tuyệt vọng.'),
            ('Logical/Boundary Error', 'Dấu gạch ngang đơn trước “though” vẫn gắn “though” vào mệnh đề sau, gây sai nghĩa logic tương tự câu A.'),
        ],
    ),
    22: _meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'C',
        'Câu trước nêu nguyên nhân: rễ cây quấn chặt đá cổ khiến nhiều phần thành phố Tikal **không thể tiếp cận trực tiếp bằng sức người**. Câu sau nêu kết quả tất yếu: tia sáng xuyên thấu của công nghệ LiDAR là **cách duy nhất** để phát lộ các phần chưa từng biết của thành phố. Quan hệ Nguyên nhân → Kết quả chọn **C (“Hence,” = Do đó)**.',
        'Luôn tóm tắt mối quan hệ giữa 2 câu bằng 1 mũi tên trước khi nhìn đáp án: Không thể vào trực tiếp → LiDAR là cách duy nhất = Nguyên nhân → Kết quả (“Hence,”).',
        [
            ('Wrong Relationship', 'Similarly = Tương tự — dùng để so sánh điểm giống nhau, không phù hợp quan hệ nhân quả.'),
            ('Wrong Relationship', 'Afterward = Sau đó — chỉ trình tự thời gian, không diễn tả hệ quả logic.'),
            ('Đáp án đúng', 'Hence = Do đó, vì vậy — nối chính xác nguyên nhân (khó tiếp cận vật lý) với hệ quả (LiDAR là cách duy nhất).'),
            ('Wrong Relationship', 'Specifically = Cụ thể là — dùng để giải thích chi tiết hơn câu trước, không phải kết luận nhân quả.'),
        ],
    ),
    23: _meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'C',
        'Câu trước định nghĩa **post-consumer waste** (rác thải phát sinh *sau* khi đến tay người tiêu dùng, ví dụ tờ tạp chí bị vứt đi). Câu sau định nghĩa khái niệm đối lập **pre-consumer waste** (rác phát sinh *trước* khi đến tay người tiêu dùng, như giấy vụn cắt thừa khi in). Quan hệ đối lập trực tiếp → Chọn C (“By contrast,”).',
        'Cặp tiền tố đối nghịch rõ rệt (“post-consumer / after” vs. “pre-consumer / before”) là tín hiệu 100% cho từ nối tương phản (“By contrast,”).',
        [
            ('Wrong Relationship', 'For example = Ví dụ — câu sau đưa ra loại rác thải ngược hẳn, không phải ví dụ cho post-consumer waste.'),
            ('Wrong Relationship', 'Specifically = Cụ thể là — sai vì không đi sâu vào post-consumer waste mà chuyển sang pre-consumer waste.'),
            ('Đáp án đúng', 'By contrast = Ngược lại — đánh dấu chính xác sự đối chiếu giữa rác sau tiêu dùng và rác trước tiêu dùng.'),
            ('Wrong Relationship', 'As a result = Kết quả là — giấy vụn khi in không phải hệ quả của việc độc giả vứt tạp chí.'),
        ],
    ),
    24: _meta(
        'Expression of Ideas', 'Transitions', 'Medium', 'D',
        'Câu trước nêu rằng vượt qua đường Kármán, máy bay **không còn duy trì độ cao nhờ lực nâng (“no longer remains aloft using the force of lift”)**. Câu sau nêu cơ chế thay thế: máy bay duy trì bay chủ yếu nhờ **vận tốc (“primarily by its velocity”)**. Quan hệ phủ định X → thay bằng Y đòi hỏi từ nối **D (“Instead,” = Thay vào đó)**.',
        'Mẫu logic kinh điển trên SAT Transitions: “no longer [làm X]. **Instead,** [làm Y].”',
        [
            ('Wrong Relationship', 'Regardless = Bất kể điều đó — dùng khi kết quả vẫn xảy ra bất chấp trở ngại, không phải cơ chế thay thế.'),
            ('Wrong Relationship', 'For instance = Ví dụ — câu sau không minh họa cho việc mất lực nâng mà nêu phương thức thay thế lực nâng.'),
            ('Wrong Relationship', 'Granted = Thừa nhận rằng — dùng để nhượng bộ một phản biện, sai ngữ cảnh.'),
            ('Đáp án đúng', 'Instead = Thay vào đó — nối hoàn hảo giữa việc không dùng lực nâng nữa và việc chuyển sang dựa vào vận tốc.'),
        ],
    ),
    25: _meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'C',
        'Mục tiêu đề bài yêu cầu cực kỳ cụ thể: **nêu năm thành lập của Schomburg Center** (“indicate the year the Schomburg Center was founded”). Dựa vào ghi chú thứ 3 (“It was founded in 1925”), chỉ câu C đáp ứng đúng mục tiêu → Chọn C.',
        'Trong câu Rhetorical Synthesis, đọc câu mục tiêu (“The student wants to...”) trước tiên và bám chặt từ khóa đích (“year... founded”) để chốt đáp án trong vài giây.',
        [
            ('Wrong Goal', 'Chỉ nêu người được đặt tên cho thư viện, không nêu năm thành lập.'),
            ('Wrong Goal', 'Chỉ nêu loại hình tổ chức (“research library”), thiếu năm thành lập.'),
            ('Đáp án đúng', 'Nêu trực tiếp và chính xác năm thành lập 1925 của Schomburg Center.'),
            ('Wrong Goal', 'Chỉ nêu vị trí địa lý (New York City), không nêu năm thành lập.'),
        ],
    ),
    26: _meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'B',
        'Mục tiêu: **so sánh hàm lượng vitamin C của cải Brussels và táo** (“compare the vitamin C content of brussels sprouts and apples”). Ghi chú cho biết ascorbic acid = vitamin C, cải Brussels có 80 mg/100 g còn táo có 6 mg/100 g. Chỉ câu B so sánh hàm lượng vitamin C của cả hai loại → Chọn B.',
        'Câu mục tiêu có động từ “compare X and Y” bắt buộc đáp án phải đề cập ĐỒNG THỜI cả X, Y và mối so sánh về đúng thuộc tính được hỏi (hàm lượng vitamin C).',
        [
            ('Incomplete Comparison', 'Chỉ nêu hàm lượng vitamin C của cải Brussels mà không nhắc đến táo.'),
            ('Đáp án đúng', 'Đề cập cả hai loại thực phẩm và so sánh chính xác hàm lượng vitamin C (cải Brussels chứa nhiều hơn táo).'),
            ('Wrong Attribute', 'So sánh phân loại rau/quả thay vì so sánh hàm lượng vitamin C.'),
            ('Incomplete/Wrong Goal', 'Nói về việc con người không tự tổng hợp được ascorbic acid, không so sánh với táo.'),
        ],
    ),
    27: _meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'A',
        'Mục tiêu: **nhấn mạnh điểm tương đồng giữa hai bộ phim** (“emphasize a similarity between the two films”). Cả *The Three Passions* và *Désirée* đều có sự góp mặt của nữ diễn viên Merle Oberon — chỉ câu A nêu điểm chung này (“are both films that include Merle Oberon”) → Chọn A.',
        'Phân biệt thật rõ yêu cầu “similarity” (điểm giống nhau: từ khóa *both*) với “difference” (điểm khác nhau: từ khóa *whereas*, *however*).',
        [
            ('Đáp án đúng', 'Nhấn mạnh trực tiếp điểm chung của hai bộ phim: cả hai đều có sự tham gia của Merle Oberon.'),
            ('Opposite Goal', 'Nhấn mạnh sự khác biệt về thời điểm phát hành (“whereas”) thay vì điểm tương đồng.'),
            ('Opposite Goal', 'Nhấn mạnh sự khác biệt về vai diễn không ghi tên vs. có ghi tên (“however”).'),
            ('Incomplete', 'Chỉ nhắc đến một bộ phim (*The Three Passions*), không đề cập *Désirée*.'),
        ],
    ),
}


# ============================================================================
# MODULE 2 METADATA & 2-PASS AUDITED VIETNAMESE EXPLANATIONS (27 QUESTIONS)
# ============================================================================

M2_META = {
    1: _meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'C',
        'Mệnh đề quan hệ ngay sau chỗ trống giải thích rõ tác động của thủy triều vịnh Mexico: “which shift sediments along the coast and reshape the deltaic lobes over time” (dịch chuyển trầm tích dọc bờ biển và định hình lại các thùy châu thổ). Vậy hình dạng và kích thước châu thổ bị **tác động/ảnh hưởng** bởi thủy triều → Chọn C (“influenced”).',
        'Chọn từ có sắc thái trung tính phù hợp với văn bản khoa học địa lý (“shift sediments and reshape”) thay vì các từ mang sắc thái khen/chê chủ quan như “enhanced” hay “protected”.',
        [
            ('Wrong Meaning', 'surpassed = bị vượt qua — vô nghĩa khi nói hình dạng châu thổ bị vượt qua bởi thủy triều.'),
            ('Too Positive', 'enhanced = được cải thiện/nâng cao — thủy triều chỉ làm thay đổi hình dạng chứ không “cải thiện” chất lượng châu thổ.'),
            ('Đáp án đúng', 'influenced = bị ảnh hưởng, chi phối — diễn đạt chuẩn xác và trung tính tác động dịch chuyển trầm tích của thủy triều.'),
            ('Wrong Meaning', 'protected = được bảo vệ — trái ngược ý thủy triều dịch chuyển trầm tích và liên tục biến đổi thùy châu thổ.'),
        ],
    ),
    2: _meta(
        'Craft and Structure', 'Words in Context', 'Medium', 'A',
        'Lisa Linn Kanae là nhà văn **đương đại** (“contemporary”), còn câu sau liệt kê những câu chuyện truyền thống của người bản địa *Kanaka Maoli* và các nhà văn xưa như David Malo tạo nên di sản văn học phong phú của Hawai‘i. Điều đó có nghĩa tác phẩm của bà **được đi trước / kế thừa từ** một lịch sử văn học lâu đời → Chọn A (“preceded”).',
        'Chú ý manh mối thời gian “contemporary” (hiện đại) đặt cạnh “rich literary history / traditional stories / heritage” (quá khứ) → động từ quan hệ thời gian chuẩn là “preceded by”.',
        [
            ('Đáp án đúng', 'preceded = được đi trước bởi — khớp chính xác trục thời gian giữa truyền thống văn học lâu đời và tác giả đương đại.'),
            ('Wrong Meaning', 'summarized = được tóm tắt bởi — một lịch sử văn học đi trước không thể “tóm tắt” tác phẩm hiện đại.'),
            ('Opposite Direction', 'supplanted = bị thay thế bởi — lịch sử truyền thống đi trước chứ không thay thế tác phẩm đương đại.'),
            ('Wrong Meaning', 'overlooked = bị bỏ qua bởi — vô lý về mặt logic lẫn giọng điệu tôn vinh của đoạn văn.'),
        ],
    ),
    3: _meta(
        'Craft and Structure', 'Words in Context', 'Hard', 'C',
        'Câu mở đầu cho biết các nhà khảo cổ tìm thấy **rất nhiều** hạt cườm vỏ ốc *Tritia gibbosula* (“a plethora of beads”) tại **nhiều di chỉ khắp** tây Bắc Phi (“in many Middle Stone Age sites across western North Africa”). Danh từ tóm gọn sự hiện diện dày đặc, phổ biến rộng khắp đó là **“ubiquity”** (sự phổ biến khắp nơi) → Chọn C.',
        'Học thuộc nhóm từ vựng học thuật tần suất cao trên Module 2 Hard: *ubiquity* (có mặt khắp nơi = “plethora... in many sites across”), *expediency* (tính thực dụng), *fecundity* (khả năng sinh sản), *heterogeneity* (tính đa dạng).',
        [
            ('Wrong Meaning', 'expediency = tính tiện lợi/thực dụng — không mô tả sự hiện diện dày đặc của hiện vật trên diện rộng.'),
            ('Wrong Meaning', 'fecundity = khả năng sinh sản/độ màu mỡ — dùng cho sinh vật hoặc đất đai, không dùng cho hạt cườm khảo cổ.'),
            ('Đáp án đúng', 'ubiquity = sự hiện diện phổ biến khắp nơi — khớp hoàn hảo với “a plethora of beads... in many sites across western North Africa”.'),
            ('Wrong Context', 'heterogeneity = tính không đồng nhất/đa dạng — đoạn văn nhấn mạnh số lượng lớn và phân bố rộng, không nói các hạt cườm khác nhau về mẫu mã.'),
        ],
    ),
    4: _meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Medium', 'B',
        'Cụm gạch chân “thus capitalizing on the research potential offered by a vast but hitherto relatively underutilized source of insight into the biological past” đưa ra nhận xét đánh giá tầm quan trọng của **cách tiếp cận** mà nhóm Oliveira sử dụng (khai thác DNA lịch sử từ mẫu vật bảo tàng — một nguồn dữ liệu đồ sộ nhưng lâu nay ít được tận dụng) → Chọn B.',
        'Phân biệt rạch ròi giữa **approach/methodology** (cách tiếp cận dùng DNA bảo tàng) với **findings** (kết quả cụ thể về cỏ *Chasechloa* — thứ hoàn toàn không được nêu trong đoạn).',
        [
            ('Not Mentioned', 'Cụm gạch chân không liệt kê các ứng dụng cụ thể nào trong tương lai của phương pháp.'),
            ('Đáp án đúng', 'Đưa ra bình luận về ý nghĩa/giá trị của cách tiếp cận (dùng DNA lịch sử từ bộ sưu tập tự nhiên) mà nhóm Oliveira áp dụng.'),
            ('Wrong Focus', 'Đoạn văn không hề nhắc đến phát hiện cụ thể nào về DNA thực vật của nhóm Oliveira; trọng tâm là phương pháp tiếp cận.'),
            ('Not Explained', 'Chỉ nêu phương pháp này trước kia ít được khai thác (“hitherto relatively underutilized”) chứ không giải thích *tại sao*.'),
        ],
    ),
    5: _meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Medium', 'D',
        'Cụm danh từ có từ chỉ định “<u>This relative scarcity</u>” (Sự khan hiếm tương đối này) quy chiếu trực tiếp về câu ngay trước đó: các hiện vật làm từ thực vật rất hiếm khi được nghiên cứu vì chúng dễ phân hủy (“seldom studied due to their perishable nature”). Đây chính là một **tình huống khó khăn/hạn chế** đã được trình bày trước đó trong văn bản → Chọn D.',
        'Với cụm gạch chân mở đầu bằng “This + [danh từ trừu tượng]”, hãy lùi lại đúng câu liền trước để xác định nó đang quy chiếu (anaphoric reference) về vấn đề/tình huống nào.',
        [
            ('Contradicts Text', 'Nhóm nghiên cứu đã đạt được hiểu biết mới rất đáng phấn khích (“contributed new insights”, “exciting”), không hề thất bại mục tiêu.'),
            ('Contradicts Text', 'Phát hiện không hề “uncertain” — nhóm đã xác định rõ hiện vật có niên đại cổ hơn trước đây từng nghĩ.'),
            ('Mischaracterization', 'Hai câu trước mới so sánh hiện vật bền và hiện vật thực vật; cụm 3 từ “This relative scarcity” chỉ hồi chỉ lại sự hiếm gặp chứ không phân biệt hai loại hiện vật.'),
            ('Đáp án đúng', 'Quy chiếu trực tiếp đến thực trạng khó khăn nêu ở câu trước: hiện vật thực vật dễ phân hủy nên rất hiếm gặp để nghiên cứu.'),
        ],
    ),
    6: _meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Medium', 'B',
        'Tác phẩm *In a Flight of Starlings* của nhà vật lý Giorgio Parisi tập trung vào những khởi đầu sai lầm và sai sót thường nhật trong nghiên cứu khoa học; tác giả Sam Kean đặc biệt quan tâm đến khía cạnh này và lập luận rằng nếu các nhà khoa học lược bỏ “yếu tố con người” đó thì sẽ không thể giải thích khoa học thực sự vận hành ra sao. Vậy mục đích chính của đoạn là **nêu một điểm đồng thuận giữa Parisi và Kean trong cách nhìn về công việc khoa học** → Chọn B.',
        'Loại trừ cẩn thận các phương án bóp méo chủ thể hoặc chi tiết: Kean mới là người dùng “nonfiction narrative” (không phải Parisi), và Kean đánh giá cao sự chân thực về *sai lầm*, không phải *thành tựu*.',
        [
            ('Contradicts Text', 'Cả hai không phản đối phương pháp nghiên cứu khoa học và giữa họ là sự đồng thuận chứ không phải khác biệt.'),
            ('Đáp án đúng', 'Cả Parisi (qua chủ đề tiểu luận) và Kean (qua lập luận ủng hộ) đều coi những sai sót, thử-sai là phần cốt lõi của việc làm khoa học.'),
            ('Misread Detail', 'Sam Kean là người viết “nonfiction narrative” (Parisi viết tập tiểu luận), và Kean thích tác phẩm vì nói về sai sót chứ không phải khoe thành tựu.'),
            ('Unsupported Claim', 'Kean không hề nhận xét Parisi quá khiêm tốn về thành tích cá nhân.'),
        ],
    ),
    7: _meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Hard', 'D',
        'Trong phần gạch chân, Camillo nói nhà vua Sicily cho gọi ông về: “<u>to whose feeling sorrows I might be some allay—or I o’erween [presume] to think so</u>” (người mà ta *có thể* giúp xoa dịu phần nào nỗi đau—hoặc ta đang quá tự phụ khi nghĩ như vậy). Cách nói rào đón “might... or I o’erween to think so” cho thấy Camillo **nhận thức rằng một lợi ích mà sự hiện diện của ông có thể mang lại cho vua Sicily chỉ mang tính phỏng đoán** → Chọn D.',
        'Đọc kỹ chú thích trong ngoặc vuông `[presume]` của đề thi: từ cổ *o’erween* được giải thích ngay thành *presume* (tự cho là / võ đoán), chỉ thẳng vào sắc thái “merely speculative”.',
        [
            ('Contradicts Text', 'Không phải động lực *chính* (“which is *another* spur” — trước đó ông muốn về yên nghỉ ở quê hương sau 15 năm), và lời rào đón làm giảm nhẹ chứ không củng cố ý đó.'),
            ('Wrong Function', 'Phần gạch chân thể hiện sự khiêm nhường/dè dặt về khả năng an ủi vua Sicily, không phải cảm giác bị ép phải thuyết phục Polixenes.'),
            ('Contradicts Text', 'Camillo không kỳ vọng Polixenes được an ủi, và bản thân ông cũng tự có mong muốn hồi hương (“I desire to lay my bones there”).'),
            ('Đáp án đúng', '“might be some allay—or I o’erween [presume] to think so” diễn đạt chính xác nhận thức rằng lợi ích mang lại cho vua Sicily chỉ là suy đoán.'),
        ],
    ),
    8: _meta(
        'Information and Ideas', 'Central Ideas and Details', 'Easy', 'C',
        'Khổ thơ thứ hai trích trực tiếp suy nghĩ tự hào của người nghệ sĩ khi hoàn thành bức tượng: “And surely this shall last!” (Chắc chắn tác phẩm này sẽ trường tồn!) và “Fixed in immortal marble is my fame!” (Danh tiếng của ta đã khắc chặt trong đá cẩm thạch bất tử!). Vậy người nghệ sĩ tin bức tượng **sẽ đem lại danh tiếng bền lâu nhờ vượt qua thử thách thời gian** → Chọn C.',
        'Đọc sát hai dòng thơ trong ngoặc kép diễn tả suy nghĩ trực tiếp của nhân vật (“he proudly thought”) để tránh bị nhiễu bởi hiện trạng đổ nát ở phần giới thiệu.',
        [
            ('Unsupported Detail', 'Bài thơ nhắc “last touch of his chisel” nhưng nghệ sĩ không nói bức tượng sẽ được ca ngợi vì chi tiết chạm khắc tinh xảo.'),
            ('Contradicts Text', 'Nghệ sĩ tin đá cẩm thạch là bất tử (“immortal marble”, “surely this shall last”), không hề nghĩ nó sẽ xuống cấp để phải sửa chữa.'),
            ('Đáp án đúng', 'Khớp trực tiếp với “surely this shall last” (chống chọi thời gian) và “Fixed in immortal marble is my fame” (danh tiếng trường tồn).'),
            ('Not Mentioned', 'Không có chi tiết so sánh bức tượng này với các bức tượng thần Vệ Nữ khác.'),
        ],
    ),
    9: _meta(
        'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium', 'A',
        'Chú ý thang xếp hạng nghịch đảo trong tiêu đề bảng: **scale of 1 to 25; 1 = highest** (số càng NHỎ thì thứ hạng càng CAO!). Xét cột **Stakeholders**, thứ hạng của 5 dịch vụ lần lượt là: enhancement of pollination (**7** — cao nhất!), prevention of soil erosion (11), preservation of cultural knowledge and heritage (15), provision of medicinal plants (21), enhancement of carbon sequestration (22). Vì vậy dữ liệu ủng hộ kết luận nhấn mạnh thụ phấn với nhóm stakeholders là câu A → Chọn A.',
        'Gặp bảng xếp hạng (Ranking), luôn khoanh tròn quy ước “1 = highest” ngay lập tức: hạng 7 CAO HƠN hạng 11, 15, 21, 22 — phần lớn sai lầm đến từ việc nhìn số lớn hơn rồi tưởng xếp hạng cao hơn!',
        [
            ('Đáp án đúng', 'Với nhóm stakeholders, “enhancement of pollination” xếp hạng 7 — cao hơn (số nhỏ hơn) cả 4 dịch vụ còn lại (11, 15, 21, 22), ủng hộ trực tiếp đề xuất quảng bá.'),
            ('Misread Scale & Irrelevant', 'Sai chiều xếp hạng: hạng 11 (stakeholders) CAO hơn hạng 13 (project leaders), và cũng không liên quan đến pollination.'),
            ('Misread Scale', 'Sai chiều xếp hạng: hạng 12 (general public) THẤP hơn hạng 7 (stakeholders).'),
            ('Misread Scale', 'Sai chiều xếp hạng: hạng 22 (carbon sequestration) THẤP hơn nhiều so với hạng 7 (pollination).'),
        ],
    ),
    10: _meta(
        'Information and Ideas', 'Command of Evidence (Textual)', 'Hard', 'C',
        'Quan điểm truyền thống cho rằng gen tạo kích thước nhỏ ở chó mới xuất hiện **trong vòng 20.000 năm qua** do chọn giống của con người. Nhóm Ostrander phản bác quan điểm này sau khi phát hiện đột biến liên quan đến gen *IGF1* phổ biến ở các giống chó nhà. Để ủng hộ trực tiếp lập luận phản bác này, cần bằng chứng cho thấy: (1) đột biến *IGF1* thật sự **chi phối kích thước cơ thể**, và (2) nó đã tồn tại **trước mốc 20.000 năm ở tổ tiên của loài chó** (hóa thạch sói Siberia 53.000 năm tuổi) → Chọn C.',
        'Cẩn thận phân biệt giữa **bản thân gen *IGF1*** (vốn có ở nhiều loài thú nên câu A không chứng minh được gì) với **đột biến tạo biến thể kích thước nhỏ của gen *IGF1*** (câu C)!',
        [
            ('Subtle Trap', 'Đoạn văn đã nói sẵn *IGF1* là gen có ở nhiều loài động vật có vú; tìm thấy bản thân gen *IGF1* ở sói đỏ không chứng minh *đột biến tạo cỡ nhỏ* xuất hiện trước 20.000 năm ở tổ tiên chó.'),
            ('Irrelevant Detail', 'Đột biến ảnh hưởng đến đặc điểm *khác* kích thước cơ thể không bác bỏ được giả thuyết về nguồn gốc kích thước nhỏ.'),
            ('Đáp án đúng', 'Khóa chặt cả 2 mắt xích: đột biến *IGF1* chi phối kích thước cơ thể VÀ đã xuất hiện từ 53.000 năm trước ở tổ tiên loài chó (sớm hơn xa mốc 20.000 năm).'),
            ('Weakens Assertion', 'Nếu biến thể đó mới xuất hiện không quá 20.000 năm trước thì lại ủng hộ quan điểm cũ, đi ngược khẳng định của nhóm Ostrander.'),
        ],
    ),
    11: _meta(
        'Information and Ideas', 'Command of Evidence (Textual)', 'Easy', 'A',
        'Cơ sở dữ liệu chấm 2 tiêu chí độc lập: **level of detail** (độ chi tiết/cụ thể của dữ liệu báo cáo) và **level of traceability** (độ rõ ràng của mô tả quy trình). Nhóm hai kết luận nghiên cứu của Kozak & Keoleian có **độ cụ thể trong dữ liệu (“more specificity in its data”)** cao hơn nghiên cứu của Oguchi et al. Để **phản bác trực tiếp** kết luận này, cần bằng chứng rằng Kozak & Keoleian có **điểm detail rating thấp hơn** Oguchi et al. → Chọn A.',
        'Đọc kỹ ánh xạ thuật ngữ định nghĩa trong ngoặc đơn: “specificity in its data” = “level of detail”, còn “procedures” = “level of traceability”.',
        [
            ('Đáp án đúng', 'Điểm “detail rating” thấp hơn đồng nghĩa dữ liệu kém cụ thể hơn, bác bỏ trực tiếp kết luận của nhóm thứ hai.'),
            ('Wrong Metric', '“traceability rating” đo độ rõ ràng của quy trình, không phải độ cụ thể của dữ liệu.'),
            ('Supports Instead of Challenges', 'Điểm detail cao của Kozak & Keoleian không bác bỏ kết luận mà có xu hướng củng cố nó.'),
            ('Supports Instead of Challenges', 'Điểm detail thấp của Oguchi et al. lại ủng hộ kết luận của nhóm thứ hai.'),
        ],
    ),
    12: _meta(
        'Information and Ideas', 'Command of Evidence (Textual)', 'Hard', 'D',
        'Đất tan băng tạo hai chiều ngược nhau đối với cân bằng CO<sub>2</sub>: (1) thực vật hấp thụ CO<sub>2</sub> (làm GIẢM net CO<sub>2</sub>), và (2) hô hấp dị dưỡng của vi sinh vật đất phát thải CO<sub>2</sub> (làm TĂNG net CO<sub>2</sub>). Nhóm Yonghong Yi kết luận **net CO<sub>2</sub> sẽ tăng** nếu tuyết phủ theo mùa đến **sớm hơn** thời điểm mặt đất đóng băng. Cơ chế ủng hộ trực tiếp nhất là câu D: lớp tuyết đến sớm **cách nhiệt giữ ấm cho đất**, giúp vi sinh vật tiếp tục hô hấp thải CO<sub>2</sub> ngay trong giai đoạn thực vật không sinh trưởng (không có hấp thụ CO<sub>2</sub> bù lại) → Chọn D.',
        'Với bài cân bằng hai chiều (Output − Absorption = Net), muốn chứng minh Net TĂNG thì cần bằng chứng làm Output tăng/duy trì trong khi Absorption giảm hoặc bằng 0!',
        [
            ('Ambiguous Direction', 'Nói ảnh hưởng của nhiệt độ đất lên cả thực vật lẫn vi sinh vật mạnh hơn khi có tuyết phủ nhưng không cho biết chiều nào thắng thế để làm net CO<sub>2</sub> tăng.'),
            ('Ambiguous Net Effect', 'Nếu tuyết đến sớm làm giảm CẢ tăng trưởng thực vật (giảm hấp thụ) LẪN tốc độ hô hấp dị dưỡng (giảm phát thải) thì không suy ra được net CO<sub>2</sub> tăng.'),
            ('Wrong Variable', 'So sánh độ dài thời gian tuyết tồn tại giữa các vùng không gian khác nhau, không giải thích tác động của việc tuyết đến *sớm hơn* mốc đóng băng.'),
            ('Đáp án đúng', 'Lớp tuyết cách nhiệt giúp phát thải CO<sub>2</sub> từ hô hấp dị dưỡng tiếp diễn khi thực vật không hấp thụ CO<sub>2</sub>, đẩy trực tiếp net CO<sub>2</sub> tăng lên.'),
        ],
    ),
    13: _meta(
        'Information and Ideas', 'Inferences', 'Medium', 'B',
        'Kết nối hai dữ kiện dạng tam đoạn luận: (1) Tại New York City, người nói **tiếng Quan Thoại (Mandarin)** tập trung chủ yếu ở Flushing (quận **Queens**), còn người nói **tiếng Quảng Đông & Phúc Châu (Cantonese & Fuzhounese)** tập trung ở Chinatown (quận **Manhattan**); (2) Tiếng Quan Thoại phổ biến ở **miền bắc Trung Quốc**, còn tiếng Quảng Đông & Phúc Châu phổ biến ở **miền nam Trung Quốc**. Suy luận trực tiếp: **người di cư từ bắc Trung Quốc có xu hướng định cư ở Queens, còn người từ nam Trung Quốc có xu hướng định cư ở Manhattan** → Chọn B.',
        'Trong dạng Inferences ghép chuỗi A→B và B→C, hãy liên kết đúng các đầu mối địa lý/ngôn ngữ mà không thêm giả định ngoài bài (như số lượng dân số hay lịch sử di cư).',
        [
            ('Not Mentioned', 'Đoạn văn không đề cập thời điểm di cư sớm/muộn hay khả năng nói nhiều phương ngữ.'),
            ('Đáp án đúng', 'Suy luận logic trực tiếp từ chuỗi Bắc TQ → Mandarin → Flushing (Queens) và Nam TQ → Cantonese/Fuzhounese → Chinatown (Manhattan).'),
            ('Unsupported Quantity', 'Đoạn văn không đưa số liệu dân số so sánh tổng số người nói tiếng Quảng Đông/Phúc Châu với tiếng Quan Thoại.'),
            ('Not Mentioned', 'Không có thông tin nào nói người nhập cư thường xuyên chuyển nhà qua lại giữa Queens và Manhattan.'),
        ],
    ),
    14: _meta(
        'Information and Ideas', 'Inferences', 'Medium', 'A',
        'Đoạn văn nêu việc gọi *Black Swan Green* là “tiểu thuyết tự truyện” có **mặt hạn chế** về cách công chúng nhìn nhận tác phẩm, vì nghệ thuật rất đề cao **sự sáng tạo và trí tưởng tượng** (“given the high value placed on creativity and imagination in artistic endeavors”). Do đó, những độc giả hiểu nhãn mác này theo nghĩa Mitchell chỉ hư cấu hóa lại chuyện có thật có thể kết luận rằng **cuốn tiểu thuyết kém xứng đáng được tán dương hơn so với trường hợp nó không dựa trên chuyện có thật** → Chọn A.',
        'Bám chặt chuỗi nhân quả ở hai câu cuối: Nghệ thuật đề cao trí tưởng tượng → bị xem là “merely fictionalized actual events” (ít tưởng tượng) → bị đánh giá thấp giá trị/kém đáng khen hơn.',
        [
            ('Đáp án đúng', 'Kết nối trọn vẹn “drawbacks in terms of how the work is perceived” với tiêu chí đề cao sức sáng tạo trong nghệ thuật.'),
            ('Wrong Subject', 'Câu cuối đang nói về kết luận của nhóm “Readers who take this characterization...”, không phải tranh cãi giữa các nhà phê bình (“critics disagree”).'),
            ('Irrelevant Detail', 'Độ khó khi nhận diện nguyên mẫu ngoài đời của các nhân vật khác không giải thích hạn chế về giá trị sáng tạo.'),
            ('Misread Text', 'Đoạn văn viết tác phẩm “is regularly described as” (được người khác gọi là), không nói Mitchell tự nhận hay hối hận về việc công bố.'),
        ],
    ),
    15: _meta(
        'Standard English Conventions', 'Boundaries', 'Easy', 'C',
        'Mệnh đề phía trước chỗ trống là một mệnh đề độc lập hoàn chỉnh dẫn nhập vào một danh sách gồm ba thời kỳ (“divided ancient Egyptian history into three primary periods”), theo sau là phần liệt kê cụ thể 3 thời kỳ (Old Kingdom, Middle Kingdom, New Kingdom). Dấu câu chuẩn để giới thiệu danh sách ngay sau mệnh đề độc lập là **dấu hai chấm (colon)** → Chọn C (“periods: the”).',
        'Mẫu cấu trúc chuẩn cho dấu hai chấm: **[Mệnh đề độc lập giới thiệu số lượng/danh mục]: [Danh sách liệt kê chi tiết]**. Dùng dấu chấm tạo mảnh câu (fragment), còn dùng dấu chấm phẩy sai vì vế sau không phải mệnh đề độc lập.',
        [
            ('Sentence Fragment', 'Dùng dấu chấm biến phần liệt kê “The Old Kingdom..., the Middle Kingdom..., and the New Kingdom...” thành câu cụt không có động từ chính.'),
            ('Invalid Semicolon', 'Dấu chấm phẩy chỉ dùng giữa hai mệnh đề độc lập; vế sau chỉ là cụm danh từ liệt kê.'),
            ('Đáp án đúng', 'Dấu hai chấm mở ra danh sách ba thời kỳ lịch sử Ai Cập cổ đại hoàn toàn chuẩn mực sau mệnh đề độc lập.'),
            ('Ambiguous Punctuation', 'Dấu phẩy khiến cụm “three primary periods” dễ bị hiểu nhầm là mục đầu tiên trong chuỗi 4 danh từ ngang hàng.'),
        ],
    ),
    16: _meta(
        'Standard English Conventions', 'Boundaries', 'Easy', 'A',
        'Trong cụm “the hit song “Little Marie” by Chuck Berry”, tên bài hát “Little Marie” là thông tin **thiết yếu** xác định bài hit nào của Chuck Berry (ông có nhiều bài hit). Do đó **không đặt bất kỳ dấu câu nào** giữa danh từ “song” và tên bài hát → Chọn A (“song”).',
        'Khi danh từ chung có mạo từ xác định (“the hit song”, “the novel”, “the poet”) đứng ngay trước tên riêng thiết yếu, KHÔNG chen dấu phẩy, dấu hai chấm hay dấu chấm phẩy vào giữa.',
        [
            ('Đáp án đúng', 'Không dùng dấu câu vì tên bài hát “Little Marie” là thành phần định danh thiết yếu đi liền sau “the hit song”.'),
            ('Unnecessary Comma', 'Đặt dấu phẩy biến “Little Marie” thành bổ ngữ thừa; nếu bỏ đi sẽ còn “you would have heard the hit song by Chuck Berry” (không rõ bài nào).'),
            ('Invalid Colon', 'Vế trước dấu hai chấm (“...heard the hit song”) chưa tạo thành một mệnh đề độc lập hoàn chỉnh về ý.'),
            ('Invalid Semicolon', 'Dấu chấm phẩy không thể nối một cụm chưa hoàn chỉnh với tên bài hát.'),
        ],
    ),
    17: _meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Easy', 'B',
        'Xác định chủ ngữ cốt lõi đứng trước chuỗi cụm giới từ/động từ nguyên mẫu: “**The allocation** [of a new country dialing prefix (+380) to route incoming international calls] _______”. Chủ ngữ chính là danh từ số ít **“The allocation”** (đừng bị đánh lừa bởi danh từ số nhiều “calls” sát chỗ trống!), và sự kiện xảy ra năm 1991 nên chọn động từ số ít quá khứ **B (“was”)**.',
        'Mẹo gạch bỏ nhiễu S-V Agreement: gạch toàn bộ cụm bắt đầu bằng giới từ (“of...”) và cụm mục đích (“to route...”) để lộ chủ ngữ thật (“The allocation” = số ít). Trong 4 đáp án chỉ duy nhất B là số ít!',
        [
            ('Subject-Verb Disagreement', '“are” là động từ số nhiều (và hiện tại), sai với chủ ngữ số ít “The allocation”.'),
            ('Đáp án đúng', '“was” là động từ số ít duy nhất, khớp cả về số với “The allocation” lẫn thì quá khứ với sự kiện 1991.'),
            ('Subject-Verb Disagreement', '“have been” chia số nhiều, sai với chủ ngữ số ít “The allocation”.'),
            ('Subject-Verb Disagreement', '“were” chia số nhiều, bẫy những bạn nhìn nhầm danh từ “calls” ngay trước chỗ trống.'),
        ],
    ),
    18: _meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'C',
        'Câu liệt kê ba yếu tố chính sau “namely,” trong đó các mục tự chúng đã chứa dấu phẩy bên trong: (1) *the size and composition of the meteoroids*; (2) *their velocity upon entering Earth’s mesosphere, with higher-velocity meteoroids releasing more energy*; và (3) *and atmospheric fluctuations, such as changes in humidity*. Để ý dấu chấm phẩy `;` đã cho sẵn trước mục 3 (“; and atmospheric fluctuations”) — đây là danh sách phức tạp dùng **dấu chấm phẩy (super-comma)** phân cách các mục → Chọn C (“meteoroids; their”).',
        'Khi thấy một dấu chấm phẩy `;` đứng trước “and” ở cuối chuỗi liệt kê có dấu phẩy nội bộ, hãy lập tức dùng đúng dấu chấm phẩy `;` để ngăn cách các mục trước đó cho đồng nhất!',
        [
            ('Inconsistent Separator', 'Dấu gạch ngang không phù hợp để phân tách mục 1 và mục 2 trong danh sách đã dùng dấu chấm phẩy ở mục 3.'),
            ('Ambiguous Separator', 'Dùng dấu phẩy giữa mục 1 và mục 2 sẽ lẫn với các dấu phẩy nội bộ trong mục 2 và phá vỡ tính nhất quán với dấu `;` phía sau.'),
            ('Đáp án đúng', 'Dấu chấm phẩy (“super-comma”) phân tách rạch ròi mục 1 và mục 2, đồng bộ hoàn toàn với dấu chấm phẩy trước “and atmospheric fluctuations”.'),
            ('Sentence Fragment', 'Dùng dấu chấm biến cả mục 2 và mục 3 thành một câu cụt không có động từ chính chia thì.'),
        ],
    ),
    19: _meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Medium', 'A',
        'Tìm chủ ngữ của động từ cần điền trong mệnh đề “that”: “that **its ruminations** [on fourteenth-century Persian life] _______ Iranian society hundreds of years later.” Chủ ngữ cốt lõi là danh từ **số nhiều “its ruminations”** (những suy tư của tác phẩm). Trong 4 đáp án, B/C/D đều là động từ số ít, chỉ duy nhất **A (“influence”)** chia số nhiều → Chọn A.',
        'Mẹo “3 số ít – 1 số nhiều”: khi 3 lựa chọn cùng chia số ít (*influences, is influencing, has influenced*) và chỉ 1 lựa chọn chia số nhiều (*influence*), hãy kiểm tra ngay chủ ngữ cốt lõi — gần như chắc chắn bài đang kiểm tra Subject-Verb Agreement!',
        [
            ('Đáp án đúng', '“influence” là động từ số nhiều duy nhất khớp với chủ ngữ số nhiều “its ruminations” (và khớp thì hiện tại mô tả ảnh hưởng còn kéo dài).'),
            ('Subject-Verb Disagreement', '“influences” chia số ít — bẫy nhìn nhầm danh từ “life” ngay trước chỗ trống.'),
            ('Subject-Verb Disagreement', '“is influencing” chia số ít, không hòa hợp với “its ruminations”.'),
            ('Subject-Verb Disagreement', '“has influenced” chia số ít, không hòa hợp với “its ruminations”.'),
        ],
    ),
    20: _meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'A',
        'Kết hợp 2 quy tắc dấu phẩy chuẩn SAT: (1) Danh xưng nghề nghiệp đứng trước tên riêng không có mạo từ (“Slovak photographer Mária Svarbová”) là cụm liền mạch **không có dấu phẩy** giữa “photographer” và “Mária Svarbová” (loại C, D); (2) Mệnh đề quan hệ bổ sung phía sau một tên người cụ thể (“who aptly describes her photos as...”) là mệnh đề quan hệ không xác định nên **bắt buộc có dấu phẩy** trước “who” (loại B) → Chọn A.',
        'Công thức ghi nhớ nhanh: **[Tính từ + Nghề nghiệp + Tên riêng], who...** — KHÔNG phẩy trước tên riêng, CÓ phẩy trước “who”.',
        [
            ('Đáp án đúng', 'Giữ liền cụm “Slovak photographer Mária Svarbová” và đặt dấu phẩy chuẩn xác trước mệnh đề quan hệ không xác định “who...”.'),
            ('Missing Comma', 'Thiếu dấu phẩy trước mệnh đề quan hệ không xác định “who aptly describes...” bổ nghĩa cho tên riêng cụ thể.'),
            ('Wrong Comma Placement', 'Đặt thừa dấu phẩy giữa “photographer” và tên riêng, đồng thời thiếu dấu phẩy trước “who”.'),
            ('Unnecessary Comma', 'Đặt dấu phẩy sau “photographer” biến tên riêng “Mária Svarbová” thành bổ ngữ không thiết yếu là sai khi phía trước không có “the” xác định.'),
        ],
    ),
    21: _meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Medium', 'C',
        'Xét cấu trúc cả câu: Mệnh đề chính là “ancient Egyptians slept on hard, elevated headrests”, theo sau bởi dấu phẩy và cụm “their design _______ airflow, protection from insects, and hairstyle maintenance over comfort.” Nếu điền động từ chia thì (A, B, D), vế sau trở thành một mệnh đề độc lập thứ hai nối với mệnh đề đầu chỉ bằng dấu phẩy → **lỗi Comma Splice**! Phải dùng phân từ hiện tại **C (“prioritizing”)** để tạo **cụm phân từ độc lập (nominative absolute phrase)** bổ nghĩa hợp lệ cho câu → Chọn C.',
        'Mẫu tuyệt chiêu Module 2 Hard: **[Mệnh đề độc lập], [danh từ sở hữu + V-ing / V-ed...]**. Khi thấy 3 đáp án là động từ chia thì và 1 đáp án là phân từ (*-ing*), hãy kiểm tra ngay bẫy Comma Splice!',
        [
            ('Comma Splice', '“was prioritizing” là động từ chia thì, biến vế sau thành mệnh đề độc lập thứ hai gây lỗi nối hai câu bằng dấu phẩy.'),
            ('Comma Splice', '“had prioritized” là động từ chia thì, gây lỗi Comma Splice tương tự.'),
            ('Đáp án đúng', '“prioritizing” là phân từ hiện tại tạo cụm bổ ngữ tuyệt đối (“their design prioritizing...”), nối mượt sau dấu phẩy không tạo Comma Splice.'),
            ('Comma Splice', '“prioritized” là động từ quá khứ chia thì chủ động với tân ngữ “airflow...”, tạo mệnh đề độc lập thứ hai gây Comma Splice.'),
        ],
    ),
    22: _meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'C',
        'Câu 1 phát biểu quy luật toán học tổng quát: qua nhiều lần thử, các biến ngẫu nhiên độc lập có xu hướng tụ quanh giá trị trung bình. Câu 2 đưa ra trường hợp minh họa cụ thể: tung đồng xu 1.000 lần thì có xác suất 99,7% ra từ 450 đến 550 mặt ngửa. Từ nối đưa ví dụ minh họa chuẩn xác là **C (“For instance,”)**.',
        'Khi câu 1 nêu định lý/nguyên lý tổng quát và câu 2 chuyển sang kịch bản cụ thể (“if you flip a coin 1,000 times...”), luôn chọn nhóm từ nối ví dụ (*For instance / For example*).',
        [
            ('Wrong Relationship', 'In addition = Ngoài ra — dùng để thêm một ý mới ngang hàng, không phải minh họa trực tiếp cho ý câu 1.'),
            ('Wrong Relationship', 'However = Tuy nhiên — sai vì câu 2 ủng hộ và minh họa chứ không tương phản với câu 1.'),
            ('Đáp án đúng', 'For instance = Ví dụ — nối hoàn hảo giữa nguyên lý toán học chung của Talagrand và ví dụ tung đồng xu 1.000 lần.'),
            ('Wrong Relationship', 'In comparison = So sánh với đó — không có hai đối tượng nào được đặt lên bàn cân so sánh ở đây.'),
        ],
    ),
    23: _meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'D',
        'Câu 1: Bản đồ địa hình (Topographic maps) hiển thị độ cao địa mạo **trên mực nước biển (“above sea level”)**. Câu 2: Bản đồ độ sâu đáy biển (Bathymetric maps) hiển thị độ cao địa mạo **dưới mặt biển (“below the sea”)**. Hai khái niệm đối lập trực tiếp → Chọn **D (“by contrast,”)**.',
        'Nhận diện cặp từ trái nghĩa song song (“above sea level” vs. “below the sea”) để chốt ngay từ nối đối lập “by contrast,”.',
        [
            ('Wrong Relationship', 'afterward = sau đó — chỉ trình tự thời gian, không phù hợp khi đối chiếu hai loại bản đồ.'),
            ('Wrong Relationship', 'in conclusion = tóm lại — câu 2 giới thiệu loại bản đồ khác chứ không tổng kết câu 1.'),
            ('Wrong Relationship', 'for example = ví dụ — bản đồ đáy biển không phải là một ví dụ của bản đồ địa hình trên mặt biển.'),
            ('Đáp án đúng', 'by contrast = ngược lại — làm nổi bật chính xác sự đối lập giữa địa hình trên mực nước biển và dưới đáy biển.'),
        ],
    ),
    24: _meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'B',
        'Câu 1 giới thiệu khái quát rằng “edge modeling” là một quy trình họa sĩ kỹ thuật số dùng khi tạo hình ảnh game. Câu 2 giải thích **cụ thể hơn** kỹ thuật đó làm gì (“piece together separate shapes to create 3D objects”). Quan hệ Khái quát → Chi tiết cụ thể đòi hỏi **B (“Specifically,”)**.',
        'Khi câu 2 lặp lại đúng thuật ngữ ở câu 1 (“edge modeling”) rồi mô tả chi tiết cách thức thực hiện nó, từ nối chuẩn là *Specifically,* (hoặc *In particular,*).',
        [
            ('Wrong Relationship', 'In addition = Ngoài ra — câu 2 giải thích sâu hơn cùng một quy trình chứ không thêm quy trình thứ hai.'),
            ('Đáp án đúng', 'Specifically = Cụ thể là — nối mượt giữa câu giới thiệu tổng quan và câu mô tả thao tác chi tiết của edge modeling.'),
            ('Wrong Relationship', 'Thus = Do đó — không có quan hệ nguyên nhân–kết quả giữa hai câu.'),
            ('Wrong Relationship', 'By comparison = So sánh lại — không có sự đối chiếu giữa hai kỹ thuật khác nhau.'),
        ],
    ),
    25: _meta(
        'Expression of Ideas', 'Transitions', 'Medium', 'D',
        'Câu 1 cho biết tỷ lệ đô thị hóa ở Indonesia tăng từ 53,3% lên 56,6% **trong giai đoạn 2015–2020**. Câu 2 cho biết tỷ lệ đô thị hóa trên toàn Đông Nam Á tăng 2,8 điểm phần trăm **trong đúng khoảng thời gian 5 năm đó (“in that five-year period”)**. Hai diễn biến xảy ra **đồng thời** → Chọn **D (“Concurrently,” = Đồng thời)**.',
        'Cẩn thận bẫy đảo chiều ở câu A (“For example”): Indonesia là ví dụ cho Đông Nam Á, chứ KHÔNG thể nói toàn Đông Nam Á là ví dụ cho riêng Indonesia! Dấu hiệu “in that five-year period” chỉ thẳng vào “Concurrently,”.',
        [
            ('Reversed Logic', 'For example bị ngược hướng: ta có thể nêu cả khu vực trước rồi lấy Indonesia làm ví dụ, nhưng không thể lấy cả khu vực Đông Nam Á làm ví dụ cho Indonesia.'),
            ('Wrong Time Sequence', 'Eventually = Cuối cùng/về sau — mâu thuẫn với cụm “in that five-year period” (cùng khoảng thời gian 2015–2020).'),
            ('Wrong Relationship', 'In other words = Nói cách khác — sai vì câu 2 đưa số liệu mới cho cả khu vực Đông Nam Á (+2,8 điểm %), không phải diễn đạt lại số liệu Indonesia.'),
            ('Đáp án đúng', 'Concurrently = Đồng thời — khớp chuẩn xác hai xu hướng diễn ra song song trong cùng giai đoạn 2015–2020.'),
        ],
    ),
    26: _meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Medium', 'D',
        'Mục tiêu: **đưa ra một nhận định khái quát về cách trật tự từ được sử dụng ở các ngôn ngữ** (“make a generalization about how word order is employed across languages”). Ghi chú cuối cho biết **87% ngôn ngữ trên thế giới thuộc dạng SVO hoặc SOV** — nghĩa là trong đại đa số ngôn ngữ, **chủ ngữ (S) đứng trước cả động từ (V) lẫn tân ngữ (O)**! Câu D tổng hợp xuất sắc dữ kiện này thành một nhận định khái quát chuẩn xác → Chọn D.',
        'Trong câu Synthesis cấp độ nâng cao, đáp án đúng thường **tổng hợp ngầm** hai ghi chú (SVO + SOV đều có S đứng đầu + chiếm 87% = “the majority”) thay vì chép nguyên văn câu chữ.',
        [
            ('Wrong Goal', 'Chỉ nói nhà loại hình học ngôn ngữ làm gì, không đưa ra khái quát về cách trật tự từ được dùng.'),
            ('Wrong Goal', 'Tương tự A, chỉ nhắc lại hoạt động phân tích của các nhà ngôn ngữ học.'),
            ('Wrong Goal', 'Chỉ nêu định nghĩa thuật ngữ “word order”, không phải nhận định khái quát về xu hướng sử dụng ở các ngôn ngữ.'),
            ('Đáp án đúng', 'Tổng hợp chính xác rằng 87% ngôn ngữ (SVO và SOV) đều đặt chủ ngữ đứng trước động từ và tân ngữ.'),
        ],
    ),
    27: _meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Hard', 'B',
        'Mục tiêu gồm **2 yêu cầu**: nêu (1) **điểm tương đồng giữa hai bộ kit** và (2) **ý nghĩa/tầm quan trọng của điểm tương đồng đó** (“emphasize the significance of a similarity between two of the kits”). Ghi chú cho thấy Pbact hiệu quả nhất vì là bộ kit *duy nhất* có cả sản lượng đủ cao lẫn độ tinh khiết gần mức lý tưởng 1,8; ngược lại CTAB 2X (độ tinh khiết 2,2 lệch xa 1,8) và Pplant (sản lượng quá thấp 12,5) cùng chung điểm yếu thiếu đạt chuẩn ở sản lượng hoặc độ tinh khiết, dẫn tới **ý nghĩa quan trọng** là cả hai bị đánh giá kém hiệu quả hơn Pbact → Chọn B.',
        'Ở câu cuối Module 2 Hard, luôn kiểm tra ĐỒNG THỜI tính chính xác so với ghi chú (loại ngay C và D bịa sai dữ kiện!) và cả hai vế của mục tiêu (“similarity” + “significance”).',
        [
            ('Missing Significance', 'Chỉ nêu một điểm chung vụn vặt về con số (>10 và >1,4) mà không chỉ ra ý nghĩa/hệ quả gì đối với hiệu quả chiết xuất.'),
            ('Đáp án đúng', 'Chính xác về dữ kiện, nêu rõ điểm chung giữa CTAB 2X và Pplant (cùng thiếu đạt chuẩn về yield hoặc purity) và nhấn mạnh ý nghĩa của nó (kém hiệu quả hơn Pbact).'),
            ('Factually False', 'Sai dữ kiện: độ tinh khiết của CTAB 2X là 2,2 (lệch 0,4 so với 1,8) còn Pbact là 1,6 (lệch 0,2), chúng không hề “equal in purity”.'),
            ('Factually False', 'Sai dữ kiện: ghi chú khẳng định Pbact có sản lượng “sufficiently high” (đủ cao), không hề bị “insufficient yields”.'),
        ],
    ),
}


# ============================================================================
# BUILD MODULES DYNAMICALLY FROM OCR DATA + PATCHES
# ============================================================================

MODULE_1_QUESTIONS = build_rw_questions_from_ocr(
    RAW_JSON,
    mod_prefix='may25_v2_m1',
    page_start=1,
    page_end=27,
    meta_map=M1_META,
    patches=M1_PATCHES,
)

MODULE_2_QUESTIONS = build_rw_questions_from_ocr(
    RAW_JSON,
    mod_prefix='may25_v2_m2h',
    page_start=28,
    page_end=54,
    meta_map=M2_META,
    patches=M2_PATCHES,
)


# ============================================================================
# COMPLETE BLUEBOOK REAL EXAM PAYLOAD (54 UNIQUE REAL QUESTIONS)
# ============================================================================

TEST_DATA = {
    'schemaVersion': 1,
    'mode': 'adaptive_mock',
    'section': 'rw',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT Quốc tế tháng 5/2025 (Int. Ver 2) — Đủ 2 Module (M1: 27 câu + M2: 27 câu)',
        'difficultyBadge': 'REAL EXAM • MAY 2025 INT.',
        'targetTimeMinutes': 64,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'real_may2025_v2_rw_m1',
        'title': 'Section 1, Module 1: Reading and Writing',
        'subtitle': 'May 2025 Int. Ver 2 Real Exam — Module 1 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'real_may2025_v2_rw_m2_hard',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'May 2025 Int. Ver 2 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'real_may2025_v2_rw_m2_lower',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'May 2025 Int. Ver 2 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': _clone_module_questions(
            MODULE_2_QUESTIONS,
            'may25_v2_m2h',
            'may25_v2_m2l',
        ),
    },
}


def verify_all():
    """Runs full structural, fidelity, watermark, answer/optionAnalysis, and Bluebook KaTeX checks."""
    from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json

    errors = []

    # 1. Exact counts (27 + 27 = 54 unique real questions; module2_lower mirrors Module 2)
    m1_qs = TEST_DATA['module1']['questions']
    m2h_qs = TEST_DATA['module2_hard']['questions']
    m2l_qs = TEST_DATA['module2_lower']['questions']
    if len(m1_qs) != 27:
        errors.append(f'Expected 27 Module 1 questions, got {len(m1_qs)}')
    if len(m2h_qs) != 27:
        errors.append(f'Expected 27 Module 2 (hard) questions, got {len(m2h_qs)}')
    if len(m2l_qs) != 27:
        errors.append(f'Expected 27 Module 2 (lower) questions, got {len(m2l_qs)}')
    if len(m1_qs) + len(m2h_qs) != 54:
        errors.append(f'Expected 54 total real questions, got {len(m1_qs) + len(m2h_qs)}')

    # Verify routingThreshold == 0, mode, section, targetTimeMinutes
    if TEST_DATA.get('mode') != 'adaptive_mock':
        errors.append(f"Expected mode='adaptive_mock', got {TEST_DATA.get('mode')}")
    if TEST_DATA.get('section') != 'rw':
        errors.append(f"Expected section='rw', got {TEST_DATA.get('section')}")
    if TEST_DATA['basicInfo'].get('routingThreshold') != 0:
        errors.append(f"Expected routingThreshold=0, got {TEST_DATA['basicInfo'].get('routingThreshold')}")
    if TEST_DATA['basicInfo'].get('targetTimeMinutes') != 64:
        errors.append(f"Expected targetTimeMinutes=64, got {TEST_DATA['basicInfo'].get('targetTimeMinutes')}")

    # 2. Unique IDs globally + sequential numbering + non-empty options + answer/optionAnalysis consistency
    all_ids = set()
    table_qs = []
    underline_qs = []
    for mod_key, qs in [('module1', m1_qs), ('module2_hard', m2h_qs), ('module2_lower', m2l_qs)]:
        for idx, q in enumerate(qs, start=1):
            qid = q['id']
            if qid in all_ids:
                errors.append(f'Duplicate global ID: {qid}')
            all_ids.add(qid)
            if q['number'] != idx:
                errors.append(f'{mod_key} Q{idx}: wrong number field {q["number"]}')

            opts = q.get('options') or []
            if len(opts) != 4 or any(not str(o.get('text') or '').strip() for o in opts):
                errors.append(f'{qid}: expected 4 non-empty options')

            ans = q['correctAnswer']
            exp = q.get('explanation') or {}
            oa = exp.get('optionAnalysis') or {}
            if set(oa.keys()) != {'A', 'B', 'C', 'D'}:
                errors.append(f'{qid}: optionAnalysis missing keys {set(oa.keys())}')
            correct_keys = [k for k, v in oa.items() if v.get('status') == 'correct']
            trap_keys = [k for k, v in oa.items() if v.get('status') == 'trap']
            if correct_keys != [ans] or len(trap_keys) != 3:
                errors.append(
                    f'{qid}: optionAnalysis status mismatch (ans={ans}, correct={correct_keys}, traps={trap_keys})'
                )
            for k, v in oa.items():
                if not (v.get('reasonVi') or '').strip():
                    errors.append(f'{qid}: empty reasonVi for option {k}')
            if not (exp.get('summaryVi') or '').strip():
                errors.append(f'{qid}: empty summaryVi')
            if not (exp.get('keyTakeaway') or '').strip():
                errors.append(f'{qid}: empty keyTakeaway')

            # Fidelity checks: tables, graphs, and underlines must be present when referenced
            q_lower = (q['questionHtml'] or '').lower()
            stim = q['stimulusHtml'] or ''
            if 'table' in q_lower:
                if '<table' not in stim.lower():
                    errors.append(f'{qid}: question references table but stimulusHtml lacks <table>')
                elif mod_key != 'module2_lower':
                    table_qs.append(qid)
            if 'graph' in q_lower and '<svg' not in stim.lower():
                errors.append(f'{qid}: question references graph but stimulusHtml lacks <svg>')
            if 'underlined' in q_lower:
                if '<u>' not in stim.lower():
                    errors.append(f'{qid}: question references underlined text but stimulusHtml lacks <u>')
                elif mod_key != 'module2_lower':
                    underline_qs.append(qid)

            # Check for leftover OCR chrome/artifacts in prompt or stimulus
            if re.search(r'Mark\s+for\s+Review|vark\s+for\s+Review|ark\s+for\s+Review|vor\s+for\s+Review', q['questionHtml'], re.I):
                errors.append(f'{qid}: leftover Review chrome in questionHtml: {q["questionHtml"]}')
            if re.search(r'^<p>(\[|\&|Sal\b|55\}|5\}|Joi\)|I=\)|5\s+B|= BE)', stim):
                errors.append(f'{qid}: leftover leading OCR artifact in stimulusHtml: {stim[:60]}')

    # Verify module2_lower mirrors module2_hard verbatim (aside from IDs)
    for qh, ql in zip(m2h_qs, m2l_qs):
        for field in ('number', 'domain', 'skill', 'stimulusHtml', 'questionHtml', 'options', 'correctAnswer', 'explanation'):
            if qh[field] != ql[field]:
                errors.append(f'module2_lower Q{qh["number"]} differs from module2_hard on field {field}')

    # 3. Zero watermarks & zero raw ___blank artifacts across entire JSON
    serialized = json.dumps(TEST_DATA, ensure_ascii=False)
    if re.search(r'@dsatuz|dsatuz|@d7sat|d7sat|t\.me/', serialized, re.IGNORECASE):
        errors.append('Found watermark string in TEST_DATA!')
    if re.search(r'_{3,}blank', serialized, re.IGNORECASE):
        errors.append('Found unconverted ___blank artifact in TEST_DATA!')

    # 4. Official Bluebook pipeline validator (schema + Node KaTeX check)
    pipeline_errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    errors.extend(pipeline_errs)

    # Summary stats
    m1_dist = {c: sum(1 for q in m1_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    m2_dist = {c: sum(1 for q in m2h_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    print(f'[{TEST_CODE}] {TEST_TITLE}')
    print(f'  Module 1: {len(m1_qs)} Qs | Keys: {m1_dist}')
    print(f'  Module 2: {len(m2h_qs)} Qs | Keys: {m2_dist} (mirrored to module2_lower: {len(m2l_qs)} Qs)')
    print(f'  Total unique real Qs: {len(m1_qs) + len(m2h_qs)} | Global unique IDs: {len(all_ids)}')
    print(f'  Tables verified: {len(table_qs)} ({", ".join(table_qs)})')
    print(f'  Underlines verified: {len(underline_qs)} ({", ".join(underline_qs)})')

    if errors:
        print(f'  [FAILED] {len(errors)} error(s):')
        for e in errors:
            print(f'    - {e}')
        return False

    print('  [PASS] 0 errors — Bluebook schema, KaTeX, OCR patches & 2-pass audit verified!')
    return True


if __name__ == '__main__':
    ok = verify_all()
    sys.exit(0 if ok else 1)
