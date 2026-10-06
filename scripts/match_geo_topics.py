import json

with open('scripts/geo_transcriptions.json', encoding='utf-8') as f:
    data = json.load(f)

syllabus = [
    ("1.1", "Physical geography", "Changing river environments", "The main hydrological characteristics and processes that operate in rivers and drainage basins"),
    ("1.2", "Physical geography", "Changing river environments", "The main landforms associated with these processes"),
    ("1.3", "Physical geography", "Changing river environments", "Rivers present opportunities and hazards for people"),
    ("2.1", "Physical geography", "Changing coastal environments", "The physical processes that shape the coast"),
    ("2.2", "Physical geography", "Changing coastal environments", "The main landforms associated with these processes"),
    ("2.3", "Physical geography", "Changing coastal environments", "Coasts present opportunities and hazards for people"),
    ("3.1", "Physical geography", "Changing ecosystems", "The characteristics of the Antarctic ecosystem"),
    ("3.2", "Physical geography", "Changing ecosystems", "The threats to the Antarctic ecosystem and how they can be managed"),
    ("3.3", "Physical geography", "Changing ecosystems", "The characteristics of the tropical rainforest ecosystem"),
    ("3.4", "Physical geography", "Changing ecosystems", "The threats to the tropical rainforest ecosystem and how they can be managed"),
    ("4.1", "Physical geography", "Tectonic hazards", "The structure of the Earth and the distribution of earthquakes and volcanoes"),
    ("4.2", "Physical geography", "Tectonic hazards", "The processes and features associated with earthquakes and volcanoes"),
    ("4.3", "Physical geography", "Tectonic hazards", "The impact of tectonic hazards"),
    ("4.4", "Physical geography", "Tectonic hazards", "Managing the impacts of tectonic hazards"),
    ("5.1", "Physical geography", "Climate change", "The natural and human causes of climate change"),
    ("5.2", "Physical geography", "Climate change", "The impacts of climate change at a range of geographic scales"),
    ("5.3", "Physical geography", "Climate change", "The responses to climate change"),
    ("6.1", "Human geography", "Changing populations", "Populations grow and decline"),
    ("6.2", "Human geography", "Changing populations", "Population structures change over time"),
    ("6.3", "Human geography", "Changing populations", "The causes and impacts of international migration"),
    ("7.1", "Human geography", "Changing towns and cities", "Where people live"),
    ("7.2", "Human geography", "Changing towns and cities", "The opportunities and challenges of urbanisation"),
    ("7.3", "Human geography", "Changing towns and cities", "The management of urban growth"),
    ("8.1", "Human geography", "Development", "Measuring development"),
    ("8.2", "Human geography", "Development", "The world is developing unevenly"),
    ("8.3", "Human geography", "Development", "Achieving sustainable development"),
    ("9.1", "Human geography", "Changing economies", "Changing employment structures"),
    ("9.2", "Human geography", "Changing economies", "The impact of globalisation and the role of transnational corporations"),
    ("9.3", "Human geography", "Changing economies", "Tourism is a growing industry"),
    ("10.1", "Human geography", "Resource provision", "How our food is produced"),
    ("10.2", "Human geography", "Resource provision", "The global patterns of food supply and demand"),
    ("10.3", "Human geography", "Resource provision", "The challenges of food supply"),
    ("10.4", "Human geography", "Resource provision", "How our energy is produced"),
    ("10.5", "Human geography", "Resource provision", "The global patterns of energy supply and demand"),
    ("10.6", "Human geography", "Resource provision", "The impacts of energy production")
]

print("Total topics in syllabus:", len(syllabus))
for code, group, topic, title in syllabus:
    print(f"[{code}] {group} -> {topic}: {title}")
