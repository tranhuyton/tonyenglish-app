import json

manifest_updates = {
    '7_2': {
        "intro": {"start": 0, "end": 2},
        "sec_opportunities": {"start": 1, "end": 2},
        "sec_hic_challenges": {"start": 3, "end": 6},
        "sec_lic_challenges": {"start": 7, "end": 8},
        "sec_squatter_management": {"start": 9, "end": 12},
        "card_exam_strategy": {"start": 13, "end": 13}
    },
    '7_3': {
        "intro": {"start": 0, "end": 2},
        "sec_housing_brownfield": {"start": 1, "end": 2},
        "sec_sustainable_cities": {"start": 3, "end": 4},
        "sec_transport_strategies": {"start": 5, "end": 6},
        "sec_shanghai_casestudy": {"start": 7, "end": 8},
        "sec_delhi_hazards": {"start": 9, "end": 10},
        "card_exam_strategy": {"start": 11, "end": 11}
    },
    '8_1': {
        "intro": {"start": 0, "end": 2},
        "sec_what_is_dev": {"start": 1, "end": 2},
        "sec_single_indicators": {"start": 3, "end": 5},
        "sec_hdi": {"start": 6, "end": 7},
        "sec_brandt_multipolar": {"start": 8, "end": 10},
        "card_exam_summary": {"start": 11, "end": 11}
    },
    '8_2': {
        "intro": {"start": 0, "end": 1},
        "sec_uneven_continuum": {"start": 1, "end": 1},
        "sec_underlying_causes": {"start": 2, "end": 4},
        "sec_dev_theories": {"start": 5, "end": 6},
        "sec_poverty_cycle": {"start": 7, "end": 8},
        "card_exam_summary": {"start": 9, "end": 9}
    },
    '8_3': {
        "intro": {"start": 0, "end": 1},
        "sec_three_pillars": {"start": 1, "end": 1},
        "sec_environmental_sustainability": {"start": 2, "end": 3},
        "sec_aid_microfinance": {"start": 4, "end": 5},
        "sec_indonesia_casestudy": {"start": 6, "end": 7},
        "card_exam_summary": {"start": 8, "end": 8}
    }
}

for code, ms in manifest_updates.items():
    mpath = f"public/audio/lectures/geography/{code}/manifest.json"
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    
    m['majorSections'] = ms
    
    with open(mpath, 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=2, ensure_ascii=False)
        
    print(f"Updated majorSections dictionary in {code}/manifest.json")
