"""
Final Fantasy X Enemy Database
Data extracted from Enemy entry pages from the FFX Wiki
Contains comprehensive enemy information including Zanmato levels

NOTE: Key enemies (bosses, Dark Aeons, Monster Arena) have full data including
HP, stats, drops, immunities, etc. Other enemies have basic structure and can
be expanded with full data from the guide as needed.
"""


ENEMIES = {
    "Achelous": {
        "zanmato_lv": 1,
        "hp": 5100,
        "hp_overkill": 7500,
        "mp": 85,
        "ap": 730,
        "ap_overkill": 1460,
        "location": "Gagazet Caves",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 33, "mag": 52, "def": 10, "mdef": 20,
            "acc": 1, "agl": 0, "eva": 0, "luck": 15
        },
        "gil": 420,
        "steal": {"common": "Water Gem x2", "rare": "Healing Spring"},
        "bribe": ["Healing Spring x16 (127,500 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%", "Magic +10%"],
        "armor_abilities": ["MP +10%", "Auto-Med"],
        "immunities": ["Slow", "Threaten"],
        "status_resistances": {
            "Sleep": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Achelous_from_FFX.webp"
    },


    "Adamantoise": {
        "zanmato_lv": 3,
        "hp": 54400,
        "hp_overkill": 11036,
        "mp": 40,
        "ap": 12500,
        "ap_overkill": 18750,
        "location": "Inside Sin, Omega Ruins",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 38, "mag": 31, "def": 90, "mdef": 90,
            "acc": 1, "agl": 15, "eva": 0, "luck": 15
        },
        "gil": 2200,
        "steal": {"common": "Healing Water", "rare": "Stamina Tablet"},
        "bribe": ["Special Sphere x6 (1,360,000 gil)"],
        "drop": {"common": "Power Sphere x2", "rare": "Power Sphere x4"},
        "equipment_drop": "3-4 slots, 0-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Half MP Cost"],
        "armor_abilities": ["SOS Shell", "SOS Protect", "HP +20%"],
        "immunities": ["Slow", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Demi", "Delay"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Poison": "75 (5 HP/turn)",
            "Petrify": 80,
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire"]
        },
        "image": "./images/Adamantoise-enemy-ffx.webp"
    },


    "Aerouge": {
        "zanmato_lv": 1,
        "hp": 200,
        "hp_overkill": 300,
        "mp": 220,
        "ap": 92,
        "ap_overkill": 184,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 1, "mag": 16, "def": 1, "mdef": 120,
            "acc": 1, "agl": 0, "eva": 13, "luck": 15
        },
        "gil": 144,
        "steal": {"common": "Electro Marble", "rare": "Lightning Marble"},
        "bribe": ["Lightning Marble x4 (5,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike", "Distill Mana"],
        "armor_abilities": ["Lightning Ward", "Lightningproof", "Magic Def +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Aerouge_from_FFX.webp"
    },


    "Ahriman": {
        "zanmato_lv": 1,
        "hp": 2800,
        "hp_overkill": 4200,
        "mp": 400,
        "ap": 2200,
        "ap_overkill": 4400,
        "location": "Mt. Gagazet, Zanarkand, Inside Sin",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 1, "mag": 38, "def": 1, "mdef": 180,
            "acc": 1, "agl": 0, "eva": 18, "luck": 15
        },
        "gil": 650,
        "steal": {"common": "Musk x2", "rare": "Musk x3"},
        "bribe": ["Farplane Wind x6 (70,000 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Strength +5%", "Magic +5%", "Distill Speed"],
        "armor_abilities": ["Confuse Ward"],
        "immunities": ["Darkness"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ahriman-ffx.webp"
    },


    "Alcyone": {
        "zanmato_lv": 1,
        "hp": 430,
        "hp_overkill": 645,
        "mp": 42,
        "ap": 310,
        "ap_overkill": 620,
        "location": "Bikanel",
        "monster_arena": "Bikanel",
        "stats": {
            "str": 16, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 0, "eva": 15, "luck": 15
        },
        "gil": 240,
        "steal": {"common": "Smoke Bomb", "rare": "Smoke Bomb x2"},
        "bribe": ["Mega Phoenix x2 (10,750 gil)"],
        "drop": {"common": "Speed Sphere x1, Al Bhed Potion x1", "rare": "Speed Sphere x1, Al Bhed Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Sensor", "Piercing", "Distill Speed"],
        "armor_abilities": ["Dark Ward", "Magic Def +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Alcyone_from_FFX.webp"
    },


    "Anacondaur": {
        "zanmato_lv": 1,
        "hp": 5800,
        "hp_overkill": 4060,
        "mp": 70,
        "ap": 1380,
        "ap_overkill": 2070,
        "location": "Calm Lands",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 27, "mag": 48, "def": 1, "mdef": 1,
            "acc": 1, "agl": 16, "eva": 0, "luck": 15
        },
        "gil": 750,
        "steal": {"common": "Petrify Grenade", "rare": "Petrify Grenade x2"},
        "bribe": ["Healing Water x16 (145,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Stonetouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Stone Ward"],
        "immunities": ["Petrify", "Slow"],
        "status_resistances": {
            "Sleep": 95,
            "Poison": "25 (25 HP/turn)",
            "Zombie": 25,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Lightning"]
        },
        "image": "./images/Anacondaur_from_FFX.webp"
    },


    "Aqua Flan": {
        "zanmato_lv": 1,
        "hp": 2025,
        "hp_overkill": 3038,
        "mp": 1,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Via Purifico (Land)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 22, "def": 100, "mdef": 1,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 340,
        "steal": {"common": "Fish Scale x2", "rare": "Dragon Scale x2"},
        "bribe": ["Water Gem x15 (50,625 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Distill Mana"],
        "armor_abilities": ["Water Ward"],
        "immunities": ["Berserk", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": ["Water"]
        },
        "image": "./images/Aqua_Flan_from_FFX.webp"
    },


    "Bandersnatch": {
        "zanmato_lv": 1,
        "hp": 1800,
        "hp_overkill": 2700,
        "mp": 75,
        "ap": 820,
        "ap_overkill": 1640,
        "location": "Mt. Gagazet",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 32, "mag": 1, "def": 1, "mdef": 180,
            "acc": 1, "agl": 32, "eva": 11, "luck": 15
        },
        "gil": 880,
        "steal": {"common": "Dream Powder x2", "rare": "Dream Powder x3"},
        "bribe": ["Dream Powder x20 (45,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Silence Ward", "Sleep Ward"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bandersnatch_from_FFX.webp"
    },


    "Barbatos": {
        "zanmato_lv": 2,
        "hp": 95000,
        "hp_overkill": 13560,
        "mp": 480,
        "ap": 17500,
        "ap_overkill": 26250,
        "location": "Inside Sin",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 42, "mag": 38, "def": 100, "mdef": 60,
            "acc": 1, "agl": 28, "eva": 0, "luck": 15
        },
        "gil": 1550,
        "steal": {"common": "Star Curtain", "rare": "Blessed Gem"},
        "bribe": ["Teleport Sphere x20 (2,375,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Return Sphere x1"},
        "equipment_drop": "2-4 slots, 1 ability, 50% chance",
        "weapon_abilities": ["Piercing"],
        "armor_abilities": ["HP +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Power Break", "Magic Break", "Mental Break", "Threaten", "Death", "Delay", "Berserk"],
        "status_resistances": {
            "Zombie": 90,
            "Armor Break": 50,
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Barbatos-enemy-ffx.webp"
    },


    "Bashura": {
        "zanmato_lv": 1,
        "hp": 17000,
        "hp_overkill": 6972,
        "mp": 5,
        "ap": 1860,
        "ap_overkill": 3720,
        "location": "Mt. Gagazet, Zanarkand",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 34, "mag": 1, "def": 45, "mdef": 1,
            "acc": 1, "agl": 16, "eva": 0, "luck": 15
        },
        "gil": 730,
        "steal": {"common": "Soul Spring", "rare": "Soul Spring x2"},
        "bribe": ["Stamina Spring x80 (425,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%", "Counterattack"],
        "armor_abilities": ["SOS Haste", "HP +10%"],
        "immunities": ["Power Break", "Death"],
        "status_resistances": {
            "Sleep": 80,
            "Darkness": 95,
            "Poison": "25 (25 HP/turn)",
            "Petrify": 50,
            "Zombie": 25,
            "Threaten": 20,
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/FFX_bashura.webp"
    },


    "Basilisk": {
        "zanmato_lv": 1,
        "hp": 2025,
        "hp_overkill": 924,
        "mp": 20,
        "ap": 140,
        "ap_overkill": 210,
        "location": "Djose Highroad",
        "monster_arena": "Djose Road",
        "stats": {
            "str": 14, "mag": 35, "def": 1, "mdef": 1,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 125,
        "steal": {"common": "Petrify Grenade", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x24 (50,625 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x2"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Stonetouch", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Stone Ward", "MP +5%"],
        "immunities": ["Petrify"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (5 HP/turn)",
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Lightning"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Basilisk-enemy-ffx.webp"
    },


    "Bat Eye": {
        "zanmato_lv": 1,
        "hp": 380,
        "hp_overkill": 570,
        "mp": 280,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Via Purifico (Land)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 29, "def": 1, "mdef": 120,
            "acc": 1, "agl": 16, "eva": 13, "luck": 15
        },
        "gil": 320,
        "steal": {"common": "Hi-Potion", "rare": "Silence Grenade x2"},
        "bribe": ["Silence Grenade x12 (9,500 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Strength +3%", "Strength +5%", "Magic +3%", "Magic +5%", "Distill Speed"],
        "armor_abilities": ["Confuse Ward", "MP +5%"],
        "immunities": ["Capture"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/BatEye-ffx.webp"
    },


    "Behemoth": {
        "zanmato_lv": 2,
        "hp": 23000,
        "hp_overkill": 6972,
        "mp": 480,
        "ap": 6540,
        "ap_overkill": 9810,
        "location": "Mt. Gagazet, Zanarkand Ruins",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 43, "mag": 37, "def": 1, "mdef": 1,
            "acc": 1, "agl": 23, "eva": 0, "luck": 15
        },
        "gil": 1350,
        "steal": {"common": "Ether", "rare": "Mana Tablet"},
        "bribe": ["Lv. 2 Key Sphere x30 (575,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Zombietouch", "Strength +5%", "Magic +5%", "SOS Overdrive"],
        "armor_abilities": ["SOS Shell", "SOS Protect", "SOS Reflect"],
        "immunities": ["Silence", "Darkness", "Petrify", "Slow", "Armor Break", "Mental Break", "Threaten", "Death", "Delay"],
        "status_resistances": {
            "Sleep": 80,
            "Poison": "50 (25 HP/turn)",
            "Zombie": 25,
            "Power Break": 80,
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Behemoth_from_FFX.webp"
    },

    "Behemoth King": {
        "zanmato_lv": 2,
        "hp": 67500,
        "hp_overkill": 13560,
        "mp": 700,
        "ap": 16800,
        "ap_overkill": 25200,
        "location": "Inside Sin",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 46, "mag": 44, "def": 25, "mdef": 25,
            "acc": 1, "agl": 27, "eva": 0, "luck": 15
        },
        "gil": 1850,
        "steal": {"common": "Healing Spring", "rare": "Twin Stars x2"},
        "bribe": ["Three Stars x14 (1,687,500 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Zombietouch", "SOS Overdrive"],
        "armor_abilities": ["SOS Shell", "SOS Protect", "SOS Reflect"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Armor Break", "Mental Break", "Threaten", "Death", "Delay", "Berserk"],
        "status_resistances": {
            "Power Break": 80,
            "Magic Break": 80,
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Behemoth_King_from_FFX.webp"
    },

    "Bite Bug": {
        "zanmato_lv": 1,
        "hp": 200,
        "hp_overkill": 300,
        "mp": 10,
        "ap": 40,
        "ap_overkill": 80,
        "location": "Djose Highroad, Moonflow",
        "monster_arena": "Djose Road",
        "stats": {
            "str": 13, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 15, "eva": 12, "luck": 15
        },
        "gil": 62,
        "steal": {"common": "Antidote", "rare": "Poison Fang"},
        "bribe": ["Poison Fang x2 (5,000 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Speed"],
        "armor_abilities": ["Poison Ward", "MP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bite_Bug_from_FFX.webp"
    },

    "Black Element": {
        "zanmato_lv": 1,
        "hp": 7600,
        "hp_overkill": 11400,
        "mp": 500,
        "ap": 3150,
        "ap_overkill": 6300,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 1, "mag": 33, "def": 250, "mdef": 30,
            "acc": 0, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 1040,
        "steal": {"common": "Hi-Potion", "rare": "Shining Gem x4"},
        "bribe": ["Blk Magic Sphere x2 (190,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Return Sphere x1"},
        "equipment_drop": "2-4 slots, 0-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Waterstrike", "Icestrike", "Distill Mana"],
        "armor_abilities": ["Fire Ward", "Fireproof", "Lightning Ward", "Lightningproof", "Waterproof", "Ice Ward", "Iceproof"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Sensor", "Scan"],
        "status_resistances": {
            "Silence": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Black_Element_from_FFX.webp"
    },

    "Blue Element": {
        "zanmato_lv": 1,
        "hp": 1500,
        "hp_overkill": 2250,
        "mp": 220,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Macalania Woods",
        "monster_arena": "Macalania",
        "stats": {
            "str": 1, "mag": 27, "def": 120, "mdef": 1,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 180,
        "steal": {"common": "Fish Scale x2", "rare": "Fish Scale x3"},
        "bribe": ["Water Gem x9 (37,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 0-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Distill Mana"],
        "armor_abilities": ["Water Ward", "Waterproof"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie"],
        "status_resistances": {
            "Silence": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire", "Ice"],
            "immune": [],
            "absorb": ["Water"]
        },
        "image": "./images/Blue_Element_from_FFX.webp"
    },

    "Bomb (Mi\'ihen Highroad)": {
        "zanmato_lv": 1,
        "hp": 850,
        "hp_overkill": 560,
        "mp": 30,
        "ap": 22,
        "ap_overkill": 44,
        "location": "Mi'ihen Highroad, Mushroom Rock Road",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 19, "mag": 20, "def": 1, "mdef": 1,
            "acc": 1, "agl": 11, "eva": 0, "luck": 15
        },
        "gil": 70,
        "steal": {"common": "Bomb Fragment x2", "rare": "Bomb Fragment x3"},
        "bribe": ["Bomb Core x16 (21,250 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 15.63% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Distill Power"],
        "armor_abilities": ["Fire Ward"],
        "immunities": ["Sleep", "Threaten"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bomb_from_FFX.webp"
    },

    "Bomb (Home/Airship)": {
        "zanmato_lv": 1,
        "hp": 2200,
        "hp_overkill": 1432,
        "mp": 45,
        "ap": 620,
        "ap_overkill": 1240,
        "location": "Home, Airship",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 17, "def": 1, "mdef": 1,
            "acc": 1, "agl": 11, "eva": 0, "luck": 15
        },
        "gil": 470,
        "steal": {"common": "Bomb Core x2", "rare": "Bomb Core x3"},
        "bribe": ["Fire Gem x14 (55,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Distill Power"],
        "armor_abilities": ["Fire Ward"],
        "immunities": ["Sleep", "Threaten", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bomb_from_FFX.webp"
    },

    "Buer": {
        "zanmato_lv": 1,
        "hp": 230,
        "hp_overkill": 345,
        "mp": 250,
        "ap": 92,
        "ap_overkill": 184,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 1, "mag": 22, "def": 1, "mdef": 120,
            "acc": 1, "agl": 12, "eva": 12, "luck": 15
        },
        "gil": 132,
        "steal": {"common": "Hi-Potion", "rare": "Musk"},
        "bribe": ["Musk x2 (5,750 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Strength +5%", "Magic +5%", "Distill Speed"],
        "armor_abilities": ["Confuse Ward", "MP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25% max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Buer_from_FFX.webp"
    },

    "Bunyip": {
        "zanmato_lv": 1,
        "hp": 400,
        "hp_overkill": 600,
        "mp": 15,
        "ap": 48,
        "ap_overkill": 96,
        "location": "Djose Highroad, Moonflow",
        "monster_arena": "Djose Road",
        "stats": {
            "str": 22, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 97,
        "steal": {"common": "Hi-Potion", "rare": "Hypello Potion"},
        "bribe": ["Hypello Potion x16 (10,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Berserk Ward", "Defense +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice", "Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bunyip-enemy-ffx.webp"
    },

    "Cactuar": {
        "zanmato_lv": 2,
        "hp": 800,
        "hp_overkill": 1200,
        "mp": 1,
        "ap": 8000,
        "ap_overkill": 12000,
        "location": "Cactuar Nation",
        "monster_arena": "Bikanel",
        "stats": {
            "str": 23, "mag": 1, "def": 1, "mdef": 255,
            "acc": 1, "agl": 24, "eva": 20, "luck": 15
        },
        "gil": 1500,
        "steal": {"common": "Chocobo Feather", "rare": "Chocobo Wing"},
        "bribe": None,
        "drop": {"common": "Speed Sphere x2", "rare": "Speed Sphere x3"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Initiative"],
        "armor_abilities": ["HP Stroll", "MP Stroll", "HP +10%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Demi", "Bribe", "Delay", "Berserk"],
        "status_resistances": {
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Cactuar_FFX.webp"
    },

    "Cave Iguion": {
        "zanmato_lv": 1,
        "hp": 550,
        "hp_overkill": 825,
        "mp": 1,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Via Purifico (Land)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 24, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 21, "eva": 9, "luck": 15
        },
        "gil": 300,
        "steal": {"common": "Soft", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x6 (13,750 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward", "Defense +5%"],
        "immunities": ["Capture"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Cave_Iguion.webp"
    },

    "Chimera (Macalania Woods)": {
        "zanmato_lv": 1,
        "hp": 5250,
        "hp_overkill": 1432,
        "mp": 130,
        "ap": 1220,
        "ap_overkill": 1830,
        "location": "Macalania Woods",
        "monster_arena": "Macalania",
        "stats": {
            "str": 25, "mag": 22, "def": 1, "mdef": 1,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 970,
        "steal": {"common": "Arctic Wind", "rare": "Lightning Marble"},
        "bribe": ["Mana Tablet x10 (131,250 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x2"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Magic +5%", "Magic +10%", "Distill Mana"],
        "armor_abilities": ["Magic Def +10%"],
        "immunities": ["Sleep"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Poison": "0 (10 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Chimera-enemy-ffx.webp"
    },

    "Chimera (Home/Airship)": {
        "zanmato_lv": 1,
        "hp": 9000,
        "hp_overkill": 1432,
        "mp": 200,
        "ap": 2000,
        "ap_overkill": 3000,
        "location": "Home",
        "monster_arena": "Macalania",
        "stats": {
            "str": 30, "mag": 25, "def": 1, "mdef": 1,
            "acc": 1, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 980,
        "steal": {"common": "Arctic Wind x3", "rare": "Lightning Marble x3"},
        "bribe": ["Underdog's Secret x15 (225,000 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x2"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Magic +5%", "Magic +10%", "Distill Mana"],
        "armor_abilities": ["Magic Def +10%"],
        "immunities": ["Sleep", "Poison"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Chimera-enemy-ffx.webp"
    },

    "Chimera Brain": {
        "zanmato_lv": 1,
        "hp": 9800,
        "hp_overkill": 4060,
        "mp": 250,
        "ap": 1200,
        "ap_overkill": 1800,
        "location": "Calm Lands",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 34, "mag": 32, "def": 10, "mdef": 10,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 1000,
        "steal": {"common": "Ice Gem", "rare": "Lightning Gem x2"},
        "bribe": ["Lv. 4 Key Sphere x2 (245,000 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x2"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Magic +5%", "Magic +10%", "Distill Mana"],
        "armor_abilities": ["Magic Def +10%"],
        "immunities": ["Sleep", "Death"],
        "status_resistances": {
            "Silence": 95,
            "Poison": "25 (10 HP/turn)",
            "Zombie": 25,
            "Magic Break": 25,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Chimera_Brain_from_FFX.webp"
    },

    "Coeurl": {
        "zanmato_lv": 1,
        "hp": 6000,
        "hp_overkill": 4060,
        "mp": 480,
        "ap": 1300,
        "ap_overkill": 1950,
        "location": "Calm Lands, Cavern of the Stolen Fayth",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 38, "mag": 26, "def": 1, "mdef": 40,
            "acc": 1, "agl": 0, "eva": 0, "luck": 15
        },
        "gil": 1100,
        "steal": {"common": "Mana Spring", "rare": "Mana Spring"},
        "bribe": ["Friend Sphere x2 (150,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x2"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Deathtouch", "Strength +5%", "Magic +5%", "Magic +10%"],
        "armor_abilities": ["Death Ward", "Defense +10%", "Magic Def +10%"],
        "immunities": ["Petrify", "Threaten"],
        "status_resistances": {
            "Silence": 95,
            "Sleep": 95,
            "Poison": "25 (25 HP/turn)",
            "Zombie": 25,
            "Magic Break": 25,
            "Death": 25,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Ice", "Lightning"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Coeurl-enemy-ffx.webp"
    },

    "Coeurlregina": {
        "zanmato_lv": 4,
        "hp": 380000,
        "hp_overkill": 10000,
        "mp": 80,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 1, "mag": 70, "def": 40, "mdef": 40,
            "acc": 100, "agl": 75, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Farplane Wind x2", "rare": "Blessed Gem x1"},
        "bribe": None,
        "drop": {"common": "Shining Gem x3", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Deathstrike", "Double AP"],
        "armor_abilities": ["Deathproof", "Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Master_Coeurl_from_FFX.webp"
    },

    "Condor": {
        "zanmato_lv": 1,
        "hp": 95,
        "hp_overkill": 143,
        "mp": 15,
        "ap": 2,
        "ap_overkill": 4,
        "location": "Besaid",
        "monster_arena": "Besaid",
        "stats": {
            "str": 9, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 0, "eva": 10, "luck": 15
        },
        "gil": 12,
        "steal": {"common": "Phoenix Down", "rare": "Smoke Bomb"},
        "bribe": ["Smoke Bomb x3 (2,375 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Sensor", "Piercing", "Distill Speed"],
        "armor_abilities": ["Dark Ward", "Magic Def +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Condor_from_FFX.webp"
    },

    "Dark Element": {
        "zanmato_lv": 1,
        "hp": 1800,
        "hp_overkill": 2700,
        "mp": 280,
        "ap": 810,
        "ap_overkill": 1620,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 1, "mag": 30, "def": 190, "mdef": 1,
            "acc": 1, "agl": 0, "eva": 0, "luck": 15
        },
        "gil": 520,
        "steal": {"common": "Shining Thorn", "rare": "Shining Thorn x2"},
        "bribe": ["Return Sphere x3 (45,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1 slot, 0-1 ability, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Waterstrike", "Icestrike", "Distill Mana"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Lightningproof", "Water Ward", "Ice Ward"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie"],
        "status_resistances": {
            "Silence": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Element_from_FFX.webp"
    },

    "Dark Flan": {
        "zanmato_lv": 1,
        "hp": 12800,
        "hp_overkill": 19200,
        "mp": 250,
        "ap": 3750,
        "ap_overkill": 7500,
        "location": "Mt. Gagazet, Zanarkand",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 1, "mag": 30, "def": 220, "mdef": 200,
            "acc": 1, "agl": 11, "eva": 0, "luck": 15
        },
        "gil": 1080,
        "steal": {"common": "Star Curtain", "rare": "Star Curtain x2"},
        "bribe": ["Wht Magic Sphere x2 (320,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x2"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Magic +5%", "Magic +10%", "Distill Mana"],
        "armor_abilities": ["MP +10%", "MP +20%"],
        "immunities": ["Sleep", "Poison", "Petrify", "Death", "Provoke", "Delay", "Berserk"],
        "status_resistances": {
            "Silence": 80,
            "Darkness": 20,
            "Slow": 95,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Flan_from_FFX.webp"
    },

    "Defender": {
        "zanmato_lv": 1,
        "hp": 12000,
        "hp_overkill": 4060,
        "mp": 1,
        "ap": 2700,
        "ap_overkill": 4050,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 40, "mag": 5, "def": 1, "mdef": 1,
            "acc": 1, "agl": 11, "eva": 0, "luck": 15
        },
        "gil": 1300,
        "steal": {"common": "Lunar Curtain", "rare": "Lunar Curtain x2"},
        "bribe": ["Stamina Tablet x20 (300,000 gil)"],
        "drop": {"common": "Power Sphere x2", "rare": "Power Sphere x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Strength +3%", "Strength +5%", "Distill Power"],
        "armor_abilities": ["SOS Protect", "Defense +10%"],
        "immunities": ["Sleep", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Threaten", "Death", "Capture"],
        "status_resistances": {
            "Darkness": 95,
            "Doom": "0 (10 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Defender-enemy-ffx.webp"
    },

    "Defender Z": {
        "zanmato_lv": 1,
        "hp": 42300,
        "hp_overkill": 8848,
        "mp": 1,
        "ap": 6000,
        "ap_overkill": 9000,
        "location": "Zanarkand Dome, Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 45, "mag": 5, "def": 70, "mdef": 70,
            "acc": 1, "agl": 16, "eva": 0, "luck": 15
        },
        "gil": 2400,
        "steal": {"common": "Lunar Curtain x2", "rare": "Lunar Curtain x2"},
        "bribe": ["Designer Wallet x5 (1,057,500 gil)"],
        "drop": {"common": "Lv. 2 Key Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Strength +10%", "Distill Power"],
        "armor_abilities": ["SOS Protect", "Defense +10%"],
        "immunities": ["Silence", "Sleep", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Threaten", "Death", "Delay", "Capture"],
        "status_resistances": {
            "Darkness": 20,
            "Doom": "0 (10 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Defender_Z_from_FFX.webp"
    },

    "Demonolith": {
        "zanmato_lv": 1,
        "hp": 45000,
        "hp_overkill": 13560,
        "mp": 9999,
        "ap": 11000,
        "ap_overkill": 16500,
        "location": "Inside Sin, Omega Ruins",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 33, "mag": 99, "def": 1, "mdef": 1,
            "acc": 1, "agl": 18, "eva": 0, "luck": 15
        },
        "gil": 1470,
        "steal": {"common": "Petrify Grenade x2", "rare": "Petrify Grenade x2"},
        "bribe": ["Lv. 3 Key Sphere x40 (1,125,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Stonetouch", "Stonestrike"],
        "armor_abilities": ["Stone Ward", "Stoneproof", "No Encounters"],
        "immunities": ["Sleep", "Poison", "Petrify", "Zombie", "Death", "Provoke"],
        "status_resistances": {
            "Silence": 50,
            "Darkness": 50,
            "Power Break": 80,
            "Doom": "0 (10 turns)"
        },
        "elemental_affinities": {
            "weak": ["Holy"],
            "resisted": ["Fire", "Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Demonolith-enemy-ffx.webp"
    },

    "Dingo": {
        "zanmato_lv": 1,
        "hp": 125,
        "hp_overkill": 188,
        "mp": 10,
        "ap": 2,
        "ap_overkill": 4,
        "location": "Besaid",
        "monster_arena": "Besaid",
        "stats": {
            "str": 13, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 0, "eva": 5, "luck": 15
        },
        "gil": 15,
        "steal": {"common": "Potion", "rare": "Sleeping Powder"},
        "bribe": ["Sleeping Powder x4 (3,125 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Silence Ward", "Sleep Ward", "Magic Def +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dingo_from_FFX.webp"
    },

    "Dinonix": {
        "zanmato_lv": 1,
        "hp": 140,
        "hp_overkill": 210,
        "mp": 25,
        "ap": 9,
        "ap_overkill": 18,
        "location": "Kilika Woods",
        "monster_arena": "Kilika",
        "stats": {
            "str": 14, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 0, "eva": 5, "luck": 15
        },
        "gil": 27,
        "steal": {"common": "Soft", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x2 (3,500 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward", "Defense +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dinonix_from_FFX.webp"
    },

    "Don Tonberry": {
        "zanmato_lv": 4,
        "hp": 480000,
        "hp_overkill": 10000,
        "mp": 120,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 95, "mag": 75, "def": 100, "mdef": 100,
            "acc": 80, "agl": 37, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Candle of Life x2", "rare": "Designer Wallet"},
        "bribe": None,
        "drop": {"common": "Farplane Wind x3", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 2-4 abilities, 100% chance",
        "weapon_abilities": ["Deathstrike", "Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Deathproof", "Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Tonberry-enemy-ffx.webp"
    },

    "Dual Horn (Mi'ihen Highroad)": {
        "zanmato_lv": 1,
        "hp": 1875,
        "hp_overkill": 560,
        "mp": 18,
        "ap": 42,
        "ap_overkill": 63,
        "location": "Mi'ihen Highroad, Mushroom Rock Road",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 22, "mag": 3, "def": 1, "mdef": 1,
            "acc": 1, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 105,
        "steal": {"common": "Potion", "rare": "Hi-Potion"},
        "bribe": ["Hi-Potion x60 (46,875 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Silencetouch", "Distill Ability"],
        "armor_abilities": ["HP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dual_Horn-enemy-ffx.webp"
    },

    "Dual Horn (Home/Airship)": {
        "zanmato_lv": 1,
        "hp": 3795,
        "hp_overkill": 1432,
        "mp": 22,
        "ap": 820,
        "ap_overkill": 1230,
        "location": "Home, Fahrenheit",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 27, "mag": 8, "def": 1, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 520,
        "steal": {"common": "Hi-Potion", "rare": "Mega-Potion"},
        "bribe": ["Mega-Potion x25 (94,875 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Silencetouch", "Distill Ability"],
        "armor_abilities": ["HP +5%", "HP +10%"],
        "immunities": ["Capture"],
        "status_resistances": {
            "Silence": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dual_Horn-enemy-ffx.webp"
    },

    "Epaaj": {
        "zanmato_lv": 1,
        "hp": 8700,
        "hp_overkill": 4060,
        "mp": 25,
        "ap": 970,
        "ap_overkill": 1455,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 28, "mag": 1, "def": 20, "mdef": 20,
            "acc": 1, "agl": 28, "eva": 0, "luck": 15
        },
        "gil": 950,
        "steal": {"common": "Hi-Potion", "rare": "Hi-Potion x2"},
        "bribe": ["Farplane Wind x25 (217,500 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%", "SOS Overdrive"],
        "armor_abilities": ["Defense +5%"],
        "immunities": ["Sleep", "Poison", "Power Break"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 95,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Klikk-enemy-ffx.webp"
    },

    "Espada": {
        "zanmato_lv": 4,
        "hp": 280000,
        "hp_overkill": 15000,
        "mp": 120,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 44, "mag": 31, "def": 100, "mdef": 160,
            "acc": 100, "agl": 51, "eva": 12, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Farplane Shadow x4", "rare": "Farplane Wind"},
        "bribe": None,
        "drop": {"common": "Rename Card x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Doom", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Slow": 50
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Klikk-enemy-ffx.webp"
    },

    "Evil Eye (Macalania)": {
        "zanmato_lv": 1,
        "hp": 310,
        "hp_overkill": 465,
        "mp": 300,
        "ap": 300,
        "ap_overkill": 600,
        "location": "Lake Macalania",
        "monster_arena": "Macalania",
        "stats": {
            "str": 1, "mag": 26, "def": 1, "mdef": 120,
            "acc": 1, "agl": 15, "eva": 13, "luck": 15
        },
        "gil": 205,
        "steal": {"common": "Hi-Potion", "rare": "Musk"},
        "bribe": ["Musk x3 (7,750 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Strength +5%", "Magic +5%", "Distill Speed"],
        "armor_abilities": ["Confuse Ward", "MP +10%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/BatEye-ffx.webp"
    },

    "Evil Eye (Home/Airship)": {
        "zanmato_lv": 1,
        "hp": 430,
        "hp_overkill": 645,
        "mp": 310,
        "ap": 480,
        "ap_overkill": 960,
        "location": "Home, Fahrenheit",
        "monster_arena": "Macalania",
        "stats": {
            "str": 1, "mag": 25, "def": 1, "mdef": 120,
            "acc": 1, "agl": 17, "eva": 13, "luck": 15
        },
        "gil": 280,
        "steal": {"common": "Musk", "rare": "Musk x2"},
        "bribe": ["Musk x4 (10,750 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Strength +5%", "Magic +5%", "Distill Speed"],
        "armor_abilities": ["Confuse Ward", "MP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/BatEye-ffx.webp"
    },

    "Exoray": {
        "zanmato_lv": 1,
        "hp": 7400,
        "hp_overkill": 11100,
        "mp": 300,
        "ap": 2400,
        "ap_overkill": 4800,
        "location": "Inside Sin",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 1, "mag": 24, "def": 1, "mdef": 1,
            "acc": 1, "agl": 0, "eva": 0, "luck": 15
        },
        "gil": 840,
        "steal": {"common": "Silence Grenade x3", "rare": "Ether"},
        "bribe": ["Turbo Ether x30 (185,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Sleeptouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Sleep Ward", "MP +10%"],
        "immunities": ["Darkness", "Zombie", "Berserk"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Poison": "0 (25% max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Exoray_from_FFX.webp"
    },

    "Fallen Monk (Rifle)": {
        "zanmato_lv": 1,
        "hp": 3300,
        "hp_overkill": 4950,
        "mp": 1,
        "ap": 1200,
        "ap_overkill": 1400,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 28, "mag": 33, "def": 40, "mdef": 40,
            "acc": 1, "agl": 27, "eva": 0, "luck": 15
        },
        "gil": 540,
        "steal": {"common": "Candle of Life x2", "rare": "Purifying Salt"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic Counter"],
        "armor_abilities": ["Zombie Ward", "Magic Def +5%"],
        "immunities": ["Silence", "Slow", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Sleep": 80,
            "Darkness": 95,
            "Poison": "50 (25 max HP/turn)",
            "Petrify": 50,
            "Doom": "0 (15 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Fallen_Monk_A.webp"
    },

    "Fallen Monk (Flamethrower)": {
        "zanmato_lv": 1,
        "hp": 3300,
        "hp_overkill": 4950,
        "mp": 1,
        "ap": 1200,
        "ap_overkill": 1400,
        "location": "Zanarkand Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 28, "mag": 33, "def": 40, "mdef": 40,
            "acc": 1, "agl": 22, "eva": 0, "luck": 15
        },
        "gil": 540,
        "steal": {"common": "Candle of Life x2", "rare": "Purifying Salt"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic Counter"],
        "armor_abilities": ["Zombie Ward", "Magic Def +5%"],
        "immunities": ["Silence", "Slow", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Sleep": 80,
            "Darkness": 95,
            "Poison": "50 (25 max HP/turn)",
            "Petrify": 50,
            "Doom": "0 (15 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Fallen_Monk_B.webp"
    },

    "Flame Flan": {
        "zanmato_lv": 1,
        "hp": 1500,
        "hp_overkill": 2250,
        "mp": 200,
        "ap": 480,
        "ap_overkill": 960,
        "location": "Calm Lands",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 1, "mag": 20, "def": 180, "mdef": 1,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 448,
        "steal": {"common": "Fire Gem", "rare": "Fire Gem x2"},
        "bribe": ["Fire Gem x10 (37,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Distill Mana"],
        "armor_abilities": ["Fire Ward", "Fireproof"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Lightning", "Water"],
            "immune": [],
            "absorb": ["Fire"]
        },
        "image": "./images/Flame_Flan_from_FFX.webp"
    },

    "Floating Death": {
        "zanmato_lv": 1,
        "hp": 6700,
        "hp_overkill": 10050,
        "mp": 520,
        "ap": 7100,
        "ap_overkill": 14200,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 1, "mag": 47, "def": 10, "mdef": 150,
            "acc": 1, "agl": 33, "eva": 18, "luck": 15
        },
        "gil": 1265,
        "steal": {"common": "Musk x4", "rare": "Musk x5"},
        "bribe": ["Gambler's Spirit x10 (167,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Strength +5%", "Magic +5%", "Distill Speed"],
        "armor_abilities": ["Confuse Ward", "Confuseproof", "MP +10%"],
        "immunities": ["Darkness", "Sensor", "Scan"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ahriman-ffx.webp"
    },

    "Floating Eye": {
        "zanmato_lv": 1,
        "hp": 140,
        "hp_overkill": 210,
        "mp": 200,
        "ap": 21,
        "ap_overkill": 42,
        "location": "Mi'ihen Highroad, Mushroom Rock Road",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 1, "mag": 18, "def": 1, "mdef": 120,
            "acc": 1, "agl": 10, "eva": 11, "luck": 15
        },
        "gil": 44,
        "steal": {"common": "Echo Screen", "rare": "Musk"},
        "bribe": ["Musk x1 (3,500 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Strength +5%", "Distill Speed"],
        "armor_abilities": ["Confuse Ward", "MP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Floating_Eye-enemy-ffx.webp"
    },

    "Funguar": {
        "zanmato_lv": 1,
        "hp": 540,
        "hp_overkill": 810,
        "mp": 60,
        "ap": 44,
        "ap_overkill": 88,
        "location": "Mushroom Rock Road / Djose Highroad",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 1, "mag": 26, "def": 1, "mdef": 1,
            "acc": 1, "agl": 4, "eva": 0, "luck": 15
        },
        "gil": 42,
        "steal": {"common": "Silence Grenade", "rare": "Ether"},
        "bribe": ["Turbo Ether x2 (13,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Sleeptouch", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Sleep Ward", "MP +5%"],
        "immunities": ["Darkness", "Zombie"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Poison": "0 (25% max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": ["Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Funguar-enemy-ffx.webp"
    },

    "Gandarewa": {
        "zanmato_lv": 1,
        "hp": 148,
        "hp_overkill": 220,
        "mp": 160,
        "ap": 32,
        "ap_overkill": 64,
        "location": "Mushroom Rock Road / Djose Highroad / Moonflow",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 1, "mag": 23, "def": 1, "mdef": 120,
            "acc": 1, "agl": 9, "eva": 12, "luck": 15
        },
        "gil": 62,
        "steal": {"common": "Electro Marble", "rare": "Electro Marble x2"},
        "bribe": ["Lightning Marble x3 (3,700 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike", "Distill Mana"],
        "armor_abilities": ["Lightning Ward", "Magic Def +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Gandarewa_from_FFX.webp"
    },

    "Garm": {
        "zanmato_lv": 1,
        "hp": 240,
        "hp_overkill": 360,
        "mp": 35,
        "ap": 48,
        "ap_overkill": 96,
        "location": "Djose Highroad / Moonflow",
        "monster_arena": "Djose Road",
        "stats": {
            "str": 17, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 16, "eva": 7, "luck": 15
        },
        "gil": 88,
        "steal": {"common": "Hi-Potion", "rare": "Sleeping Powder"},
        "bribe": ["Sleeping Powder x7 (6,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Silence Ward", "Sleep Ward", "Magic Def +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Garm_from_FFX.webp"
    },

    "Garuda (Besaid)": {
        "zanmato_lv": 1,
        "hp": 1400,
        "hp_overkill": 2100,
        "mp": 50,
        "ap": 8,
        "ap_overkill": 12,
        "location": "Besaid (Waterfall Way)",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 13, "mag": 10, "def": 1, "mdef": 1,
            "acc": 1, "agl": 7, "eva": 0, "luck": 15
        },
        "gil": 30,
        "steal": {"common": "Smoke Bomb", "rare": "Smoke Bomb x2"},
        "bribe": None,
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Darktouch", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Dark Ward"],
        "immunities": ["Sleep", "Zombie", "Threaten", "Provoke", "Bribe"],
        "status_resistances": {
            "Silence": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Garuda-enemy-ffx.webp"
    },

    "Garuda (Luca)": {
        "zanmato_lv": 1,
        "hp": 1800,
        "hp_overkill": 500,
        "mp": 10,
        "ap": 28,
        "ap_overkill": 42,
        "location": "Luca (Stands)",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 18, "mag": 12, "def": 1, "mdef": 1,
            "acc": 20, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["Dark Ward"],
        "immunities": ["Sleep", "Petrify", "Bribe", "Berserk"],
        "status_resistances": {
            "Silence": 20,
            "Poison": "0 (10 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Garuda-enemy-ffx.webp"
    },

    "Garuda (Mushroom Rock Road)": {
        "zanmato_lv": 1,
        "hp": 4000,
        "hp_overkill": 560,
        "mp": 50,
        "ap": 170,
        "ap_overkill": 255,
        "location": "Mushroom Rock Road",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 21, "mag": 40, "def": 1, "mdef": 1,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 140,
        "steal": {"common": "Smoke Bomb", "rare": "Smoke Bomb x2"},
        "bribe": ["Smoke Bomb x99 (100,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x2"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Darktouch", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Dark Ward"],
        "immunities": ["Sleep", "Petrify", "Provoke"],
        "status_resistances": {
            "Silence": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Garuda-enemy-ffx.webp"
    },

    "Gemini (Club)": {
        "zanmato_lv": 1,
        "hp": 36000,
        "hp_overkill": 13560,
        "mp": 1,
        "ap": 7800,
        "ap_overkill": 11700,
        "location": "Inside Sin / Omega Ruins",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 33, "mag": 1, "def": 50, "mdef": 30,
            "acc": 1, "agl": 21, "eva": 0, "luck": 1
        },
        "gil": 1111,
        "steal": {"common": "Light Curtain", "rare": "Light Curtain x2"},
        "bribe": ["Mana Tonic x10 (900,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x2"},
        "equipment_drop": "2-4 slots, 1-2 abilities, 31.25% chance",
        "weapon_abilities": ["Piercing", "Strength +10%", "Magic +10%"],
        "armor_abilities": ["SOS Regen", "HP +10%"],
        "immunities": ["Petrify", "Slow", "Zombie", "Power Break", "Threaten", "Death", "Delay", "Berserk"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 80,
            "Darkness": 20,
            "Poison": "90 (20 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Water", "Ice"]
        },
        "image": "./images/Gemini_Club-ffx.webp"
    },

    "Gemini (Sword)": {
        "zanmato_lv": 1,
        "hp": 36000,
        "hp_overkill": 13560,
        "mp": 1,
        "ap": 7800,
        "ap_overkill": 11700,
        "location": "Inside Sin / Omega Ruins",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 33, "mag": 1, "def": 50, "mdef": 30,
            "acc": 9, "agl": 21, "eva": 1, "luck": 1
        },
        "gil": 1111,
        "steal": {"common": "Light Curtain", "rare": "Light Curtain x2"},
        "bribe": ["Stamina Tonic x10 (900,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x2"},
        "equipment_drop": "2-4 slots, 1-2 abilities, 31.25% chance",
        "weapon_abilities": ["Piercing", "Strength +10%", "Magic +10%"],
        "armor_abilities": ["SOS Regen", "HP +10%"],
        "immunities": ["Petrify", "Slow", "Zombie", "Power Break", "Threaten", "Death", "Delay", "Berserk"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 80,
            "Darkness": 20,
            "Poison": "90 (20 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire", "Lightning"]
        },
        "image": "./images/Gemini_Blue-enemy-ffx.webp"
    },

    "Ghost": {
        "zanmato_lv": 1,
        "hp": 9999,
        "hp_overkill": 4060,
        "mp": 350,
        "ap": 1450,
        "ap_overkill": 2175,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 1, "mag": 33, "def": 120, "mdef": 1,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 810,
        "steal": {"common": "Phoenix Down x2", "rare": "Farplane Shadow"},
        "bribe": ["Mega Phoenix x38 (249,975 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Magic +5%", "Magic +10%", "Distill Mana"],
        "armor_abilities": ["Death Ward", "MP +10%", "No Encounters"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Berserk"],
        "status_resistances": {
            "Silence": 95,
            "Doom": "0 (7 turns)"
        },
        "elemental_affinities": {
            "weak": ["Holy"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ghost-enemy-ffx.webp"
    },

    "Gold Element": {
        "zanmato_lv": 1,
        "hp": 1200,
        "hp_overkill": 1800,
        "mp": 180,
        "ap": 92,
        "ap_overkill": 184,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 1, "mag": 32, "def": 120, "mdef": 1,
            "acc": 1, "agl": 7, "eva": 0, "luck": 15
        },
        "gil": 107,
        "steal": {"common": "Electro Marble", "rare": "Electro Marble x2"},
        "bribe": ["Lightning Marble x20 (30,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 0-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike", "Distill Mana"],
        "armor_abilities": ["Lightning Ward", "Lightningproof"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie"],
        "status_resistances": {
            "Silence": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": ["Fire", "Ice"],
            "immune": [],
            "absorb": ["Lightning"]
        },
        "image": "./images/Gold_Element_from_FFX.webp"
    },

    "Grat": {
        "zanmato_lv": 1,
        "hp": 4000,
        "hp_overkill": 6000,
        "mp": 25,
        "ap": 980,
        "ap_overkill": 1960,
        "location": "Mt. Gagazet",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 28, "mag": 1, "def": 50, "mdef": 50,
            "acc": 1, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 520,
        "steal": {"common": "Antidote x4", "rare": "Remedy x3"},
        "bribe": ["Remedy x40 (100,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 6.25% chance",
        "weapon_abilities": ["Piercing", "Poisontouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Poison Ward", "HP +5%", "HP +10%"],
        "immunities": ["Darkness", "Slow", "Zombie", "Delay"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 80,
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 25,
            "Death": 50,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Grat_from_FFX.webp"
    },

    "Great Malboro": {
        "zanmato_lv": 2,
        "hp": 64000,
        "hp_overkill": 13560,
        "mp": 1,
        "ap": 21000,
        "ap_overkill": 31500,
        "location": "Omega Ruins / Inside Sin",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 36, "mag": 42, "def": 1, "mdef": 1,
            "acc": 1, "agl": 18, "eva": 0, "luck": 15
        },
        "gil": 1900,
        "steal": {"common": "Remedy", "rare": "Mana Tonic"},
        "bribe": ["Wings to Discovery x5 (1,600,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "3-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Darktouch", "Silencetouch", "Sleeptouch", "Poisontouch"],
        "armor_abilities": ["Dark Ward", "Silence Ward", "Sleep Ward", "Poison Ward", "Stone Ward", "Confuse Ward", "Berserk Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Haste", "Berserk"],
        "status_resistances": {
            "Power Break": 50,
            "Magic Break": 50,
            "Armor Break": 50,
            "Mental Break": 50,
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": ["Ice", "Water"],
            "absorb": []
        },
        "image": "./images/Malboro_Menace-ffx.webp"
    },

    "Greater Sphere": {
        "zanmato_lv": 5,
        "hp": 1500000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 87, "mag": 102, "def": 130, "mdef": 120,
            "acc": 200, "agl": 55, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Return Sphere"},
        "bribe": None,
        "drop": {"common": "Luck Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1 ability, 100% chance",
        "weapon_abilities": ["One MP Cost"],
        "armor_abilities": ["Auto-Phoenix"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Holy"]
        },
        "image": "./images/Spherimorph-enemy-ffx.webp"
    },

    "Grenade": {
        "zanmato_lv": 1,
        "hp": 7500,
        "hp_overkill": 5384,
        "mp": 63,
        "ap": 1350,
        "ap_overkill": 2700,
        "location": "Mt. Gagazet",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 26, "mag": 24, "def": 1, "mdef": 150,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 540,
        "steal": {"common": "Fire Gem x2", "rare": "Fire Gem x3"},
        "bribe": ["Shining Gem x12 (187,500 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "2-3 slots, 1-2 abilities, 15.63% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Distill Mana"],
        "armor_abilities": ["Fire Ward", "Fireproof"],
        "immunities": ["Sleep", "Zombie", "Threaten"],
        "status_resistances": {
            "Silence": 95,
            "Darkness": 95,
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 50,
            "Death": 50,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Grenade_from_FFX.webp"
    },

    "Grendel": {
        "zanmato_lv": 1,
        "hp": 9500,
        "hp_overkill": 6972,
        "mp": 62,
        "ap": 2600,
        "ap_overkill": 3900,
        "location": "Mt. Gagazet / Zanarkand Ruins",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 41, "mag": 23, "def": 50, "mdef": 1,
            "acc": 1, "agl": 31, "eva": 0, "luck": 15
        },
        "gil": 730,
        "steal": {"common": "Hi-Potion", "rare": "Mega-Potion"},
        "bribe": ["Mega-Potion x60 (237,500 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Silencetouch", "Distill Ability"],
        "armor_abilities": ["HP +10%"],
        "immunities": ["Slow", "Magic Break"],
        "status_resistances": {
            "Sleep": 80,
            "Darkness": 95,
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 25,
            "Zombie": 25,
            "Death": 50,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Grendel_from_FFX.webp"
    },

    "Guado Guardian (Seymour)": {
        "zanmato_lv": 4,
        "hp": 2000,
        "hp_overkill": 2000,
        "mp": 10,
        "ap": 290,
        "ap_overkill": 435,
        "location": "Macalania Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 10, "mag": 15, "def": 1, "mdef": 1,
            "acc": 100, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 300,
        "steal": {"common": "Hi-Potion", "rare": "Ether"},
        "bribe": ["Ether x10 (50,000 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Sensor", "Piercing", "Strength +3%", "Strength +5%", "Magic +3%", "Magic +5%"],
        "armor_abilities": ["HP +10%", "HP +5%", "Magic Def +5%"],
        "immunities": ["Sleep", "Provoke", "Doom", "Berserk", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Poison": "0 (25 max HP/turn)",
            "Death": 10
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Guado_Guardian-enemy-ffx.webp"
    },

    "Guado Guardian (Macalania)": {
        "zanmato_lv": 4,
        "hp": 1200,
        "hp_overkill": 1432,
        "mp": 330,
        "ap": 290,
        "ap_overkill": 580,
        "location": "Macalania Temple / Lake Macalania",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 14, "def": 1, "mdef": 1,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 480,
        "steal": {"common": "Hi-Potion", "rare": "X-Potion"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Sensor", "Piercing", "Strength +3%", "Strength +5%", "Magic +3%", "Magic +5%"],
        "armor_abilities": ["HP +5%", "MP +5%", "Magic Def +3%"],
        "immunities": ["Silence", "Sleep", "Slow", "Magic Break", "Threaten", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 25,
            "Death": 25,
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Guado_Guardian-enemy-ffx.webp"
    },

    "Guado Guardian (Home)": {
        "zanmato_lv": 1,
        "hp": 2600,
        "hp_overkill": 1432,
        "mp": 600,
        "ap": 540,
        "ap_overkill": 1080,
        "location": "Home",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 24, "def": 1, "mdef": 1,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 380,
        "steal": {"common": "Hi-Potion", "rare": "X-Potion x2"},
        "bribe": ["X-Potion x30 (65,000 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Sensor", "Piercing", "Strength +3%", "Strength +5%", "Magic +3%", "Magic +5%"],
        "armor_abilities": ["HP +5%", "MP +5%", "Magic Def +3%"],
        "immunities": ["Sleep", "Magic Break", "Threaten", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Poison": "0 (25% max HP/turn)",
            "Petrify": 25,
            "Death": 25,
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Guado_Guardian-enemy-ffx.webp"
    },

    "Halma": {
        "zanmato_lv": 1,
        "hp": 13000,
        "hp_overkill": 13560,
        "mp": 1,
        "ap": 5300,
        "ap_overkill": 10600,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 46, "mag": 1, "def": 30, "mdef": 150,
            "acc": 1, "agl": 23, "eva": 0, "luck": 15
        },
        "gil": 1030,
        "steal": {"common": "Hypello Potion x3", "rare": "Shadow Gem x2"},
        "bribe": ["Supreme Gem x20 (325,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Berserk Ward", "Berserkproof"],
        "immunities": ["Sensor", "Scan"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": ["Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Shred_from_FFX.webp"
    },

    "Hornet": {
        "zanmato_lv": 4,
        "hp": 620000,
        "hp_overkill": 50000,
        "mp": 180,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 63, "mag": 88, "def": 70, "mdef": 95,
            "acc": 160, "agl": 102, "eva": 17, "luck": 33
        },
        "gil": 0,
        "steal": {"common": "Poison Fang x4", "rare": "Purifying Salt x2"},
        "bribe": None,
        "drop": {"common": "Accuracy Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Power Break": 95,
            "Magic Break": 95,
            "Armor Break": 95,
            "Mental Break": 95,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Wasp_from_FFX.webp"
    },

    "Ice Flan": {
        "zanmato_lv": 1,
        "hp": 1350,
        "hp_overkill": 2025,
        "mp": 160,
        "ap": 300,
        "ap_overkill": 600,
        "location": "Lake Macalania",
        "monster_arena": "Macalania",
        "stats": {
            "str": 1, "mag": 21, "def": 120, "mdef": 1,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 188,
        "steal": {"common": "Arctic Wind", "rare": "Arctic Wind x2"},
        "bribe": ["Ice Gem x9 (33,750 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Icestrike", "Distill Mana"],
        "armor_abilities": ["Ice Ward", "Iceproof"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": ["Lightning", "Water"],
            "immune": [],
            "absorb": ["Ice"]
        },
        "image": "./images/Ice_Flan_from_FFX.webp"
    },

    "Iguion": {
        "zanmato_lv": 1,
        "hp": 370,
        "hp_overkill": 555,
        "mp": 70,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Macalania Woods",
        "monster_arena": "Macalania",
        "stats": {
            "str": 23, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 19, "eva": 8, "luck": 15
        },
        "gil": 138,
        "steal": {"common": "Soft", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x5 (9,250 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward", "Defense +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Iguion_from_FFX.webp"
    },

    "Imp": {
        "zanmato_lv": 1,
        "hp": 880,
        "hp_overkill": 1320,
        "mp": 300,
        "ap": 770,
        "ap_overkill": 1540,
        "location": "Cavern of the Stolen Fayth / Mt. Gagazet",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 1, "mag": 25, "def": 1, "mdef": 180,
            "acc": 1, "agl": 24, "eva": 16, "luck": 15
        },
        "gil": 610,
        "steal": {"common": "Lightning Gem", "rare": "Lightning Gem x2"},
        "bribe": ["Lv. 1 Key Sphere x4 (22,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1 slot, 1 ability, 3.13% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike", "Distill Mana"],
        "armor_abilities": ["Lightning Ward", "Lightningproof"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Imp_from_FFX.webp"
    },

    "Ipiria": {
        "zanmato_lv": 1,
        "hp": 180,
        "hp_overkill": 270,
        "mp": 35,
        "ap": 24,
        "ap_overkill": 48,
        "location": "Mi'ihen Highroad (Oldroad) / Mushroom Rock Road",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 15, "mag": 1, "def": 1, "mdef": 120,
            "acc": 0, "agl": 13, "eva": 7, "luck": 15
        },
        "gil": 46,
        "steal": {"common": "Soft", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x3 (4,500 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward", "Defense +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ipiria_from_FFX.webp"
    },

    "Iron Giant": {
        "zanmato_lv": 1,
        "hp": 3600,
        "hp_overkill": 924,
        "mp": 1,
        "ap": 800,
        "ap_overkill": 1200,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 30, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 7, "eva": 0, "luck": 15
        },
        "gil": 600,
        "steal": {"common": "Light Curtain", "rare": "Light Curtain"},
        "bribe": ["Stamina Tonic x1 (90,000 gil)"],
        "drop": {"common": "Power Sphere x2", "rare": "Power Sphere x3"},
        "equipment_drop": "2-3 slots, 1-2 abilities, 31.25% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Strength +10%", "Magic +5%", "Magic +10%"],
        "armor_abilities": ["SOS Regen", "HP +5%", "HP +10%"],
        "immunities": ["Silence", "Threaten", "Berserk"],
        "status_resistances": {
            "Sleep": 50,
            "Darkness": 95,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Lightning"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Gemini_Blue-enemy-ffx.webp"
    },

    "Ironclad": {
        "zanmato_lv": 4,
        "hp": 2000000,
        "hp_overkill": 99999,
        "mp": 0,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 100, "mag": 1, "def": 220, "mdef": 180,
            "acc": 180, "agl": 65, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Light Curtain x4", "rare": "Stamina Tablet"},
        "bribe": None,
        "drop": {"common": "HP Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["HP +10%", "HP +20%", "HP +30%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Magic Break": 95,
            "Armor Break": 95,
            "Mental Break": 95,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": ["Fire", "Ice", "Lightning", "Water"],
            "absorb": []
        },
        "image": "./images/Gemini_Blue-enemy-ffx.webp"
    },

    "Jormungand": {
        "zanmato_lv": 4,
        "hp": 520000,
        "hp_overkill": 10000,
        "mp": 63,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 77, "mag": 80, "def": 33, "mdef": 186,
            "acc": 130, "agl": 53, "eva": 6, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Petrify Grenade x4", "rare": "Three Stars"},
        "bribe": None,
        "drop": {"common": "Supreme Gem x2", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-4 abilities, 100% chance",
        "weapon_abilities": ["Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Power Break": 90,
            "Magic Break": 90,
            "Armor Break": 90,
            "Mental Break": 90,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Anacondaur_from_FFX.webp"
    },

    "Juggernaut": {
        "zanmato_lv": 4,
        "hp": 1200000,
        "hp_overkill": 15000,
        "mp": 20,
        "ap": 8000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 98, "mag": 70, "def": 140, "mdef": 62,
            "acc": 150, "agl": 42, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Lunar Curtain x4", "rare": "Shining Gem"},
        "bribe": None,
        "drop": {"common": "Strength Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture", "Magical damage"],
        "status_resistances": {
            "Power Break": 95,
            "Magic Break": 95,
            "Armor Break": 95,
            "Mental Break": 95,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "absorb": []
        },
        "image": "./images/Grendel_from_FFX.webp"
    },

    "Jumbo Flan": {
        "zanmato_lv": 4,
        "hp": 1300000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 3, "mag": 98, "def": 255, "mdef": 80,
            "acc": 1, "agl": 60, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Lunar Curtain x4", "rare": "Mana Tablet"},
        "bribe": None,
        "drop": {"common": "Magic Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Magic Booster"],
        "armor_abilities": ["Fire Eater", "Water Eater", "Ice Eater"],
        "immunities": ["Silence", "Sleep", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture", "Physical damage"],
        "status_resistances": {
            "Reflect": "Auto",
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire", "Ice", "Lightning", "Water"]
        },
        "image": "./images/Dark_Flan_from_FFX.webp"
    },

    "Killer Bee": {
        "zanmato_lv": 1,
        "hp": 110,
        "hp_overkill": 165,
        "mp": 5,
        "ap": 9,
        "ap_overkill": 18,
        "location": "Kilika Woods",
        "monster_arena": "Kilika",
        "stats": {
            "str": 8, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 8, "eva": 10, "luck": 15
        },
        "gil": 23,
        "steal": {"common": "Antidote", "rare": "Poison Fang"},
        "bribe": ["Poison Fang x1 (2,750 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Icestrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Poison Ward", "MP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Killer_Bee_from_FFX.webp"
    },

    "Kusariqqu": {
        "zanmato_lv": 1,
        "hp": 445,
        "hp_overkill": 668,
        "mp": 31,
        "ap": 92,
        "ap_overkill": 184,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 32, "mag": 35, "def": 1, "mdef": 120,
            "acc": 1, "agl": 7, "eva": 0, "luck": 15
        },
        "gil": 112,
        "steal": {"common": "Hi-Potion", "rare": "Silver Hourglass"},
        "bribe": ["Silver Hourglass x20 (11,125 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 25% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Slow Ward", "Defense +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Kusariqqu_from_FFX.webp"
    },

    "Lamashtu": {
        "zanmato_lv": 1,
        "hp": 275,
        "hp_overkill": 413,
        "mp": 21,
        "ap": 32,
        "ap_overkill": 64,
        "location": "Djose Highroad / Mushroom Rock Road",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 23, "mag": 20, "def": 1, "mdef": 120,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 72,
        "steal": {"common": "Potion", "rare": "Silver Hourglass"},
        "bribe": ["Silver Hourglass x10 (6,875 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Slow Ward", "HP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Lamashtu_from_FFX.webp"
    },

    "Land Worm": {
        "zanmato_lv": 1,
        "hp": 80000,
        "hp_overkill": 13560,
        "mp": 160,
        "ap": 22000,
        "ap_overkill": 33000,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 55, "mag": 50, "def": 10, "mdef": 10,
            "acc": 1, "agl": 21, "eva": 0, "luck": 15
        },
        "gil": 2200,
        "steal": {"common": "Stamina Spring", "rare": "Stamina Spring"},
        "bribe": ["Dark Matter x2 (2,000,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Lv. 4 Key Sphere x1"},
        "equipment_drop": "3-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Slowtouch", "Slowstrike", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["HP +10%", "Auto-Potion"],
        "immunities": ["Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Berserk", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 80,
            "Darkness": 20,
            "Poison": "0 (2 max HP/turn)",
            "Power Break": 50,
            "Magic Break": 50,
            "Doom": "0 (10 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Land_Worm_from_FFX.webp"
    },

    "Larva": {
        "zanmato_lv": 1,
        "hp": 1498,
        "hp_overkill": 924,
        "mp": 1000,
        "ap": 262,
        "ap_overkill": 393,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 10, "mag": 19, "def": 40, "mdef": 45,
            "acc": 1, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 350,
        "steal": {"common": "Lunar Curtain", "rare": "Lunar Curtain x2"},
        "bribe": ["Shining Thorn x10 (37,450 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike"],
        "armor_abilities": ["Lightning Ward"],
        "immunities": ["Sleep", "Darkness", "Poison", "Slow", "Berserk"],
        "status_resistances": {
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Larva-enemy-ffx.webp"
    },

    "Machea": {
        "zanmato_lv": 1,
        "hp": 18000,
        "hp_overkill": 13560,
        "mp": 59,
        "ap": 8300,
        "ap_overkill": 12450,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 40, "mag": 1, "def": 70, "mdef": 30,
            "acc": 1, "agl": 39, "eva": 0, "luck": 15
        },
        "gil": 1450,
        "steal": {"common": "Hi-Potion x2", "rare": "Stamina Tonic"},
        "bribe": ["Chocobo Wing x60 (450,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%", "SOS Overdrive"],
        "armor_abilities": ["Defense +10%", "Defense +20%"],
        "immunities": ["Sleep", "Poison", "Power Break", "Sensor", "Scan"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 95,
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Klikk-enemy-ffx.webp"
    },

    "Maelspike": {
        "zanmato_lv": 1,
        "hp": 10000,
        "hp_overkill": 7500,
        "mp": 35,
        "ap": 600,
        "ap_overkill": 900,
        "location": "Mt. Gagazet",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 40, "mag": 33, "def": 50, "mdef": 1,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 330,
        "steal": {"common": "Water Gem x2", "rare": "Water Gem x3"},
        "bribe": ["Attribute Sphere x1 (250,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "2-4 slots, 1-2 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Strength +3%", "Strength +5%"],
        "armor_abilities": ["Zombie Ward", "Defense +5%", "Defense +10%"],
        "immunities": ["Sleep", "Slow", "Threaten"],
        "status_resistances": {
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Maelspike_from_FFX.webp"
    },

    "Mafdet": {
        "zanmato_lv": 1,
        "hp": 710,
        "hp_overkill": 1065,
        "mp": 25,
        "ap": 300,
        "ap_overkill": 600,
        "location": "Lake Macalania",
        "monster_arena": "Macalania",
        "stats": {
            "str": 29, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 172,
        "steal": {"common": "Hi-Potion", "rare": "Hypello Potion"},
        "bribe": ["Hypello Potion x28 (17,750 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Berserk Ward", "Defense +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice", "Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mafdet_from_FFX.webp"
    },

    "Magic Urn": {
        "zanmato_lv": 1,
        "hp": 999999,
        "hp_overkill": 999999,
        "mp": 9999,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 40, "def": 255, "mdef": 255,
            "acc": 1, "agl": 1, "eva": 0, "luck": 1
        },
        "gil": 0,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Overkill: x2", "rare": "Overkill: x2"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Shell", "Protect", "Reflect", "Haste", "Demi", "Regen", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Magic_Urn-enemy-ffx.webp"
    },

    "Malboro": {
        "zanmato_lv": 2,
        "hp": 27000,
        "hp_overkill": 4060,
        "mp": 1,
        "ap": 2200,
        "ap_overkill": 3300,
        "location": "Calm Lands / Cavern of the Stolen Fayth",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 32, "mag": 32, "def": 1, "mdef": 1,
            "acc": 1, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 1500,
        "steal": {"common": "Remedy", "rare": "Remedy"},
        "bribe": ["Wings to Discovery x4 (675,000 gil)"],
        "drop": {"common": "Mana Sphere x2", "rare": "Mana Sphere x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Darktouch", "Silencetouch", "Sleeptouch", "Poisontouch"],
        "armor_abilities": ["Dark Ward", "Silence Ward", "Sleep Ward", "Poison Ward", "Stone Ward", "Confuse Ward", "Berserk Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Haste", "Berserk"],
        "status_resistances": {
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": ["Ice", "Water"],
            "absorb": []
        },
        "image": "./images/FFX_Malboro.PNG.webp"
    },

    "Malboro Menace": {
        "zanmato_lv": 4,
        "hp": 640000,
        "hp_overkill": 12000,
        "mp": 200,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 60, "mag": 53, "def": 24, "mdef": 63,
            "acc": 120, "agl": 34, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Remedy x4", "rare": "Mana Spring x2"},
        "bribe": None,
        "drop": {"common": "Mana Tonic x2", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-4 abilities, 100% chance",
        "weapon_abilities": ["Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Malboro_Menace-ffx.webp"
    },

    "Mandragora": {
        "zanmato_lv": 1,
        "hp": 31000,
        "hp_overkill": 5384,
        "mp": 120,
        "ap": 6320,
        "ap_overkill": 9345,
        "location": "Mt. Gagazet Cavern / Zanarkand Ruins",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 34, "mag": 40, "def": 12, "mdef": 15,
            "acc": 1, "agl": 13, "eva": 0, "luck": 15
        },
        "gil": 1200,
        "steal": {"common": "Remedy x2", "rare": "Remedy x3"},
        "bribe": ["Return Sphere x24 (775,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Poisontouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Dark Ward", "Silence Ward", "Sleep Ward", "Poison Ward", "Stone Ward", "Confuse Ward", "Berserk Ward"],
        "immunities": ["Darkness", "Slow", "Zombie", "Threaten", "Provoke"],
        "status_resistances": {
            "Silence": 95,
            "Sleep": 80,
            "Poison": "25 (5 HP/turn)",
            "Petrify": 25,
            "Death": 50,
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mandragora-enemy-ffx.webp"
    },

    "Master Coeurl": {
        "zanmato_lv": 1,
        "hp": 13000,
        "hp_overkill": 13560,
        "mp": 540,
        "ap": 6500,
        "ap_overkill": 9750,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 42, "mag": 38, "def": 50, "mdef": 50,
            "acc": 1, "agl": 28, "eva": 0, "luck": 15
        },
        "gil": 2030,
        "steal": {"common": "Farplane Shadow x2", "rare": "Farplane Shadow x4"},
        "bribe": ["Warp Sphere x1 (325,000 gil)"],
        "drop": {"common": "Lv. 1 Key Sphere x1", "rare": "Friend Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Deathtouch", "Deathstrike", "Strength +5%", "Magic +5%", "Magic +10%"],
        "armor_abilities": ["Death Ward", "Deathproof", "Curseproof", "Defense +10%", "Magic Def +10%"],
        "immunities": ["Threaten"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": ["Ice", "Lightning"],
            "absorb": []
        },
        "image": "./images/Master_Coeurl_from_FFX.webp"
    },

    "Master Tonberry": {
        "zanmato_lv": 1,
        "hp": 48000,
        "hp_overkill": 13560,
        "mp": 1,
        "ap": 20000,
        "ap_overkill": 30000,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 47, "mag": 52, "def": 40, "mdef": 40,
            "acc": 1, "agl": 18, "eva": 0, "luck": 15
        },
        "gil": 2400,
        "steal": {"common": "Mana Spring", "rare": "Tetra Elemental"},
        "bribe": ["Pendulum x3 (1,200,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Teleport Sphere x1"},
        "equipment_drop": "3-4 slots, 0-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Deathstrike", "Slowstrike"],
        "armor_abilities": ["Death Ward", "Deathproof"],
        "immunities": ["Silence", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Delay", "Berserk"],
        "status_resistances": {
            "Sleep": 99,
            "Doom": "0 (25 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Master_Tonberry_from_FFX.webp"
    },

    "Maze Larva": {
        "zanmato_lv": 1,
        "hp": 2222,
        "hp_overkill": 2108,
        "mp": 1111,
        "ap": 1850,
        "ap_overkill": 2775,
        "location": "Via Purifico (Land)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 11, "mag": 24, "def": 40, "mdef": 45,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 620,
        "steal": {"common": "Fish Scale x2", "rare": "Dragon Scale x2"},
        "bribe": ["Water Gem x14 (55,550 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Sleeptouch"],
        "armor_abilities": ["Sleep Ward", "Magic Def +5%"],
        "immunities": ["Sleep", "Poison", "Petrify", "Zombie", "Death", "Berserk", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Larva-enemy-ffx.webp"
    },

    "Mech Defender": {
        "zanmato_lv": 1,
        "hp": 8700,
        "hp_overkill": 5384,
        "mp": 1,
        "ap": 950,
        "ap_overkill": 1425,
        "location": "Mt. Gagazet",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 40, "mag": 15, "def": 1, "mdef": 10,
            "acc": 1, "agl": 7, "eva": 0, "luck": 15
        },
        "gil": 880,
        "steal": {"common": "Al Bhed Potion x2", "rare": "Al Bhed Potion x3"},
        "bribe": ["Al Bhed Potion x99 (217,500 gil)"],
        "drop": {"common": "Phoenix Down x1", "rare": "Mega Phoenix x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost", "SOS Shell", "SOS Protect", "SOS Reflect"],
        "immunities": ["Sleep", "Poison", "Zombie", "Threaten", "Death", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mech_Defender_from_FFX.webp"
    },

    "Mech Guard": {
        "zanmato_lv": 1,
        "hp": 1280,
        "hp_overkill": 1432,
        "mp": 1,
        "ap": 310,
        "ap_overkill": 465,
        "location": "Bikanel",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 25, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 600,
        "steal": {"common": "Grenade", "rare": "Grenade x3"},
        "bribe": ["Grenade x50 (32,000 gil)"],
        "drop": {"common": "Hi-Potion x1", "rare": "Hi-Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost"],
        "immunities": ["Sleep", "Poison", "Zombie", "Threaten", "Death", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Worker-enemy-ffx.webp"
    },

    "Mech Gunner": {
        "zanmato_lv": 1,
        "hp": 2800,
        "hp_overkill": 1432,
        "mp": 1,
        "ap": 540,
        "ap_overkill": 810,
        "location": "Bikanel",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 31, "mag": 1, "def": 10, "mdef": 10,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 800,
        "steal": {"common": "Al Bhed Potion", "rare": "Al Bhed Potion x2"},
        "bribe": ["Al Bhed Potion x40 (70,000 gil)"],
        "drop": {"common": "Hi-Potion x2", "rare": "Hi-Potion x2"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost", "SOS Shell", "SOS Protect", "SOS Reflect"],
        "immunities": ["Sleep", "Poison", "Zombie", "Threaten", "Death", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mech_Gunner-enemy-ffx.webp"
    },

    "Mech Hunter": {
        "zanmato_lv": 1,
        "hp": 5500,
        "hp_overkill": 4060,
        "mp": 1,
        "ap": 820,
        "ap_overkill": 1230,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 36, "mag": 1, "def": 10, "mdef": 10,
            "acc": 1, "agl": 8, "eva": 0, "luck": 15
        },
        "gil": 673,
        "steal": {"common": "Al Bhed Potion", "rare": "Al Bhed Potion x2"},
        "bribe": ["Al Bhed Potion x60 (137,500 gil)"],
        "drop": {"common": "Phoenix Down x1", "rare": "Mega Phoenix x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost", "SOS Shell", "SOS Protect", "SOS Reflect"],
        "immunities": ["Sleep", "Poison", "Zombie", "Threaten", "Death", "Berserk", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mech_Hunter_from_FFX.webp"
    },

    "Mech Leader": {
        "zanmato_lv": 1,
        "hp": 3700,
        "hp_overkill": 5550,
        "mp": 1,
        "ap": 830,
        "ap_overkill": 1245,
        "location": "Mt. Gagazet",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 31, "mag": 28, "def": 5, "mdef": 5,
            "acc": 1, "agl": 15, "eva": 0, "luck": 15
        },
        "gil": 530,
        "steal": {"common": "Grenade x2", "rare": "Frag Grenade x2"},
        "bribe": ["Door to Tomorrow x2 (92,500 gil)"],
        "drop": {"common": "Hi-Potion x1", "rare": "Mega-Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost"],
        "immunities": ["Sleep", "Poison", "Zombie", "Threaten", "Death", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mech_Leader_from_FFX.webp"
    },

    "Mech Scouter (Normal)": {
        "zanmato_lv": 1,
        "hp": 2750,
        "hp_overkill": 4125,
        "mp": 1,
        "ap": 480,
        "ap_overkill": 720,
        "location": "Calm Lands",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 384,
        "steal": {"common": "Grenade x3", "rare": "Grenade x4"},
        "bribe": ["Door to Tomorrow x1 (68,750 gil)"],
        "drop": {"common": "Hi-Potion x1", "rare": "Mega-Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost"],
        "immunities": ["Sleep", "Poison", "Zombie", "Threaten", "Death", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mech_Scouter_from_FFX.webp"
    },

    "Mech Scouter (Flaming)": {
        "zanmato_lv": 1,
        "hp": 2750,
        "hp_overkill": 4125,
        "mp": 1,
        "ap": 530,
        "ap_overkill": 795,
        "location": "Calm Lands",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 215,
        "steal": {"common": "Grenade x3", "rare": "Grenade x3"},
        "bribe": ["Door to Tomorrow x1 (68,750 gil)"],
        "drop": {"common": "Hi-Potion x1", "rare": "Mega-Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost"],
        "immunities": ["Sleep", "Poison", "Zombie", "Threaten", "Death", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mech_Scouter_from_FFX.webp"
    },

    "Melusine": {
        "zanmato_lv": 1,
        "hp": 265,
        "hp_overkill": 405,
        "mp": 65,
        "ap": 92,
        "ap_overkill": 184,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 20, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 17, "eva": 8, "luck": 15
        },
        "gil": 108,
        "steal": {"common": "Soft", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x4 (6,625 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward", "Defense +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire", "Lightning"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Melusine_from_FFX.webp"
    },

    "Mi'ihen Fang": {
        "zanmato_lv": 1,
        "hp": 160,
        "hp_overkill": 240,
        "mp": 20,
        "ap": 20,
        "ap_overkill": 40,
        "location": "Mi'ihen Highroad",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 16, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 13, "eva": 5, "luck": 15
        },
        "gil": 33,
        "steal": {"common": "Potion", "rare": "Sleeping Powder"},
        "bribe": ["Sleeping Powder x5 (4,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Silence Ward", "Sleep Ward", "Magic Def +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mi'ihen_Fang_from_FFX.webp"
    },

    "Mimic (Ruminant)": {
        "zanmato_lv": 1,
        "hp": 60000,
        "hp_overkill": 13560,
        "mp": 10,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 54, "mag": 26, "def": 1, "mdef": 1,
            "acc": 1, "agl": 25, "eva": 0, "luck": 15
        },
        "gil": 50000,
        "steal": None,
        "bribe": None,
        "drop": {"common": "Overkill: x2", "rare": "Overkill: x2"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Haste", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/MimicA_(FFX).webp"
    },

    "Mimic (Machina)": {
        "zanmato_lv": 1,
        "hp": 40000,
        "hp_overkill": 13560,
        "mp": 10,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 33, "mag": 38, "def": 150, "mdef": 150,
            "acc": 1, "agl": 29, "eva": 0, "luck": 15
        },
        "gil": 50000,
        "steal": None,
        "bribe": None,
        "drop": {"common": "Overkill: x2", "rare": "Overkill: x2"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Haste", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/MimicB_(FFX).webp"
    },

    "Mimic (Roc)": {
        "zanmato_lv": 1,
        "hp": 40000,
        "hp_overkill": 13560,
        "mp": 10,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 42, "mag": 12, "def": 255, "mdef": 1,
            "acc": 1, "agl": 22, "eva": 0, "luck": 15
        },
        "gil": 50000,
        "steal": None,
        "bribe": None,
        "drop": {"common": "Overkill: x2", "rare": "Overkill: x2"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Haste", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/MimicC_(FFX).webp"
    },

    "Mimic (Basilisk)": {
        "zanmato_lv": 1,
        "hp": 40000,
        "hp_overkill": 13560,
        "mp": 10,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 42, "mag": 58, "def": 1, "mdef": 255,
            "acc": 1, "agl": 22, "eva": 0, "luck": 15
        },
        "gil": 50000,
        "steal": None,
        "bribe": None,
        "drop": {"common": "Overkill: x2", "rare": "Overkill: x2"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Haste", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/MimicD_(FFX).webp"
    },

    "Murussu": {
        "zanmato_lv": 1,
        "hp": 580,
        "hp_overkill": 870,
        "mp": 20,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Macalania Woods",
        "monster_arena": "Macalania",
        "stats": {
            "str": 25, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 7, "eva": 0, "luck": 15
        },
        "gil": 165,
        "steal": {"common": "Hi-Potion", "rare": "Hypello Potion"},
        "bribe": ["Hypello Potion x24 (14,500 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Berserk Ward", "Defense +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Murussu_from_FFX.webp"
    },

    "Mushussu": {
        "zanmato_lv": 1,
        "hp": 680,
        "hp_overkill": 1020,
        "mp": 38,
        "ap": 310,
        "ap_overkill": 620,
        "location": "Bikanel",
        "monster_arena": "Bikanel",
        "stats": {
            "str": 36, "mag": 42, "def": 1, "mdef": 120,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 270,
        "steal": {"common": "Hi-Potion", "rare": "Silver Hourglass"},
        "bribe": ["Gold Hourglass x5 (17,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Al Bhed Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Slow Ward", "HP +10%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mushussu_from_FFX.webp"
    },

    "Nebiros": {
        "zanmato_lv": 1,
        "hp": 700,
        "hp_overkill": 1050,
        "mp": 65,
        "ap": 480,
        "ap_overkill": 960,
        "location": "Calm Lands",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 22, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 22, "eva": 16, "luck": 15
        },
        "gil": 320,
        "steal": {"common": "Poison Fang", "rare": "Poison Fang x2"},
        "bribe": ["Poison Fang x6 (17,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Speed"],
        "armor_abilities": ["Poison Ward"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Nebiros_from_FFX.webp"
    },

    "Nega Elemental": {
        "zanmato_lv": 4,
        "hp": 1300000,
        "hp_overkill": 15000,
        "mp": 999,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 1, "mag": 80, "def": 140, "mdef": 42,
            "acc": 150, "agl": 44, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Star Curtain x4", "rare": "Twin Stars"},
        "bribe": None,
        "drop": {"common": "Twin Stars x2", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 2-4 abilities, 100% chance",
        "weapon_abilities": ["Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["Fire Eater", "Lightning Eater", "Water Eater", "Ice Eater"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire", "Ice", "Lightning", "Water", "Holy"]
        },
        "image": "./images/Dark_Element_from_FFX.webp"
    },

    "Neslug (Outside)": {
        "zanmato_lv": 4,
        "hp": 4000000,
        "hp_overkill": 12000,
        "mp": 999,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 130, "mag": 130, "def": 80, "mdef": 80,
            "acc": 1, "agl": 43, "eva": 0, "luck": 20
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Friend Sphere"},
        "bribe": None,
        "drop": {"common": "Pendulum x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Triple AP"],
        "armor_abilities": ["HP +10%", "HP +20%", "HP +30%"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Silence": 50
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Neslug-ffx-enemy.webp"
    },

    "Neslug (In Shell)": {
        "zanmato_lv": 4,
        "hp": 4000000,
        "hp_overkill": 12000,
        "mp": 999,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 130, "mag": 130, "def": 80, "mdef": 80,
            "acc": 1, "agl": 43, "eva": 0, "luck": 20
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Friend Sphere"},
        "bribe": None,
        "drop": {"common": "Pendulum x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Triple AP"],
        "armor_abilities": ["HP +10%", "HP +20%", "HP +30%"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture", "Physical damage"],
        "status_resistances": {
            "Silence": 50,
            "Regen": "Auto"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Neslug-ffx-enemy.webp"
    },

    "Neslug (Broken Shell)": {
        "zanmato_lv": 4,
        "hp": 4000000,
        "hp_overkill": 12000,
        "mp": 999,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 130, "mag": 130, "def": 80, "mdef": 80,
            "acc": 1, "agl": 120, "eva": 0, "luck": 20
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Friend Sphere"},
        "bribe": None,
        "drop": {"common": "Pendulum x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Triple AP"],
        "armor_abilities": ["HP +10%", "HP +20%", "HP +30%"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Silence": 50
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Neslug-ffx-enemy.webp"
    },

    "Nidhogg": {
        "zanmato_lv": 1,
        "hp": 2000,
        "hp_overkill": 3000,
        "mp": 46,
        "ap": 810,
        "ap_overkill": 1620,
        "location": "Cavern of the Stolen Fayth / Mt. Gagazet",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 43, "mag": 50, "def": 1, "mdef": 180,
            "acc": 1, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 602,
        "steal": {"common": "Hi-Potion", "rare": "Gold Hourglass"},
        "bribe": ["Gold Hourglass x12 (50,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Slow Ward"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Nidhogg_from_FFX.webp"
    },

    "Ochu": {
        "zanmato_lv": 1,
        "hp": 7200,
        "hp_overkill": 924,
        "mp": 35,
        "ap": 180,
        "ap_overkill": 270,
        "location": "Moonflow",
        "monster_arena": "Djose Road",
        "stats": {
            "str": 22, "mag": 14, "def": 1, "mdef": 1,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 520,
        "steal": {"common": "Remedy", "rare": "Remedy x2"},
        "bribe": ["Remedy x70 (180,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Mana Sphere x2"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Poisontouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Dark Ward", "Silence Ward", "Sleep Ward", "Poison Ward", "Stone Ward", "Confuse Ward", "Berserk Ward"],
        "immunities": ["Darkness", "Zombie", "Provoke", "Berserk"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Poison": "100 (5 HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ochu_from_FFX.webp"
    },

    "Octopus": {
        "zanmato_lv": 1,
        "hp": 4500,
        "hp_overkill": 2108,
        "mp": 1,
        "ap": 750,
        "ap_overkill": 1050,
        "location": "Via Purifico (Underwater)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 27, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 220,
        "steal": {"common": "Dragon Scale x2", "rare": "Water Gem x2"},
        "bribe": ["Healing Spring x20 (112,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1 slot, 0-1 ability, 50% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Water Ward", "HP +5%"],
        "immunities": ["Sleep", "Threaten", "Capture"],
        "status_resistances": {
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Octopus-enemy-ffx.webp"
    },

    "Ogre": {
        "zanmato_lv": 1,
        "hp": 9400,
        "hp_overkill": 4060,
        "mp": 3,
        "ap": 1080,
        "ap_overkill": 1620,
        "location": "Calm Lands",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 28, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 980,
        "steal": {"common": "Stamina Spring", "rare": "Stamina Spring x2"},
        "bribe": ["Stamina Spring x50 (235,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%", "Counterattack"],
        "armor_abilities": ["SOS Haste", "HP +10%"],
        "immunities": ["Slow", "Power Break"],
        "status_resistances": {
            "Sleep": 95,
            "Darkness": 95,
            "Poison": "25 (25 HP/turn)",
            "Petrify": 25,
            "Zombie": 25,
            "Death": 25,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ogre_from_FFX.webp"
    },

    "One-Eye": {
        "zanmato_lv": 4,
        "hp": 150000,
        "hp_overkill": 15000,
        "mp": 270,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 55, "mag": 77, "def": 58, "mdef": 183,
            "acc": 85, "agl": 38, "eva": 10, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Lunar Curtain x3", "rare": "Blessed Gem"},
        "bribe": None,
        "drop": {"common": "Magic Def Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Triple AP"],
        "armor_abilities": ["MP +10%", "MP +20%", "MP +30%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Magic Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Regen": "Auto",
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": ["Fire", "Ice", "Lightning", "Water"],
            "absorb": []
        },
        "image": "./images/BatEye-ffx.webp"
    },

    "Ornitholestes": {
        "zanmato_lv": 4,
        "hp": 800000,
        "hp_overkill": 99999,
        "mp": 300,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 83, "mag": 30, "def": 55, "mdef": 170,
            "acc": 200, "agl": 130, "eva": 80, "luck": 20
        },
        "gil": 0,
        "steal": {"common": "Rename Card", "rare": "Chocobo Wing"},
        "bribe": None,
        "drop": {"common": "Gambler's Spirit x2", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Double Overdrive"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": ["Water"],
            "absorb": ["Fire"]
        },
        "image": "./images/Yowie_from_FFX.webp"
    },

    "Phlegyas": {
        "zanmato_lv": 1,
        "hp": 1680,
        "hp_overkill": 2108,
        "mp": 50,
        "ap": 650,
        "ap_overkill": 975,
        "location": "Via Purifico (Underwater)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 26, "mag": 33, "def": 1, "mdef": 20,
            "acc": 1, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 410,
        "steal": {"common": "Dragon Scale x2", "rare": "Water Gem"},
        "bribe": ["Healing Spring x6 (42,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["MP +10%", "Auto-Med"],
        "immunities": ["Capture"],
        "status_resistances": {
            "Silence": 95,
            "Sleep": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Phlegyas-enemy-ffx.webp"
    },

    "Piranha (Single)": {
        "zanmato_lv": 1,
        "hp": 50,
        "hp_overkill": 225,
        "mp": 1,
        "ap": 1,
        "ap_overkill": 2,
        "location": "Salvage Ship / Besaid (Valley)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 6, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 2,
        "steal": {"common": "Grenade", "rare": "Grenade x2"},
        "bribe": ["Water Gem x1 (1,250 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Poison", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Piranha_from_FFX.webp"
    },

    "Piranha (Paired)": {
        "zanmato_lv": 1,
        "hp": 100,
        "hp_overkill": 225,
        "mp": 2,
        "ap": 1,
        "ap_overkill": 2,
        "location": "Salvage Ship / Besaid (Valley)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 8, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 3,
        "steal": {"common": "Grenade", "rare": "Grenade x2"},
        "bribe": ["Water Gem x1 (2,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Poison", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Piranha_from_FFX.webp"
    },

    "Piranha (Trio)": {
        "zanmato_lv": 1,
        "hp": 150,
        "hp_overkill": 225,
        "mp": 3,
        "ap": 1,
        "ap_overkill": 2,
        "location": "Salvage Ship / Underwater Ruins / Besaid (Valley)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 10, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 5,
        "steal": {"common": "Grenade", "rare": "Grenade x2"},
        "bribe": ["Water Gem x2 (3,750 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Poison", "Capture"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Piranha_from_FFX.webp"
    },

    "Pteryx": {
        "zanmato_lv": 4,
        "hp": 100000,
        "hp_overkill": 99999,
        "mp": 0,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 90, "mag": 5, "def": 100, "mdef": 100,
            "acc": 200, "agl": 60, "eva": 60, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Smoke Bomb x4", "rare": "Candle of Life"},
        "bribe": None,
        "drop": {"common": "Evasion Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Power Break": 90,
            "Magic Break": 90,
            "Armor Break": 90,
            "Mental Break": 90,
            "Regen": "Auto",
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Simurgh_from_FFX.webp"
    },

    "Puroboros": {
        "zanmato_lv": 1,
        "hp": 20000,
        "hp_overkill": 13560,
        "mp": 180,
        "ap": 3200,
        "ap_overkill": 6400,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 40, "mag": 32, "def": 60, "mdef": 20,
            "acc": 1, "agl": 28, "eva": 0, "luck": 15
        },
        "gil": 970,
        "steal": {"common": "Fire Gem x3", "rare": "Fire Gem x4"},
        "bribe": ["Shining Gem x36 (500,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Lv. 1 Key Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Distill Power"],
        "armor_abilities": ["Fireproof", "Fire Eater"],
        "immunities": ["Sleep", "Threaten", "Sensor", "Scan"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Petrify": 120,
            "Death": 120,
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Puroboros_from_FFX.webp"
    },

    "Qactuar": {
        "zanmato_lv": 2,
        "hp": 500,
        "hp_overkill": 750,
        "mp": 1,
        "ap": 350,
        "ap_overkill": 525,
        "location": "Thunder Plains",
        "monster_arena": "Thunder Plains",
        "stats": {
            "str": 19, "mag": 1, "def": 1, "mdef": 255,
            "acc": 1, "agl": 15, "eva": 17, "luck": 15
        },
        "gil": 48,
        "steal": {"common": "Chocobo Feather", "rare": "Chocobo Feather"},
        "bribe": None,
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x2"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Initiative", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["HP +5%", "HP Stroll", "MP Stroll"],
        "immunities": ["Silence", "Darkness", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Demi", "Bribe", "Delay", "Berserk"],
        "status_resistances": {
            "Sleep": 80,
            "Poison": "25 (1 HP/turn)",
            "Petrify": 25,
            "Death": 25,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Qactuar_FFX.webp"
    },

    "Ragora": {
        "zanmato_lv": 1,
        "hp": 780,
        "hp_overkill": 1170,
        "mp": 15,
        "ap": 20,
        "ap_overkill": 40,
        "location": "Kilika Woods",
        "monster_arena": "Kilika",
        "stats": {
            "str": 18, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 8, "eva": 0, "luck": 15
        },
        "gil": 48,
        "steal": {"common": "Antidote", "rare": "Remedy"},
        "bribe": ["Remedy x8 (19,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 6.25% chance",
        "weapon_abilities": ["Piercing", "Poisontouch", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Poison Ward", "HP +5%"],
        "immunities": ["Darkness", "Zombie"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Ragora_from_FFX.webp"
    },

    "Raldo": {
        "zanmato_lv": 1,
        "hp": 240,
        "hp_overkill": 360,
        "mp": 10,
        "ap": 20,
        "ap_overkill": 40,
        "location": "Mi'ihen Highroad",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 19, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 5, "eva": 0, "luck": 15
        },
        "gil": 42,
        "steal": {"common": "Potion", "rare": "Hypello Potion"},
        "bribe": ["Hypello Potion x10 (6,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Berserk Ward", "Defense +3%"],
        "immunities": [],
        "status_resistances": {
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Raldo_from_FFX.webp"
    },

    "Raptor": {
        "zanmato_lv": 1,
        "hp": 200,
        "hp_overkill": 300,
        "mp": 45,
        "ap": 32,
        "ap_overkill": 64,
        "location": "Mushroom Rock Road / Djose Highroad",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 18, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 14, "eva": 7, "luck": 15
        },
        "gil": 48,
        "steal": {"common": "Soft", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x3 (5,000 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward", "Defense +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire", "Lightning"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Raptor_from_FFX.webp"
    },

    "Red Element": {
        "zanmato_lv": 1,
        "hp": 450,
        "hp_overkill": 675,
        "mp": 130,
        "ap": 32,
        "ap_overkill": 64,
        "location": "Mushroom Rock Road",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 1, "mag": 23, "def": 120, "mdef": 1,
            "acc": 0, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 55,
        "steal": {"common": "Bomb Fragment", "rare": "Bomb Fragment x2"},
        "bribe": ["Bomb Core x1 (11,250 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 0-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Distill Mana"],
        "armor_abilities": ["Fire Ward", "Fireproof"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie"],
        "status_resistances": {
            "Silence": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Lightning", "Water"],
            "immune": [],
            "absorb": ["Fire"]
        },
        "image": "./images/Red_Element_from_FFX.webp"
    },

    "Remora": {
        "zanmato_lv": 1,
        "hp": 3000,
        "hp_overkill": 2108,
        "mp": 22,
        "ap": 830,
        "ap_overkill": 1245,
        "location": "Via Purifico (Underwater)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 25, "def": 30, "mdef": 1,
            "acc": 1, "agl": 11, "eva": 0, "luck": 15
        },
        "gil": 535,
        "steal": {"common": "Dragon Scale", "rare": "Dragon Scale x2"},
        "bribe": ["Water Gem x20 (75,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "2-3 slots, 1-2 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Strength +3%", "Strength +5%"],
        "armor_abilities": ["Zombie Ward", "Defense +5%"],
        "immunities": ["Sleep", "Capture"],
        "status_resistances": {
            "Darkness": 95,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Remora-enemy-ffx.webp"
    },

    "Sahagin (Baaj Temple)": {
        "zanmato_lv": 1,
        "hp": 100,
        "hp_overkill": 200,
        "mp": 5,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Submerged Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 3, "mag": 1, "def": 1, "mdef": 1,
            "acc": 25, "agl": 5, "eva": 0, "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Poison", "Doom", "Sensor", "Scan", "Bribe", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sahagin_underwater_from_FFX.webp"
    },

    "Sahagin (Via Purifico (Land))": {
        "zanmato_lv": 1,
        "hp": 1380,
        "hp_overkill": 2070,
        "mp": 20,
        "ap": 200,
        "ap_overkill": 400,
        "location": "Via Purifico",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 28, "mag": 24, "def": 15, "mdef": 1,
            "acc": 1, "agl": 15, "eva": 0, "luck": 15
        },
        "gil": 180,
        "steal": {"common": "Fish Scale x2", "rare": "Dragon Scale x2"},
        "bribe": ["Water Gem x8 (34,500 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Water Ward", "HP +5%"],
        "immunities": ["Capture"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sahagin_land_from_FFX.webp"
    },

    "Sahagin (Via Purifico (Underwater))": {
        "zanmato_lv": 1,
        "hp": 380,
        "hp_overkill": 570,
        "mp": 20,
        "ap": 200,
        "ap_overkill": 400,
        "location": "Via Purifico",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 13, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 18, "eva": 0, "luck": 15
        },
        "gil": 200,
        "steal": {"common": "Fish Scale", "rare": "Dragon Scale"},
        "bribe": ["Water Gem x3 (9,500 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Water Ward", "HP +5%"],
        "immunities": ["Capture"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Sahagin_underwater_from_FFX.webp"
    },

    "Sahagin Chief": {
        "zanmato_lv": 1,
        "hp": 170,
        "hp_overkill": 340,
        "mp": 20,
        "ap": 2,
        "ap_overkill": 3,
        "location": "Luca",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 12, "mag": 1, "def": 1, "mdef": 1,
            "acc": 25, "agl": 8, "eva": 0, "luck": 1
        },
        "gil": 20,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Poison", "Petrify", "Doom", "Bribe", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sahagin_land_from_FFX.webp"
    },

    "Sand Wolf": {
        "zanmato_lv": 1,
        "hp": 450,
        "hp_overkill": 675,
        "mp": 55,
        "ap": 310,
        "ap_overkill": 620,
        "location": "Bikanel",
        "monster_arena": "Bikanel",
        "stats": {
            "str": 23, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 23, "eva": 9, "luck": 15
        },
        "gil": 225,
        "steal": {"common": "Sleeping Powder", "rare": "Sleeping Powder x2"},
        "bribe": ["Sleeping Powder x12 (11,250 gil)"],
        "drop": {"common": "Power Sphere x1, Al Bhed Potion x1", "rare": "Power Sphere x1, Al Bhed Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Silence Ward", "Sleep Ward", "Magic Def +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sand_Wolf_from_FFX.webp"
    },

    "Sand Worm": {
        "zanmato_lv": 1,
        "hp": 45000,
        "hp_overkill": 1432,
        "mp": 100,
        "ap": 2000,
        "ap_overkill": 3000,
        "location": "Bikanel",
        "monster_arena": "Bikanel",
        "stats": {
            "str": 30, "mag": 28, "def": 5, "mdef": 5,
            "acc": 1, "agl": 8, "eva": 0, "luck": 15
        },
        "gil": 1000,
        "steal": {"common": "Shadow Gem x2", "rare": "Stamina Spring x2"},
        "bribe": ["Winning Formula x15 (1,125,000 gil)"],
        "drop": {"common": "Ability Sphere x2", "rare": "Lv. 1 Key Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Slowtouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["HP +10%", "Auto-Potion"],
        "immunities": ["Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke"],
        "status_resistances": {
            "Sleep": 80,
            "Darkness": 50,
            "Power Break": 50,
            "Poison": "0 (10 max HP/turn)",
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": ["Ice", "Water"],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sand_Worm-enemy-ffx.webp"
    },

    "Sandragora": {
        "zanmato_lv": 1,
        "hp": 12750,
        "hp_overkill": 1432,
        "mp": 3,
        "ap": 540,
        "ap_overkill": 1080,
        "location": "Bikanel",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 25, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 336,
        "steal": {"common": "Remedy x2", "rare": "Musk x10"},
        "bribe": ["Remedy x99 (318,750 gil)"],
        "drop": {"common": "Al Bhed Potion x2, Mana Sphere x1", "rare": "Al Bhed Potion x2, Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 6.25% chance",
        "weapon_abilities": ["Piercing", "Poisontouch", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Poison Ward", "HP +5%", "HP +10%"],
        "immunities": ["Silence", "Darkness", "Slow", "Zombie", "Power Break", "Threaten", "Provoke", "Capture"],
        "status_resistances": {
            "Sleep": 80,
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 25,
            "Death": 25,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": ["Water"]
        },
        "image": "./images/Sandragora_from_FFX.webp"
    },

    "Shred": {
        "zanmato_lv": 1,
        "hp": 1950,
        "hp_overkill": 2925,
        "mp": 30,
        "ap": 480,
        "ap_overkill": 960,
        "location": "Calm Lands",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 35, "mag": 1, "def": 1, "mdef": 180,
            "acc": 1, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 368,
        "steal": {"common": "Hypello Potion", "rare": "Hypello Potion x2"},
        "bribe": ["Hypello Potion x50 (48,750 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Berserk Ward"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": ["Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Shred_from_FFX.webp"
    },

    "Simurgh": {
        "zanmato_lv": 1,
        "hp": 200,
        "hp_overkill": 300,
        "mp": 27,
        "ap": 48,
        "ap_overkill": 96,
        "location": "Djose Highroad",
        "monster_arena": "Djose Road",
        "stats": {
            "str": 13, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 73,
        "steal": {"common": "Smoke Bomb", "rare": "Smoke Bomb x2"},
        "bribe": ["Smoke Bomb x5 (5,000 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Sensor", "Piercing", "Distill Speed"],
        "armor_abilities": ["Dark Ward", "Magic Def +3%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Simurgh_from_FFX.webp"
    },

    "Sinscale (Enemy)": {
        "zanmato_lv": 4,
        "hp": 100,
        "hp_overkill": 500,
        "mp": 0,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Dream Zanarkand",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 5, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 8, "eva": 0, "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Threaten", "Provoke", "Scan", "Bribe", "Capture"],
        "status_resistances": {
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinscale-enemy-ffx.webp"
    },

    "Sinscale (S.S. Liki)": {
        "zanmato_lv": 1,
        "hp": 200,
        "hp_overkill": 400,
        "mp": 0,
        "ap": 2,
        "ap_overkill": 3,
        "location": "S.S. Liki",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 13, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 12, "eva": 0, "luck": 1
        },
        "gil": 22,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": ["Potion x10 (5,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Threaten", "Doom", "Capture"],
        "status_resistances": {
            "Poison": "0 (25 max HP/turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinscale-enemy-ffx.webp"
    },

    "Sinscale (Underwater)": {
        "zanmato_lv": 1,
        "hp": 100,
        "hp_overkill": 300,
        "mp": 0,
        "ap": 2,
        "ap_overkill": 3,
        "location": "S.S. Liki",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 11, "mag": 1, "def": 1, "mdef": 1,
            "acc": 100, "agl": 1, "eva": 0, "luck": 1
        },
        "gil": 24,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Petrify", "Threaten", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinscale_2-enemy-ffx.webp"
    },

    "Skoll": {
        "zanmato_lv": 1,
        "hp": 1000,
        "hp_overkill": 1500,
        "mp": 60,
        "ap": 480,
        "ap_overkill": 960,
        "location": "Calm Lands",
        "monster_arena": "Calm Lands",
        "stats": {
            "str": 28, "mag": 1, "def": 1, "mdef": 180,
            "acc": 1, "agl": 28, "eva": 10, "luck": 15
        },
        "gil": 420,
        "steal": {"common": "Dream Powder", "rare": "Dream Powder x2"},
        "bribe": ["Dream Powder x12 (25,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Silence Ward", "Sleep Ward"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Skoll_from_FFX.webp"
    },

    "Sleep Sprout": {
        "zanmato_lv": 4,
        "hp": 98000,
        "hp_overkill": 10000,
        "mp": 820,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 3, "mag": 112, "def": 167, "mdef": 203,
            "acc": 1, "agl": 26, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Poison Fang x4", "rare": "Farplane Wind"},
        "bribe": None,
        "drop": {"common": "Teleport Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-4 abilities, 100% chance",
        "weapon_abilities": ["Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Exoray_from_FFX.webp"
    },

    "Snow Flan": {
        "zanmato_lv": 1,
        "hp": 600,
        "hp_overkill": 900,
        "mp": 120,
        "ap": 48,
        "ap_overkill": 96,
        "location": "Djose Highroad",
        "monster_arena": "Djose Road",
        "stats": {
            "str": 1, "mag": 19, "def": 120, "mdef": 1,
            "acc": 1, "agl": 7, "eva": 0, "luck": 15
        },
        "gil": 93,
        "steal": {"common": "Antarctic Wind", "rare": "Antarctic Wind x2"},
        "bribe": ["Arctic Wind x10 (15,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x2"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Icestrike", "Distill Mana"],
        "armor_abilities": ["Ice Ward", "Iceproof"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": ["Lightning", "Water"],
            "immune": [],
            "absorb": ["Ice"]
        },
        "image": "./images/Snow_Flan_from_FFX.webp"
    },

    "Snow Wolf": {
        "zanmato_lv": 1,
        "hp": 400,
        "hp_overkill": 600,
        "mp": 50,
        "ap": 300,
        "ap_overkill": 600,
        "location": "Lake Macalania",
        "monster_arena": "Macalania",
        "stats": {
            "str": 20, "mag": 1, "def": 1, "mdef": 120,
            "acc": 1, "agl": 20, "eva": 8, "luck": 15
        },
        "gil": 192,
        "steal": {"common": "Sleeping Powder", "rare": "Sleeping Powder x2"},
        "bribe": ["Sleeping Powder x11 (10,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Silence Ward", "Sleep Ward", "Magic Def +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Snow_Wolf_from_FFX.webp"
    },

    "Spirit": {
        "zanmato_lv": 1,
        "hp": 10000,
        "hp_overkill": 13560,
        "mp": 700,
        "ap": 4300,
        "ap_overkill": 8600,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 1, "mag": 42, "def": 90, "mdef": 30,
            "acc": 1, "agl": 24, "eva": 0, "luck": 15
        },
        "gil": 1300,
        "steal": {"common": "Stamina Spring", "rare": "Stamina Spring x2"},
        "bribe": ["Twin Stars x10 (250,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Friend Sphere x1"},
        "equipment_drop": "3-4 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Sleeptouch", "Sleepstrike"],
        "armor_abilities": ["Sleepproof", "Magic Def +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Armor Break", "Death", "Sensor", "Scan"],
        "status_resistances": {
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Spirit.webp"
    },

    "Splasher (Single)": {
        "zanmato_lv": 1,
        "hp": 200,
        "hp_overkill": 900,
        "mp": 2,
        "ap": 140,
        "ap_overkill": 280,
        "location": "Mt. Gagazet Cavern",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 14, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 20, "eva": 10, "luck": 15
        },
        "gil": 100,
        "steal": {"common": "Grenade", "rare": "Frag Grenade"},
        "bribe": ["Dragon Scale x4 (5,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1 slot, 0-1 ability, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["HP +5%", "Defense +3%"],
        "immunities": ["Sleep", "Poison"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Splasher_from_FFX.webp"
    },

    "Splasher (Paired)": {
        "zanmato_lv": 1,
        "hp": 400,
        "hp_overkill": 900,
        "mp": 4,
        "ap": 300,
        "ap_overkill": 600,
        "location": "Mt. Gagazet",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 19, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 8, "luck": 15
        },
        "gil": 140,
        "steal": {"common": "Grenade", "rare": "Frag Grenade"},
        "bribe": ["Dragon Scale x8 (10,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1 slot, 0-1 ability, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["HP +5%", "Defense +3%"],
        "immunities": ["Sleep", "Poison"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Splasher_from_FFX.webp"
    },

    "Splasher (Trio)": {
        "zanmato_lv": 1,
        "hp": 600,
        "hp_overkill": 900,
        "mp": 6,
        "ap": 440,
        "ap_overkill": 880,
        "location": "Mt. Gagazet",
        "monster_arena": "Mt. Gagazet",
        "stats": {
            "str": 24, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 15, "eva": 6, "luck": 15
        },
        "gil": 200,
        "steal": {"common": "Grenade", "rare": "Frag Grenade"},
        "bribe": ["Dragon Scale x12 (15,000 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1 slot, 0-1 ability, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["HP +5%", "Defense +3%"],
        "immunities": ["Sleep", "Poison"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire"],
            "immune": ["Water"],
            "absorb": []
        },
        "image": "./images/Splasher_from_FFX.webp"
    },

    "Stratoavis": {
        "zanmato_lv": 4,
        "hp": 320000,
        "hp_overkill": 10000,
        "mp": 115,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 73, "mag": 32, "def": 41, "mdef": 82,
            "acc": 100, "agl": 32, "eva": 5, "luck": 18
        },
        "gil": 0,
        "steal": {"common": "Smoke Bomb x3", "rare": "Stamina Spring x2"},
        "bribe": None,
        "drop": {"common": "Amulet x2", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 2-3 abilities, 100% chance",
        "weapon_abilities": ["Magic +5%", "Magic +10%", "Magic +20%"],
        "armor_abilities": ["HP +10%", "HP +20%", "HP +30%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Slow": 90,
            "Power Break": 90,
            "Magic Break": 90,
            "Armor Break": 90,
            "Mental Break": 90,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Zu_from_FFX.webp"
    },

    "Swamp Mafdet": {
        "zanmato_lv": 1,
        "hp": 850,
        "hp_overkill": 1275,
        "mp": 1,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Via Purifico",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 1, "def": 1, "mdef": 120,
            "acc": 0, "agl": 6, "eva": 1, "luck": 15
        },
        "gil": 290,
        "steal": {"common": "Hi-Potion", "rare": "Hypello Potion"},
        "bribe": ["Hypello Potion x33 (21,250 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Berserk Ward", "Defense +5%"],
        "immunities": ["Capture"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice", "Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mafdet_from_FFX.webp"
    },

    "Tanket": {
        "zanmato_lv": 4,
        "hp": 900000,
        "hp_overkill": 10000,
        "mp": 0,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 103, "mag": 3, "def": 100, "mdef": 250,
            "acc": 100, "agl": 41, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Light Curtain x4", "rare": "Lunar Curtain x4"},
        "bribe": None,
        "drop": {"common": "Defense Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Armor Break": 90,
            "Mental Break": 99,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Murussu_from_FFX.webp"
    },

    "Th'uban": {
        "zanmato_lv": 5,
        "hp": 3000000,
        "hp_overkill": 99999,
        "mp": 85,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 102, "mag": 212, "def": 80, "mdef": 80,
            "acc": 180, "agl": 53, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Teleport Sphere"},
        "bribe": None,
        "drop": {"common": "Underdog's Secret x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Triple AP", "Triple Overdrive"],
        "armor_abilities": ["HP +10%", "HP +20%", "HP +30%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Reflect", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Th'uban_from_FFX.webp"
    },

    "Thorn": {
        "zanmato_lv": 1,
        "hp": 4080,
        "hp_overkill": 4060,
        "mp": 120,
        "ap": 830,
        "ap_overkill": 1660,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 1, "mag": 25, "def": 1, "mdef": 1,
            "acc": 1, "agl": 8, "eva": 0, "luck": 15
        },
        "gil": 530,
        "steal": {"common": "Silence Grenade x2", "rare": "Ether"},
        "bribe": ["Turbo Ether x16 (102,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 4.3% chance",
        "weapon_abilities": ["Piercing", "Sleeptouch", "Strength +3%", "Strength +5%", "Magic +3%", "Magic +5%"],
        "armor_abilities": ["Sleep Ward", "MP +5%"],
        "immunities": ["Silence", "Darkness", "Poison", "Zombie", "Magic Break"],
        "status_resistances": {
            "Sleep": 95,
            "Petrify": 25,
            "Death": 25,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": ["Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Thorn_from_FFX.webp"
    },

    "Thunder Flan": {
        "zanmato_lv": 1,
        "hp": 450,
        "hp_overkill": 675,
        "mp": 50,
        "ap": 24,
        "ap_overkill": 48,
        "location": "Mi'ihen Highroad / Mushroom Rock Road",
        "monster_arena": "Mushroom Rock Road",
        "stats": {
            "str": 1, "mag": 17, "def": 120, "mdef": 1,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 50,
        "steal": {"common": "Electro Marble", "rare": "Electro Marble x2"},
        "bribe": ["Lightning Marble x8 (11,250 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike", "Distill Mana"],
        "armor_abilities": ["Lightning Ward", "Lightningproof"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": ["Fire", "Ice"],
            "immune": [],
            "absorb": ["Lightning"]
        },
        "image": "./images/Thunder_Flan_from_FFX.webp"
    },

    "Tonberry": {
        "zanmato_lv": 1,
        "hp": 13500,
        "hp_overkill": 4060,
        "mp": 1,
        "ap": 6500,
        "ap_overkill": 9750,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 40, "mag": 43, "def": 10, "mdef": 10,
            "acc": 1, "agl": 14, "eva": 0, "luck": 15
        },
        "gil": 2000,
        "steal": {"common": "Hi-Potion", "rare": "Farplane Shadow"},
        "bribe": ["Amulet x2 (337,500 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Lv. 2 Key Sphere x1"},
        "equipment_drop": "2-3 slots, 0-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Deathtouch", "Slowtouch"],
        "armor_abilities": ["Death Ward"],
        "immunities": ["Silence", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Delay", "Berserk"],
        "status_resistances": {
            "Sleep": 20,
            "Doom": "0 (25 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Tonberry-enemy-ffx.webp"
    },

    "Valaha": {
        "zanmato_lv": 1,
        "hp": 8700,
        "hp_overkill": 4060,
        "mp": 29,
        "ap": 1320,
        "ap_overkill": 1980,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 36, "mag": 21, "def": 1, "mdef": 1,
            "acc": 1, "agl": 23, "eva": 0, "luck": 15
        },
        "gil": 720,
        "steal": {"common": "Hi-Potion", "rare": "Hi-Potion x2"},
        "bribe": ["X-Potion x60 (217,500 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Silencetouch", "Distill Ability"],
        "armor_abilities": ["HP +10%"],
        "immunities": ["Slow", "Magic Break", "Death"],
        "status_resistances": {
            "Sleep": 80,
            "Darkness": 95,
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 25,
            "Doom": "0 (2 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Valaha_from_FFX.webp"
    },

    "Varuna": {
        "zanmato_lv": 1,
        "hp": 56000,
        "hp_overkill": 11036,
        "mp": 1,
        "ap": 19500,
        "ap_overkill": 29250,
        "location": "Omega Ruins / Inside Sin",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 13, "mag": 38, "def": 70, "mdef": 40,
            "acc": 1, "agl": 26, "eva": 0, "luck": 15
        },
        "gil": 1780,
        "steal": {"common": "Farplane Wind", "rare": "Shining Gem"},
        "bribe": ["Megalixir x20 (1,400,000 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Lv. 2 Key Sphere x1"},
        "equipment_drop": "3-4 slots, 0-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Magic +10%", "Double Overdrive"],
        "armor_abilities": ["SOS Shell", "Magic Def +10%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Slow", "Zombie", "Magic Break", "Armor Break", "Threaten", "Death", "Provoke", "Reflect", "Delay", "Berserk"],
        "status_resistances": {
            "Petrify": 80,
            "Doom": "0 (7 turns)"
        },
        "elemental_affinities": {
            "weak": ["Holy"],
            "resisted": ["Fire", "Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Varuna_from_FFX.webp"
    },

    "Vidatu": {
        "zanmato_lv": 4,
        "hp": 95000,
        "hp_overkill": 10000,
        "mp": 840,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 12, "mag": 77, "def": 230, "mdef": 230,
            "acc": 110, "agl": 33, "eva": 80, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Lightning Gem x4", "rare": "Mana Tonic"},
        "bribe": None,
        "drop": {"common": "MP Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Double AP"],
        "armor_abilities": ["MP +10%", "MP +20%", "MP +30%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Magic Break": 99,
            "Armor Break": 80,
            "Mental Break": 80,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Imp_from_FFX.webp"
    },

    "Vorban": {
        "zanmato_lv": 4,
        "hp": 630000,
        "hp_overkill": 10000,
        "mp": 120,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 95, "mag": 75, "def": 100, "mdef": 100,
            "acc": 80, "agl": 33, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Healing Spring x2", "rare": "Stamina Tablet"},
        "bribe": None,
        "drop": {"common": "Friend Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Barbatos-enemy-ffx.webp"
    },

    "Vouivre (Luca)": {
        "zanmato_lv": 1,
        "hp": 255,
        "hp_overkill": 500,
        "mp": 1,
        "ap": 14,
        "ap_overkill": 21,
        "location": "Luca / Mi'ihen Highroad / Mushroom Rock Road",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 20, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 3, "eva": 0, "luck": 1
        },
        "gil": 50,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Icestrike"],
        "armor_abilities": ["Slow Ward", "HP +5%"],
        "immunities": ["Sensor", "Scan", "Bribe"],
        "status_resistances": {
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Vouivre-enemy-ffx.webp"
    },

    "Vouivre (Mi'ihen Highroad)": {
        "zanmato_lv": 1,
        "hp": 255,
        "hp_overkill": 383,
        "mp": 22,
        "ap": 24,
        "ap_overkill": 48,
        "location": "Luca / Mi'ihen Highroad / Mushroom Rock Road",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 20, "mag": 21, "def": 1, "mdef": 120,
            "acc": 15, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 60,
        "steal": {"common": "Potion", "rare": "Silver Hourglass"},
        "bribe": ["Silver Hourglass x10 (6,375 gil)"],
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Power"],
        "armor_abilities": ["Slow Ward", "HP +5%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Vouivre-enemy-ffx.webp"
    },

    "Warrior Monk (Rifle)": {
        "zanmato_lv": 1,
        "hp": 1400,
        "hp_overkill": 2100,
        "mp": 20,
        "ap": 420,
        "ap_overkill": 840,
        "location": "Bevelle",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 20, "def": 1, "mdef": 1,
            "acc": 1, "agl": 19, "eva": 0, "luck": 15
        },
        "gil": 460,
        "steal": {"common": "Hi-Potion x2", "rare": "Purifying Salt"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic Counter"],
        "armor_abilities": ["Death Ward", "Magic Def +5%"],
        "immunities": ["Silence", "Power Break", "Magic Break", "Provoke", "Bribe", "Capture"],
        "status_resistances": {
            "Sleep": 50,
            "Darkness": 95,
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 25,
            "Zombie": 25,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Warrior_Monk_Rifle.webp"
    },

    "Warrior Monk (Flamethrower)": {
        "zanmato_lv": 1,
        "hp": 1400,
        "hp_overkill": 2100,
        "mp": 20,
        "ap": 420,
        "ap_overkill": 840,
        "location": "Bevelle",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 20, "def": 1, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 460,
        "steal": {"common": "Hi-Potion x2", "rare": "Purifying Salt"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic Counter"],
        "armor_abilities": ["Death Ward", "Magic Def +5%"],
        "immunities": ["Silence", "Power Break", "Magic Break", "Provoke", "Bribe", "Capture"],
        "status_resistances": {
            "Sleep": 50,
            "Darkness": 95,
            "Poison": "25 (25 max HP/turn)",
            "Petrify": 25,
            "Zombie": 25,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Warrior_Monk_Flamethrower.webp"
    },

    "Wasp": {
        "zanmato_lv": 1,
        "hp": 360,
        "hp_overkill": 540,
        "mp": 30,
        "ap": 240,
        "ap_overkill": 480,
        "location": "Macalania Woods",
        "monster_arena": "Macalania",
        "stats": {
            "str": 17, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 18, "eva": 13, "luck": 15
        },
        "gil": 142,
        "steal": {"common": "Hi-Potion", "rare": "Poison Fang"},
        "bribe": ["Poison Fang x3 (9,000 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Speed"],
        "armor_abilities": ["Poison Ward", "MP +10%"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Wasp_from_FFX.webp"
    },

    "Water Flan": {
        "zanmato_lv": 1,
        "hp": 315,
        "hp_overkill": 473,
        "mp": 30,
        "ap": 2,
        "ap_overkill": 4,
        "location": "Besaid",
        "monster_arena": "Besaid",
        "stats": {
            "str": 3, "mag": 15, "def": 120, "mdef": 1,
            "acc": 1, "agl": 5, "eva": 0, "luck": 15
        },
        "gil": 18,
        "steal": {"common": "Fish Scale", "rare": "Dragon Scale"},
        "bribe": ["Water Gem x2 (7,875 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Waterstrike", "Distill Mana"],
        "armor_abilities": ["Water Ward", "Waterproof"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire", "Ice"],
            "immune": [],
            "absorb": ["Water"]
        },
        "image": "./images/Aqua_Flan_from_FFX.webp"
    },

    "White Element": {
        "zanmato_lv": 1,
        "hp": 390,
        "hp_overkill": 585,
        "mp": 120,
        "ap": 20,
        "ap_overkill": 40,
        "location": "Mi'ihen Highroad",
        "monster_arena": "Mi'ihen Highroad",
        "stats": {
            "str": 1, "mag": 22, "def": 120, "mdef": 1,
            "acc": 1, "agl": 5, "eva": 0, "luck": 15
        },
        "gil": 48,
        "steal": {"common": "Antarctic Wind", "rare": "Antarctic Wind x2"},
        "bribe": ["Arctic Wind x7 (9,750 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 0-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Icestrike", "Distill Mana"],
        "armor_abilities": ["Ice Ward", "Iceproof"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Berserk"],
        "status_resistances": {
            "Silence": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": ["Lightning", "Water"],
            "immune": [],
            "absorb": ["Ice"]
        },
        "image": "./images/White_Element_from_FFX.webp"
    },

    "Worker": {
        "zanmato_lv": 1,
        "hp": 300,
        "hp_overkill": 600,
        "mp": 1,
        "ap": 7,
        "ap_overkill": 10,
        "location": "Luca",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 12, "mag": 1, "def": 100, "mdef": 1,
            "acc": 15, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 85,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Hi-Potion x1", "rare": "X-Potion x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Worker-enemy-ffx.webp"
    },

    "Wraith": {
        "zanmato_lv": 1,
        "hp": 22222,
        "hp_overkill": 13560,
        "mp": 3500,
        "ap": 3100,
        "ap_overkill": 6200,
        "location": "Inside Sin / Omega Ruins",
        "monster_arena": "Inside Sin",
        "stats": {
            "str": 1, "mag": 24, "def": 150, "mdef": 50,
            "acc": 1, "agl": 25, "eva": 0, "luck": 15
        },
        "gil": 1070,
        "steal": {"common": "Farplane Shadow", "rare": "Farplane Wind"},
        "bribe": ["Farplane Wind x60 (555,550 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 15.63% chance",
        "weapon_abilities": ["Piercing", "Magic +5%", "Magic +10%", "Distill Mana"],
        "armor_abilities": ["Death Ward", "No Encounters"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Berserk"],
        "status_resistances": {
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": ["Holy"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Wraith_from_FFX.webp"
    },

    "Xiphos": {
        "zanmato_lv": 1,
        "hp": 2700,
        "hp_overkill": 1432,
        "mp": 5,
        "ap": 520,
        "ap_overkill": 720,
        "location": "Macalania Woods",
        "monster_arena": "Macalania",
        "stats": {
            "str": 20, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 220,
        "steal": {"common": "Hi-Potion", "rare": "Mega-Potion"},
        "bribe": ["Megalixir x1 (67,500 gil)"],
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x2"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Strength +3%", "Magic +3%", "SOS Overdrive"],
        "armor_abilities": ["Defense +5%"],
        "immunities": ["Sleep", "Poison"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 50,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Xiphos_from_FFX.webp"
    },

    "YAT-97": {
        "zanmato_lv": 1,
        "hp": 3700,
        "hp_overkill": 5550,
        "mp": 1,
        "ap": 3200,
        "ap_overkill": 4800,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 41, "mag": 38, "def": 1, "mdef": 120,
            "acc": 1, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 1080,
        "steal": {"common": "Holy Water x3", "rare": "Ether x2"},
        "bribe": ["Ether x16 (92,500 gil)"],
        "drop": {"common": "Phoenix Down x2", "rare": "Mega Phoenix x1"},
        "equipment_drop": "2-4 slots, 0-2 abilities, 11.72% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Armor Break", "Threaten", "Death", "Provoke", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (15 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/YAT-97.webp"
    },

    "YAT-99": {
        "zanmato_lv": 1,
        "hp": 2700,
        "hp_overkill": 2108,
        "mp": 1,
        "ap": 1870,
        "ap_overkill": 2805,
        "location": "Bevelle",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 40, "mag": 32, "def": 1, "mdef": 120,
            "acc": 1, "agl": 9, "eva": 0, "luck": 15
        },
        "gil": 1300,
        "steal": {"common": "Remedy", "rare": "Ether"},
        "bribe": ["Ether x10 (67,500 gil)"],
        "drop": {"common": "Phoenix Down x1", "rare": "Mega Phoenix x1"},
        "equipment_drop": "2-3 slots, 0-2 abilities, 11.72% chance",
        "weapon_abilities": ["Piercing", "Strength +3%", "Strength +5%", "Magic +3%", "Magic +5%"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (15 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/YAT-99.webp"
    },

    "Yellow Element": {
        "zanmato_lv": 1,
        "hp": 300,
        "hp_overkill": 450,
        "mp": 100,
        "ap": 9,
        "ap_overkill": 18,
        "location": "Kilika Woods",
        "monster_arena": "Kilika",
        "stats": {
            "str": 1, "mag": 18, "def": 120, "mdef": 1,
            "acc": 1, "agl": 5, "eva": 0, "luck": 15
        },
        "gil": 33,
        "steal": {"common": "Electro Marble", "rare": "Lightning Marble"},
        "bribe": ["Lightning Marble x6 (7,500 gil)"],
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 0-2 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike", "Distill Mana"],
        "armor_abilities": ["Lightning Ward"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Berserk"],
        "status_resistances": {
            "Silence": 20,
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Water"],
            "resisted": ["Fire", "Ice"],
            "immune": [],
            "absorb": ["Lightning"]
        },
        "image": "./images/Yellow_Element_from_FFX.webp"
    },

    "YKT-11": {
        "zanmato_lv": 1,
        "hp": 6200,
        "hp_overkill": 8848,
        "mp": 1,
        "ap": 3200,
        "ap_overkill": 4800,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 34, "mag": 1, "def": 1, "mdef": 60,
            "acc": 1, "agl": 25, "eva": 0, "luck": 15
        },
        "gil": 1080,
        "steal": {"common": "Holy Water x3", "rare": "Ether x2"},
        "bribe": ["Elixir x12 (155,000 gil)"],
        "drop": {"common": "Hi-Potion x2", "rare": "Mega-Potion x1"},
        "equipment_drop": "2-4 slots, 0-2 abilities, 11.72% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Darkness": 95,
            "Doom": "0 (15 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/YKT-11.webp"
    },

    "YKT-63": {
        "zanmato_lv": 1,
        "hp": 4200,
        "hp_overkill": 2108,
        "mp": 1,
        "ap": 1870,
        "ap_overkill": 2805,
        "location": "Bevelle",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 40, "mag": 1, "def": 1, "mdef": 60,
            "acc": 1, "agl": 22, "eva": 0, "luck": 15
        },
        "gil": 1300,
        "steal": {"common": "Remedy", "rare": "Ether"},
        "bribe": ["Elixir x8 (105,000 gil)"],
        "drop": {"common": "Hi-Potion x1", "rare": "Mega-Potion x1"},
        "equipment_drop": "2-3 slots, 0-2 abilities, 11.72% chance",
        "weapon_abilities": ["Piercing", "Strength +3%", "Strength +5%", "Magic +3%", "Magic +5%"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Berserk", "Capture"],
        "status_resistances": {
            "Darkness": 95,
            "Doom": "0 (15 turns)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Water"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/YKT-63.webp"
    },

    "Yowie": {
        "zanmato_lv": 1,
        "hp": 900,
        "hp_overkill": 1350,
        "mp": 95,
        "ap": 810,
        "ap_overkill": 1620,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Stolen Fayth Cavern",
        "stats": {
            "str": 26, "mag": 1, "def": 1, "mdef": 180,
            "acc": 1, "agl": 29, "eva": 10, "luck": 15
        },
        "gil": 480,
        "steal": {"common": "Soft", "rare": "Petrify Grenade"},
        "bribe": ["Petrify Grenade x12 (22,500 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Power Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward"],
        "immunities": [],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25 max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Ice"],
            "resisted": ["Fire", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yowie_from_FFX.webp"
    },

    "Zaurus": {
        "zanmato_lv": 1,
        "hp": 7850,
        "hp_overkill": 11775,
        "mp": 1,
        "ap": 5000,
        "ap_overkill": 10000,
        "location": "Omega Ruins",
        "monster_arena": "Omega Dungeon",
        "stats": {
            "str": 38, "mag": 1, "def": 30, "mdef": 150,
            "acc": 1, "agl": 46, "eva": 14, "luck": 15
        },
        "gil": 950,
        "steal": {"common": "Petrify Grenade x2", "rare": "Petrify Grenade x3"},
        "bribe": ["Rename Card x10 (196,250 gil)"],
        "drop": {"common": "Speed Sphere x1", "rare": "Speed Sphere x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 3.13% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Distill Speed"],
        "armor_abilities": ["Slow Ward", "Slowproof"],
        "immunities": ["Sensor", "Scan"],
        "status_resistances": {
            "Silence": 20,
            "Sleep": 20,
            "Darkness": 20,
            "Poison": "0 (25% max HP/turn)",
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yowie_from_FFX.webp"
    },

    "Zu (Oasis)": {
        "zanmato_lv": 1,
        "hp": 12000,
        "hp_overkill": 12000,
        "mp": 50,
        "ap": 1200,
        "ap_overkill": 1800,
        "location": "Bikanel",
        "monster_arena": "Bikanel",
        "stats": {
            "str": 32, "mag": 30, "def": 20, "mdef": 20,
            "acc": 1, "agl": 8, "eva": 0, "luck": 15
        },
        "gil": 1200,
        "steal": {"common": "Smoke Bomb x3", "rare": "Smoke Bomb x4"},
        "bribe": None,
        "drop": {"common": "Al Bhed Potion x2, Power Sphere x1", "rare": "Al Bhed Potion x2, Power Sphere x2"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Darktouch", "Strength +3%", "Magic +3%"],
        "armor_abilities": ["Dark Ward"],
        "immunities": ["Sleep", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Reflect", "Bribe"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 20,
            "Poison": "25 (25 max HP/turn)",
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Zu_from_FFX.webp"
    },

    "Zu (East/Central/West)": {
        "zanmato_lv": 1,
        "hp": 18000,
        "hp_overkill": 1432,
        "mp": 50,
        "ap": 1200,
        "ap_overkill": 1800,
        "location": "Bikanel",
        "monster_arena": "Bikanel",
        "stats": {
            "str": 37, "mag": 35, "def": 20, "mdef": 20,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 1200,
        "steal": {"common": "Smoke Bomb x3", "rare": "Smoke Bomb x4"},
        "bribe": ["Skill Sphere x2 (450,000 gil)"],
        "drop": {"common": "Al Bhed Potion x2, Power Sphere x1", "rare": "Al Bhed Potion x4, Power Sphere x2"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Darktouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Dark Ward"],
        "immunities": ["Sleep", "Petrify", "Zombie", "Threaten", "Death", "Provoke"],
        "status_resistances": {
            "Silence": 20,
            "Darkness": 95,
            "Poison": "25 (25 max HP/turn)",
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Zu_from_FFX.webp"
    },

    "Abaddon": {
        "zanmato_lv": 4,
        "hp": 380000,
        "hp_overkill": 10000,
        "mp": 780,
        "ap": 8000,
        "ap_overkill": 16000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 40, "mag": 95, "def": 180, "mdef": 160,
            "acc": 130, "agl": 120, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Purifying Salt x3", "rare": "Shining Gem"},
        "bribe": None,
        "drop": {"common": "Mana Tablet x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Magic +5%", "Magic +10%", "Magic +20%"],
        "armor_abilities": ["Magic Def +5%", "Magic Def +10%", "Magic Def +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Varuna_from_FFX.webp"
    },

    "Abyss Worm": {
        "zanmato_lv": 4,
        "hp": 480000,
        "hp_overkill": 12000,
        "mp": 200,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 60, "mag": 93, "def": 24, "mdef": 63,
            "acc": 120, "agl": 22, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Shadow Gem x4", "rare": "Stamina Tablet"},
        "bribe": None,
        "drop": {"common": "Stamina Tonic x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Land_Worm_from_FFX.webp"
    },

    "Cactuar King": {
        "zanmato_lv": 4,
        "hp": 100000,
        "hp_overkill": 10000,
        "mp": 0,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 255, "mag": 255, "def": 100, "mdef": 255,
            "acc": 180, "agl": 80, "eva": 240, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Chocobo Wing x2", "rare": "Designer Wallet"},
        "bribe": None,
        "drop": {"common": "Blessed Gem x3", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "absorb": []
        },
        "image": "./images/Qactuar_FFX.webp"
    },

    "Catoblepas": {
        "zanmato_lv": 4,
        "hp": 550000,
        "hp_overkill": 10000,
        "mp": 160,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 76, "mag": 58, "def": 33, "mdef": 27,
            "acc": 180, "agl": 47, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Healing Spring x3", "rare": "Stamina Tonic"},
        "bribe": None,
        "drop": {"common": "Three Stars x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 2-4 abilities, 100% chance",
        "weapon_abilities": ["Deathstrike", "Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Deathproof", "Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Power Break": 50,
            "Magic Break": 50,
            "Armor Break": 50,
            "Mental Break": 50,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Behemoth_from_FFX.webp"
    },

    "Chimerageist": {
        "zanmato_lv": 4,
        "hp": 120000,
        "hp_overkill": 10000,
        "mp": 30,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Area Conquest",
        "stats": {
            "str": 66, "mag": 68, "def": 10, "mdef": 10,
            "acc": 180, "agl": 29, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Mana Spring x2", "rare": "Stamina Spring x2"},
        "bribe": None,
        "drop": {"common": "Return Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Firestrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["Fire Eater", "Water Eater", "Ice Eater"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Power Break": 50,
            "Magic Break": 50,
            "Armor Break": 50,
            "Mental Break": 50,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": ["Fire", "Ice", "Lightning", "Water"],
            "absorb": []
        },
        "image": "./images/Chimera_Brain_from_FFX.webp"
    },

    "Bomb King": {
        "zanmato_lv": 4,
        "hp": 480000,
        "hp_overkill": 10000,
        "mp": 780,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 73, "mag": 71, "def": 200, "mdef": 200,
            "acc": 150, "agl": 46, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Fire Gem x4", "rare": "Shining Gem"},
        "bribe": None,
        "drop": {"common": "Door to Tomorrow x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Strength +5%", "Strength +10%", "Strength +20%"],
        "armor_abilities": ["Defense +5%", "Defense +10%", "Defense +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bomb_from_FFX.webp"
    },

    "Fafnir": {
        "zanmato_lv": 4,
        "hp": 1100000,
        "hp_overkill": 13000,
        "mp": 30,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 76, "mag": 109, "def": 30, "mdef": 130,
            "acc": 160, "agl": 38, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Gold Hourglass x2", "rare": "Stamina Spring x2"},
        "bribe": None,
        "drop": {"common": "Light Curtain x20", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1-4 abilities, 100% chance",
        "weapon_abilities": ["Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["Fire Eater", "Water Eater", "Ice Eater"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Power Break": 95,
            "Magic Break": 95,
            "Armor Break": 95,
            "Mental Break": 95,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Nidhogg_from_FFX.webp"
    },

    "Fenrir": {
        "zanmato_lv": 4,
        "hp": 850000,
        "hp_overkill": 99999,
        "mp": 300,
        "ap": 10000,
        "ap_overkill": 10000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 73, "mag": 12, "def": 40, "mdef": 165,
            "acc": 200, "agl": 200, "eva": 60, "luck": 30
        },
        "gil": 0,
        "steal": {"common": "Chocobo Feather x2", "rare": "Chocobo Wing"},
        "bribe": None,
        "drop": {"common": "Agility Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 2-4 abilities, 100% chance",
        "weapon_abilities": ["Deathstrike", "Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Deathproof", "Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Armor Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Magic Break": 99,
            "Mental Break": 99,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bandersnatch_from_FFX.webp"
    },

    "Jormungand (Species Conquest)": {
        "zanmato_lv": 4,
        "hp": 520000,
        "hp_overkill": 10000,
        "mp": 63,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 77, "mag": 80, "def": 33, "mdef": 186,
            "acc": 130, "agl": 53, "eva": 6, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Petrify Grenade x4", "rare": "Three Stars"},
        "bribe": None,
        "drop": {"common": "Supreme Gem x2", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-4 abilities, 100% chance",
        "weapon_abilities": ["Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Power Break": 90,
            "Magic Break": 90,
            "Armor Break": 90,
            "Mental Break": 90,
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Anacondaur_from_FFX.webp"
    },

    "Kottos": {
        "zanmato_lv": 4,
        "hp": 440000,
        "hp_overkill": 15000,
        "mp": 20,
        "ap": 8000,
        "ap_overkill": 8000,
        "location": "Monster Arena",
        "monster_arena": "Species Conquest",
        "stats": {
            "str": 88, "mag": 12, "def": 60, "mdef": 1,
            "acc": 150, "agl": 36, "eva": 0, "luck": 25
        },
        "gil": 0,
        "steal": {"common": "Stamina Spring x4", "rare": "Soul Spring x2"},
        "bribe": None,
        "drop": {"common": "Healing Spring x20", "rare": "Dark Matter x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Counterattack", "Evade & Counter", "Magic Counter"],
        "armor_abilities": ["HP +10%", "HP +20%", "HP +30%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (200 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/FFX_bashura.webp"
    },

    "Catastrophe (Shell)": {
        "zanmato_lv": 5,
        "hp": 2200000,
        "hp_overkill": 99999,
        "mp": 380,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 120, "mag": 77, "def": 80, "mdef": 80,
            "acc": 150, "agl": 34, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Lv. 2 Key Sphere"},
        "bribe": None,
        "drop": {"common": "Designer Wallet x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-4 abilities, 100% chance",
        "weapon_abilities": ["Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Catastrophe-ffx-open-enemy.webp"
    },

    "Catastrophe (Open)": {
        "zanmato_lv": 5,
        "hp": 2200000,
        "hp_overkill": 99999,
        "mp": 380,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 120, "mag": 77, "def": 80, "mdef": 80,
            "acc": 150, "agl": 50, "eva": 0, "luck": 30
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Lv. 2 Key Sphere"},
        "bribe": None,
        "drop": {"common": "Designer Wallet x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-4 abilities, 100% chance",
        "weapon_abilities": ["Darkstrike", "Silencestrike", "Sleepstrike", "Poisonstrike", "Stonestrike", "Zombiestrike", "Slowstrike"],
        "armor_abilities": ["Darkproof", "Silenceproof", "Sleepproof", "Poisonproof", "Stoneproof", "Zombieproof", "Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Catastrophe-ffx-open-enemy.webp"
    },

    "Earth Eater": {
        "zanmato_lv": 5,
        "hp": 1300000,
        "hp_overkill": 99999,
        "mp": 30,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 117, "mag": 186, "def": 200, "mdef": 210,
            "acc": 120, "agl": 47, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Lv. 1 Key Sphere"},
        "bribe": None,
        "drop": {"common": "Fortune Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Triple Overdrive"],
        "armor_abilities": ["Auto-Potion"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Earth_Eater_from_FFX.webp"
    },

    "Nemesis": {
        "zanmato_lv": 5,
        "hp": 10000000,
        "hp_overkill": 99999,
        "mp": 9999,
        "ap": 55000,
        "ap_overkill": 55000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 255, "mag": 255, "def": 150, "mdef": 150,
            "acc": 150, "agl": 200, "eva": 0, "luck": 1
        },
        "gil": 0,
        "steal": {"common": "Lv. 4 Key Sphere", "rare": "Warp Sphere"},
        "bribe": None,
        "drop": {"common": "Warp Sphere x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Break Damage Limit"],
        "armor_abilities": ["Break HP Limit"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire", "Ice", "Lightning", "Water", "Holy"]
        },
        "image": "./images/FFX_Nemesis.PNG.webp"
    },

    "Shinryu": {
        "zanmato_lv": 5,
        "hp": 2000000,
        "hp_overkill": 99999,
        "mp": 72,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 92, "mag": 86, "def": 60, "mdef": 98,
            "acc": 200, "agl": 70, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Three Stars"},
        "bribe": None,
        "drop": {"common": "Wings to Discovery x1", "rare": "Dark Matter x1"},
        "equipment_drop": "2-4 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Double AP"],
        "armor_abilities": ["Auto-Med"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Shinryu-ffx-enemy.webp"
    },

    "Ultima Buster (Body)": {
        "zanmato_lv": 5,
        "hp": 5000000,
        "hp_overkill": 99999,
        "mp": 140,
        "ap": 50000,
        "ap_overkill": 50000,
        "location": "Monster Arena",
        "monster_arena": "Original",
        "stats": {
            "str": 168, "mag": 178, "def": 1, "mdef": 71,
            "acc": 130, "agl": 72, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Gambler's Spirit", "rare": "Lv. 3 Key Sphere"},
        "bribe": None,
        "drop": {"common": "Winning Formula x1", "rare": "Dark Matter x1"},
        "equipment_drop": "3-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Triple AP", "Overdrive → AP", "Triple Overdrive"],
        "armor_abilities": ["Break MP Limit"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (255 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ultima_Buster.webp"
    },

    "Ultima Buster (Head)": {
        "zanmato_lv": 1,
        "hp": 80000,
        "hp_overkill": 1,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Monster Arena",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 178, "def": 1, "mdef": 1,
            "acc": 1, "agl": 80, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ultima_Buster.webp"
    },

    "Ultima Buster (Arms)": {
        "zanmato_lv": 1,
        "hp": 80000,
        "hp_overkill": 1,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Monster Arena",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 1, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (3 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ultima_Buster.webp"
    },

    "Anima (Macalania)": {
        "zanmato_lv": 4,
        "hp": 18000,
        "hp_overkill": 1400,
        "mp": 50,
        "ap": 2500,
        "ap_overkill": 3750,
        "location": "Macalania Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 25, "mag": 20, "def": 1, "mdef": 1,
            "acc": 30, "agl": 25, "eva": 0, "luck": 20
        },
        "gil": 3000,
        "steal": {"common": "Silence Grenade", "rare": "Farplane Shadow"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Darktouch", "Silencetouch", "Sleeptouch"],
        "armor_abilities": ["Dark Ward", "Silence Ward", "Sleep Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Anima-enemy-ffx.webp"
    },

    "Anima (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 54000,
        "hp_overkill": 54000,
        "mp": 3000,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 38, "mag": 60, "def": 1, "mdef": 1,
            "acc": 1, "agl": 15, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Anima-enemy-ffx.webp"
    },

    "Anima (Sin)": {
        "zanmato_lv": 3,
        "hp": "Varies",
        "hp_overkill": 168,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Anima-enemy-ffx.webp"
    },

    "Bahamut (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 35000,
        "hp_overkill": 35000,
        "mp": 1500,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 32, "mag": 47, "def": 1, "mdef": 1,
            "acc": 15, "agl": 18, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bahamut_Render_FFX.webp"
    },

    "Bahamut (Sin)": {
        "zanmato_lv": 3,
        "hp": "Varies",
        "hp_overkill": 5000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Distill", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bahamut_Render_FFX.webp"
    },

    "Biran Ronso": {
        "zanmato_lv": 4,
        "hp": "Varies",
        "hp_overkill": 2500,
        "mp": 200,
        "ap": 4500,
        "ap_overkill": 6750,
        "location": "Mt. Gagazet",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": 30, "mdef": 10,
            "acc": 100, "agl": "Varies", "eva": 0, "luck": 15
        },
        "gil": 1500,
        "steal": {"common": "Lv. 3 Key Sphere", "rare": "Lv. 3 Key Sphere x2"},
        "bribe": None,
        "drop": {"common": "Return Sphere x1", "rare": "Friend Sphere x1"},
        "equipment_drop": "2-3 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Piercing"],
        "armor_abilities": ["MP +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Reflect", "Bribe", "Delay", "Capture"],
        "status_resistances": {
            "Doom": "0 (20 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Biran_Ronso_Render.webp"
    },

    "Braska's Final Aeon (First)": {
        "zanmato_lv": 6,
        "hp": 60000,
        "hp_overkill": 20000,
        "mp": 106,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Sin (Dream's End)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 45, "mag": 50, "def": 100, "mdef": 100,
            "acc": 10, "agl": 40, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Turbo Ether", "rare": "Elixir"},
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Petrify", "Slow", "Threaten", "Death", "Doom", "Demi", "Regen", "Distill", "Bribe", "Delay", "Capture"],
        "status_resistances": {
            "Silence": "75",
            "Poison": "90 (1 max HP removed each turn)",
            "Zombie": "50"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Braskas_Final_Aeon-enemy-ffx.webp"
    },

    "Braska's Final Aeon (Second)": {
        "zanmato_lv": 6,
        "hp": 120000,
        "hp_overkill": 20000,
        "mp": 106,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Sin (Dream's End)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 50, "mag": 50, "def": 100, "mdef": 100,
            "acc": 10, "agl": 40, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Turbo Ether", "rare": "Elixir"},
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Petrify", "Slow", "Threaten", "Death", "Doom", "Demi", "Regen", "Distill", "Bribe", "Delay", "Capture"],
        "status_resistances": {
            "Silence": "75",
            "Poison": "90 (1 max HP removed each turn)",
            "Zombie": "50"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/BraskasFinalAeon_2-ffx.webp"
    },

    "Chocobo Eater": {
        "zanmato_lv": 4,
        "hp": 10000,
        "hp_overkill": 800,
        "mp": 5,
        "ap": 90,
        "ap_overkill": 135,
        "location": "Mi'ihen Highroad",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 25, "mag": 20, "def": 25, "mdef": 35,
            "acc": 25, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 970,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": None,
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Sensor", "Piercing", "Strength +5%", "Strength +10%", "Magic +5%", "Magic +10%"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Petrify", "Zombie", "Threaten", "Death", "Doom", "Demi", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Poison": "40 (5 max HP removed each turn)",
            "Power Break": "50",
            "Magic Break": "50",
            "Armor Break": "50",
            "Mental Break": "50"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Chocobo_Eater-enemy-ffx.webp"
    },

    "Cindy (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 48000,
        "hp_overkill": 48000,
        "mp": 8000,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 48, "mag": 38, "def": 1, "mdef": 1,
            "acc": 1, "agl": 15, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Cindy_FFX_Render.webp"
    },

    "Cindy (Sin)": {
        "zanmato_lv": 4,
        "hp": "Varies",
        "hp_overkill": 2000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Cindy_FFX_Render.webp"
    },

    "Crawler": {
        "zanmato_lv": 4,
        "hp": 16000,
        "hp_overkill": 4000,
        "mp": 1,
        "ap": 4400,
        "ap_overkill": 6600,
        "location": "Lake Macalania",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 25, "mag": 30, "def": 100, "mdef": 50,
            "acc": 30, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 7000,
        "steal": {"common": "Lunar Curtain", "rare": "Lunar Curtain x2"},
        "bribe": None,
        "drop": {"common": "Elixir x1", "rare": "Elixir x2"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Alchemy"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Regen", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire", "Ice", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Crawler-enemy-ffx.webp"
    },

    "Dark Anima": {
        "zanmato_lv": 5,
        "hp": 8000000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 30000,
        "ap_overkill": 40000,
        "location": "Mt. Gagazet",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 155, "mag": 255, "def": 230, "mdef": 255,
            "acc": 255, "agl": 183, "eva": 0, "luck": 85
        },
        "gil": 0,
        "steal": {"common": "Three Stars x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Deathstrike", "One MP Cost", "Triple AP", "Break Damage Limit"],
        "armor_abilities": ["Deathproof", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture", "Magical damage"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire", "Ice", "Lightning", "Water"]
        },
        "image": "./images/Dark_Anima.webp"
    },

    "Dark Bahamut": {
        "zanmato_lv": 5,
        "hp": 4000000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 30000,
        "ap_overkill": 40000,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 245, "mag": 222, "def": 234, "mdef": 233,
            "acc": 250, "agl": 255, "eva": 0, "luck": 102
        },
        "gil": 0,
        "steal": {"common": "Twin Stars x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["One MP Cost", "Double AP", "Double Overdrive", "Break Damage Limit"],
        "armor_abilities": ["Auto-Protect", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Bahamut.webp"
    },

    "Dark Cindy": {
        "zanmato_lv": 5,
        "hp": 3000000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 10000,
        "ap_overkill": 12000,
        "location": "Mushroom Rock Road",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 175, "mag": 171, "def": 223, "mdef": 105,
            "acc": 255, "agl": 185, "eva": 0, "luck": 40
        },
        "gil": 0,
        "steal": {"common": "Return Sphere", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Alchemy", "Triple Overdrive", "Gillionaire", "Break Damage Limit"],
        "armor_abilities": ["Auto-Phoenix", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Cindy.webp"
    },

    "Dark Ifrit": {
        "zanmato_lv": 5,
        "hp": 1400000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 20000,
        "ap_overkill": 30000,
        "location": "Bikanel",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 220, "mag": 177, "def": 173, "mdef": 163,
            "acc": 230, "agl": 124, "eva": 8, "luck": 27
        },
        "gil": 0,
        "steal": {"common": "Mega Phoenix x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Firestrike", "Break Damage Limit"],
        "armor_abilities": ["Fire Eater", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Ice"],
            "immune": ["Lightning", "Water"],
            "absorb": []
        },
        "image": "./images/Dark_Ifrit.webp"
    },

    "Dark Ixion (First encounter)": {
        "zanmato_lv": 5,
        "hp": 1200000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 20000,
        "ap_overkill": 30000,
        "location": "Thunder Plains (North)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 176, "mag": 133, "def": 220, "mdef": 188,
            "acc": 254, "agl": 180, "eva": 0, "luck": 36
        },
        "gil": 0,
        "steal": {"common": "Stamina Tablet x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Lightningstrike", "Break Damage Limit"],
        "armor_abilities": ["Lightning Eater", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Water"],
            "immune": ["Fire", "Ice"],
            "absorb": []
        },
        "image": "./images/Dark_Ixion.webp"
    },

    "Dark Ixion (Second encounter)": {
        "zanmato_lv": 5,
        "hp": 1200000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 20000,
        "ap_overkill": 30000,
        "location": "Thunder Plains (North)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 182, "mag": 146, "def": 222, "mdef": 198,
            "acc": 254, "agl": 180, "eva": 0, "luck": 36
        },
        "gil": 0,
        "steal": {"common": "Stamina Tablet x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Lightningstrike", "Break Damage Limit"],
        "armor_abilities": ["Lightning Eater", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Water"],
            "immune": ["Fire", "Ice"],
            "absorb": []
        },
        "image": "./images/Dark_Ixion.webp"
    },

    "Dark Mindy": {
        "zanmato_lv": 5,
        "hp": 2000000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 10000,
        "ap_overkill": 12000,
        "location": "Mushroom Rock Road",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 148, "mag": 248, "def": 187, "mdef": 132,
            "acc": 255, "agl": 233, "eva": 240, "luck": 130
        },
        "gil": 0,
        "steal": {"common": "Teleport Sphere", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Magic Booster", "One MP Cost", "Triple Overdrive", "Break Damage Limit"],
        "armor_abilities": ["Auto-Haste", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Mindy.webp"
    },

    "Dark Sandy": {
        "zanmato_lv": 5,
        "hp": 2500000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 10000,
        "ap_overkill": 12000,
        "location": "Mushroom Rock Road",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 186, "mag": 207, "def": 201, "mdef": 168,
            "acc": 255, "agl": 201, "eva": 100, "luck": 80
        },
        "gil": 0,
        "steal": {"common": "Friend Sphere", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Evade & Counter", "Magic Counter", "Triple Overdrive", "Break Damage Limit"],
        "armor_abilities": ["Auto-Shell", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Sandy.webp"
    },

    "Dark Shiva": {
        "zanmato_lv": 5,
        "hp": 1100000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 20000,
        "ap_overkill": 30000,
        "location": "Macalania Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 173, "mag": 244, "def": 163, "mdef": 255,
            "acc": 250, "agl": 255, "eva": 0, "luck": 73
        },
        "gil": 0,
        "steal": {"common": "Mana Tablet x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Icestrike", "Break Damage Limit"],
        "armor_abilities": ["Ice Eater", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire"],
            "immune": ["Lightning", "Water"],
            "absorb": []
        },
        "image": "./images/Dark_Shiva.webp"
    },

    "Dark Valefor": {
        "zanmato_lv": 5,
        "hp": 800000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 10000,
        "ap_overkill": 15000,
        "location": "Besaid",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 148, "mag": 186, "def": 120, "mdef": 220,
            "acc": 250, "agl": 105, "eva": 10, "luck": 48
        },
        "gil": 0,
        "steal": {"common": "X-Potion x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["First Strike", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike", "Break Damage Limit"],
        "armor_abilities": ["Auto-Regen", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Valefor.webp"
    },

    "Dark Yojimbo": {
        "zanmato_lv": 5,
        "hp": 1600000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 8000,
        "ap_overkill": 10000,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 244, "mag": 131, "def": 210, "mdef": 144,
            "acc": 255, "agl": 243, "eva": 0, "luck": 114
        },
        "gil": 0,
        "steal": {"common": "Stamina Tonic x2", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Dark Matter x1", "rare": "Master Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Counterattack", "Magic Counter", "Overdrive -> AP", "Break Damage Limit"],
        "armor_abilities": ["Curseproof", "Break HP Limit", "Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Dark_Yojimbo.webp"
    },

    "Defender X": {
        "zanmato_lv": 1,
        "hp": 64000,
        "hp_overkill": 4060,
        "mp": 1,
        "ap": 6600,
        "ap_overkill": 9900,
        "location": "Calm Lands",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 42, "mag": 5, "def": 30, "mdef": 1,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 3500,
        "steal": {"common": "Lunar Curtain x4", "rare": "Lunar Curtain x4"},
        "bribe": None,
        "drop": {"common": "Lv. 2 Key Sphere x1", "rare": "Lv. 2 Key Sphere x2"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 23.44% chance",
        "weapon_abilities": ["Piercing", "Strength +5%", "Strength +10%", "Magic +5%", "Magic +10%", "Distill Power"],
        "armor_abilities": ["SOS Protect"],
        "immunities": ["Silence", "Sleep", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Threaten", "Death", "Demi", "Bribe", "Delay", "Capture"],
        "status_resistances": {
            "Darkness": "95",
            "Doom": "0 (10 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Defender-enemy-ffx.webp"
    },

    "Evrae": {
        "zanmato_lv": 4,
        "hp": 32000,
        "hp_overkill": 2000,
        "mp": 500,
        "ap": 5400,
        "ap_overkill": 8100,
        "location": "Fahrenheit",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 36, "mag": 30, "def": 1, "mdef": 1,
            "acc": 100, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 2600,
        "steal": {"common": "Water Gem", "rare": "Water Gem x2"},
        "bribe": None,
        "drop": {"common": "Blk Magic Sphere x1", "rare": "Blk Magic Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Stonetouch"],
        "armor_abilities": ["Stone Ward"],
        "immunities": ["Silence", "Sleep", "Poison", "Petrify", "Zombie", "Magic Break", "Armor Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Darkness": "50",
            "Slow": "50"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Lightning", "Water"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Evrae-enemy-ffx.webp"
    },

    "Evrae Altana": {
        "zanmato_lv": 4,
        "hp": 16384,
        "hp_overkill": 2000,
        "mp": 200,
        "ap": 5800,
        "ap_overkill": 8700,
        "location": "Via Purifico",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 32, "mag": 27, "def": 1, "mdef": 1,
            "acc": 100, "agl": 25, "eva": 0, "luck": 15
        },
        "gil": 3000,
        "steal": {"common": "Water Gem x2", "rare": "Healing Spring"},
        "bribe": None,
        "drop": {"common": "Blk Magic Sphere x1", "rare": "Blk Magic Sphere x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Stonetouch"],
        "armor_abilities": ["Stone Ward"],
        "immunities": ["Silence", "Sleep", "Poison", "Petrify", "Threaten", "Death", "Provoke", "Doom", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Slow": "50",
            "Zombie": "Auto"
        },
        "elemental_affinities": {
            "weak": ["Holy"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Evrae_Altana_from_FFX.webp"
    },

    "Extractor": {
        "zanmato_lv": 4,
        "hp": 4000,
        "hp_overkill": 600,
        "mp": 10,
        "ap": 660,
        "ap_overkill": 990,
        "location": "Moonflow (Underwater)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 23, "mag": 15, "def": 1, "mdef": 1,
            "acc": 30, "agl": 15, "eva": 0, "luck": 15
        },
        "gil": 2400,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Mega Phoenix x1", "rare": "Mega Phoenix x2"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS NulBlaze", "SOS NulShock", "SOS NulTide", "SOS NulFrost"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Death", "Doom", "Regen", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Provoke": "50"
        },
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire", "Ice", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Albhed_Extractor.webp"
    },

    "Geneaux's Tentacle": {
        "zanmato_lv": 4,
        "hp": 450,
        "hp_overkill": 500,
        "mp": 10,
        "ap": 5,
        "ap_overkill": 7,
        "location": "Kilika Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 14, "mag": 1, "def": 1, "mdef": 1,
            "acc": 20, "agl": 10, "eva": 0, "luck": 10
        },
        "gil": 30,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x1", "rare": "Ability Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 0% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Doom", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Ice", "Lightning"],
            "immune": [],
            "absorb": ["Water"]
        },
        "image": "./images/Sinspawn_Geneaux-enemy-ffx.webp"
    },

    "Geosgaeno (1st Encounter)": {
        "zanmato_lv": 4,
        "hp": 32767,
        "hp_overkill": 0,
        "mp": 128,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Submerged Ruins (Underwater Hall)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 36, "mag": 40, "def": 50, "mdef": 50,
            "acc": 50, "agl": 5, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": {"common": "Water Gem", "rare": "Water Gem x2"},
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Poison": "95 (10 max HP removed each turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Geosgaeno-enemy-ffx.webp"
    },

    "Geosgaeno (2nd Encounter)": {
        "zanmato_lv": 4,
        "hp": 32767,
        "hp_overkill": 32767,
        "mp": 128,
        "ap": 4200,
        "ap_overkill": 6300,
        "location": "Submerged Ruins (Underwater Hall)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 36, "mag": 40, "def": 50, "mdef": 50,
            "acc": 50, "agl": 48, "eva": 0, "luck": 15
        },
        "gil": 1000,
        "steal": {"common": "Water Gem", "rare": "Water Gem x2"},
        "bribe": None,
        "drop": {"common": "Power Sphere x2", "rare": "Power Sphere x2"},
        "equipment_drop": "2-3 slots, 1 ability, 100% chance",
        "weapon_abilities": ["No Encounters"],
        "armor_abilities": ["Auto-Reflect"],
        "immunities": ["Silence", "Sleep", "Darkness", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Poison": "95 (10 max HP removed each turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Geosgaeno-enemy-ffx.webp"
    },

    "Grothia": {
        "zanmato_lv": 1,
        "hp": 8000,
        "hp_overkill": 2550,
        "mp": 600,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Via Purifico (Land)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 23, "mag": 21, "def": 10, "mdef": 1,
            "acc": 1, "agl": 18, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire"]
        },
        "image": "./images/Ifrit_FFX_Render.webp"
    },

    "Ifrit (Highroad)": {
        "zanmato_lv": 1,
        "hp": 3000,
        "hp_overkill": 2550,
        "mp": 200,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Mi'ihen Highroad (South End)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 15, "mag": 10, "def": 20, "mdef": 10,
            "acc": 15, "agl": 10, "eva": 10, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ifrit_FFX_Render.webp"
    },

    "Ifrit (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 28000,
        "hp_overkill": 28000,
        "mp": 800,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 29, "mag": 45, "def": 40, "mdef": 40,
            "acc": 15, "agl": 18, "eva": 10, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ifrit_FFX_Render.webp"
    },

    "Ifrit (Sin)": {
        "zanmato_lv": 3,
        "hp": "Varies",
        "hp_overkill": 2000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ifrit_FFX_Render.webp"
    },

    "Ixion (Moonflow)": {
        "zanmato_lv": 1,
        "hp": 6000,
        "hp_overkill": 924,
        "mp": 450,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Moonflow (South Bank Road)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 22, "mag": 23, "def": 1, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Reflect", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ixion_Render_FFX.webp"
    },

    "Ixion (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 30000,
        "hp_overkill": 30000,
        "mp": 720,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 40, "mag": 50, "def": 40, "mdef": 40,
            "acc": 15, "agl": 12, "eva": 10, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Reflect", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ixion_Render_FFX.webp"
    },

    "Ixion (Sin)": {
        "zanmato_lv": 3,
        "hp": "Varies",
        "hp_overkill": 3000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ixion_Render_FFX.webp"
    },

    "Klikk": {
        "zanmato_lv": 1,
        "hp": 1500,
        "hp_overkill": 400,
        "mp": 5,
        "ap": 5,
        "ap_overkill": 7,
        "location": "Submerged Ruins (Hall)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 14, "mag": 1, "def": 1, "mdef": 1,
            "acc": 50, "agl": 4, "eva": 0, "luck": 15
        },
        "gil": 50,
        "steal": {"common": "Grenade", "rare": "Grenade x2"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x2", "rare": "Ability Sphere x2"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Poison", "Sensor", "Scan", "Bribe", "Capture"],
        "status_resistances": {
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Klikk-enemy-ffx.webp"
    },

    "Left Fin": {
        "zanmato_lv": 4,
        "hp": 65000,
        "hp_overkill": 10000,
        "mp": 999,
        "ap": 16000,
        "ap_overkill": 24000,
        "location": "Fahrenheit",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 30, "def": 100, "mdef": 50,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 10000,
        "steal": {"common": "Mega-Potion", "rare": "Supreme Gem"},
        "bribe": None,
        "drop": {"common": "HP Sphere x1", "rare": "HP Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Poisonstrike"],
        "armor_abilities": ["Poisonproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Doom", "Haste", "Demi", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Left_Fin-enemy-ffx.webp"
    },

    "Lord Ochu": {
        "zanmato_lv": 1,
        "hp": 4649,
        "hp_overkill": 800,
        "mp": 39,
        "ap": 40,
        "ap_overkill": 60,
        "location": "Kilika Woods",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 15, "mag": 23, "def": 1, "mdef": 1,
            "acc": 10, "agl": 8, "eva": 10, "luck": 20
        },
        "gil": 420,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": ["Remedy x80 (116,225 gil)"],
        "drop": {"common": "MP Sphere x1", "rare": "HP Sphere x1"},
        "equipment_drop": "1-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Poisontouch", "Strength +5%", "Magic +5%"],
        "armor_abilities": ["Dark Ward", "Silence Ward", "Sleep Ward", "Poison Ward", "Stone Ward", "Confuse Ward", "Berserk Ward"],
        "immunities": ["Darkness", "Poison", "Provoke", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (1 turn)"
        },
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mandragora-enemy-ffx.webp"
    },

    "Mindy (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 20000,
        "hp_overkill": 20000,
        "mp": 7000,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 21, "mag": 28, "def": 1, "mdef": 1,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mindy_FFX_Render.webp"
    },

    "Mindy (Sin)": {
        "zanmato_lv": 4,
        "hp": "Varies",
        "hp_overkill": 2000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mindy_FFX_Render.webp"
    },

    "Mortibody": {
        "zanmato_lv": 4,
        "hp": 4000,
        "hp_overkill": 36000,
        "mp": 50,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Bevelle Highbridge",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 22, "mag": 20, "def": 50, "mdef": 1,
            "acc": 100, "agl": 28, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Magic Break", "Mental Break", "Death", "Provoke", "Doom", "Demi", "Distill", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Armor Break": "50"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mortiorchis_Render.webp"
    },

    "Mortiorchis": {
        "zanmato_lv": 4,
        "hp": 4000,
        "hp_overkill": 36000,
        "mp": 512,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Mt. Gagazet",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 40, "mag": 40, "def": 100, "mdef": 1,
            "acc": 100, "agl": 38, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Haste", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mortiorchis_Render.webp"
    },

    "Mortiphasm": {
        "zanmato_lv": 1,
        "hp": 1,
        "hp_overkill": 1,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin (Garden of Pain)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 1, "eva": 1, "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Shell", "Protect", "Reflect", "Haste", "Demi", "Regen", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture", "Physical damage", "Magical damage"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Mortiphasm.webp"
    },

    "Negator": {
        "zanmato_lv": 4,
        "hp": 1000,
        "hp_overkill": 1000,
        "mp": 1,
        "ap": 220,
        "ap_overkill": 330,
        "location": "Lake Macalania",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 1, "eva": 0, "luck": 1
        },
        "gil": 300,
        "steal": {"common": "Hi-Potion", "rare": "Hi-Potion x2"},
        "bribe": None,
        "drop": {"common": "Potion x1", "rare": "Hi-Potion x1"},
        "equipment_drop": "1-3 slots, 1-2 abilities, 15.23% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Doom", "Regen", "Scan", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire", "Ice", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Negator-enemy-ffx.webp"
    },

    "Oblitzerator": {
        "zanmato_lv": 4,
        "hp": 6000,
        "hp_overkill": 600,
        "mp": 10,
        "ap": 36,
        "ap_overkill": 54,
        "location": "Luca Docks",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 16, "mag": 1, "def": 1, "mdef": 1,
            "acc": 10, "agl": 1, "eva": 0, "luck": 1
        },
        "gil": 580,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Elixir x1", "rare": "Elixir x2"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Lightningstrike"],
        "armor_abilities": ["Defense +3%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Doom", "Regen", "Distill", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": ["Lightning"],
            "resisted": ["Fire", "Ice", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Oblitzerator.webp"
    },

    "Omega Weapon (NTSC)": {
        "zanmato_lv": 4,
        "hp": 99999,
        "hp_overkill": 13560,
        "mp": 1,
        "ap": 50000,
        "ap_overkill": 60000,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 54, "mag": 50, "def": 80, "mdef": 20,
            "acc": 1, "agl": 32, "eva": 0, "luck": 15
        },
        "gil": 20000,
        "steal": {"common": "Gambler's Spirit x30", "rare": "Gambler's Spirit x30"},
        "bribe": None,
        "drop": {"common": "Lv. 4 Key Sphere x3", "rare": "Lv. 4 Key Sphere x3"},
        "equipment_drop": "2-3 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Triple Overdrive"],
        "armor_abilities": ["Break HP Limit"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (222 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": ["Fire", "Ice", "Lightning", "Water", "Holy"],
            "immune": [],
            "absorb": []
        },
        "image": "./images/OmegaWeapon-ffx.webp"
    },

    "Omega Weapon (PAL/Int./HD)": {
        "zanmato_lv": 4,
        "hp": 999999,
        "hp_overkill": 66666,
        "mp": 999,
        "ap": 50000,
        "ap_overkill": 60000,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 64, "mag": 57, "def": 90, "mdef": 80,
            "acc": 1, "agl": 38, "eva": 0, "luck": 15
        },
        "gil": 20000,
        "steal": {"common": "Gambler's Spirit x30", "rare": "Gambler's Spirit x30"},
        "bribe": None,
        "drop": {"common": "Lv. 4 Key Sphere x3", "rare": "Lv. 4 Key Sphere x3"},
        "equipment_drop": "2-3 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Triple Overdrive"],
        "armor_abilities": ["Break HP Limit"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (222 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire", "Ice", "Lightning", "Water", "Holy"]
        },
        "image": "./images/OmegaWeapon-ffx.webp"
    },

    "Penance": {
        "zanmato_lv": 6,
        "hp": 12000000,
        "hp_overkill": 99999,
        "mp": 999,
        "ap": 60000,
        "ap_overkill": 65000,
        "location": "Calm Lands",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 255, "mag": 255, "def": 240, "mdef": 200,
            "acc": 255, "agl": 255, "eva": 0, "luck": 10
        },
        "gil": 0,
        "steal": {"common": "Elixir", "rare": "Megalixir x2"},
        "bribe": None,
        "drop": {"common": "Master Sphere x3", "rare": "Master Sphere x3"},
        "equipment_drop": "4 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Break Damage Limit"],
        "armor_abilities": ["Ribbon"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": ["Fire", "Ice", "Lightning", "Water", "Holy"]
        },
        "image": "./images/Penance.webp"
    },

    "Pterya": {
        "zanmato_lv": 4,
        "hp": 12000,
        "hp_overkill": 2550,
        "mp": 1000,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Via Purifico (Land)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 18, "def": 10, "mdef": 10,
            "acc": 1, "agl": 21, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Valefor-FFX.webp"
    },

    "Right Fin": {
        "zanmato_lv": 4,
        "hp": 65000,
        "hp_overkill": 10000,
        "mp": 999,
        "ap": 17000,
        "ap_overkill": 25500,
        "location": "Fahrenheit",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 30, "def": 100, "mdef": 50,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 10000,
        "steal": {"common": "X-Potion", "rare": "Shining Gem"},
        "bribe": None,
        "drop": {"common": "Lv. 3 Key Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Stonestrike"],
        "armor_abilities": ["Stoneproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Doom", "Haste", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Right_Fin-enemy-ffx.webp"
    },

    "Sanctuary Keeper": {
        "zanmato_lv": 4,
        "hp": 40000,
        "hp_overkill": 6400,
        "mp": 256,
        "ap": 11000,
        "ap_overkill": 16500,
        "location": "Mt. Gagazet",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 37, "mag": 40, "def": 100, "mdef": 100,
            "acc": 50, "agl": 32, "eva": 0, "luck": 15
        },
        "gil": 6500,
        "steal": {"common": "Turbo Ether", "rare": "Turbo Ether x2"},
        "bribe": None,
        "drop": {"common": "Return Sphere x1", "rare": "Return Sphere x1"},
        "equipment_drop": "2-3 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Half MP Cost"],
        "armor_abilities": ["MP +10%"],
        "immunities": ["Silence", "Sleep", "Petrify", "Zombie", "Death", "Provoke", "Doom", "Demi", "Bribe", "Delay", "Capture"],
        "status_resistances": {
            "Darkness": "100",
            "Poison": "90 (5 max HP removed each turn)",
            "Power Break": "50",
            "Magic Break": "50"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sanctuary_Keeper-enemy-ffx.webp"
    },

    "Sandy (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 35000,
        "hp_overkill": 35000,
        "mp": 3000,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 35, "mag": 18, "def": 1, "mdef": 1,
            "acc": 1, "agl": 24, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sandy_FFX_Render.webp"
    },

    "Sandy (Sin)": {
        "zanmato_lv": 4,
        "hp": "Varies",
        "hp_overkill": 2000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sandy_FFX_Render.webp"
    },

    "Seymour": {
        "zanmato_lv": 4,
        "hp": 6000,
        "hp_overkill": 1400,
        "mp": 100,
        "ap": 2000,
        "ap_overkill": 3000,
        "location": "Macalania Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 25, "def": 1, "mdef": 25,
            "acc": 100, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 5000,
        "steal": {"common": "Turbo Ether", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Blk Magic Sphere x1", "rare": "Special Sphere x1"},
        "equipment_drop": "2-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Silencestrike"],
        "armor_abilities": ["Silenceproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Petrify", "Zombie", "Power Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Poison": "40 (10 max HP removed each turn)",
            "Magic Break": "50"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Seymour-enemy-ffx.webp"
    },

    "Seymour Flux": {
        "zanmato_lv": 4,
        "hp": 70000,
        "hp_overkill": 3500,
        "mp": 512,
        "ap": 10000,
        "ap_overkill": 15000,
        "location": "Mt. Gagazet (Prominence)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 15, "def": 40, "mdef": 40,
            "acc": 100, "agl": 38, "eva": 0, "luck": 15
        },
        "gil": 6000,
        "steal": {"common": "Elixir", "rare": "Elixir"},
        "bribe": None,
        "drop": {"common": "Lv. 4 Key Sphere x1", "rare": "Lv. 4 Key Sphere x1"},
        "equipment_drop": "1-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Darkstrike"],
        "armor_abilities": ["SOS Shell"],
        "immunities": ["Sleep", "Darkness", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Silence": "50",
            "Poison": "90 (2 max HP removed each turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Seymour_Flux-enemy-ffx.webp"
    },

    "Seymour Natus": {
        "zanmato_lv": 4,
        "hp": 36000,
        "hp_overkill": 3500,
        "mp": 200,
        "ap": 6300,
        "ap_overkill": 9450,
        "location": "Bevelle Highbridge",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 25, "def": 1, "mdef": 1,
            "acc": 100, "agl": 21, "eva": 0, "luck": 15
        },
        "gil": 3500,
        "steal": {"common": "Tetra Elemental x2", "rare": "Tetra Elemental x3"},
        "bribe": None,
        "drop": {"common": "Lv. 2 Key Sphere x2", "rare": "Lv. 2 Key Sphere x2"},
        "equipment_drop": "2-3 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["SOS Shell"],
        "immunities": ["Silence", "Sleep", "Darkness", "Petrify", "Slow", "Zombie", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Doom", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Poison": "50 (4 max HP removed each turn)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Seymour_Natus-enemy-ffx.webp"
    },

    "Seymour Omnis": {
        "zanmato_lv": 4,
        "hp": 80000,
        "hp_overkill": 15000,
        "mp": 999,
        "ap": 24000,
        "ap_overkill": 36000,
        "location": "Inside Sin (Garden of Pain)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 35, "def": 180, "mdef": 100,
            "acc": 1, "agl": 40, "eva": 0, "luck": 20
        },
        "gil": 12000,
        "steal": {"common": "Shining Gem", "rare": "Supreme Gem"},
        "bribe": None,
        "drop": {"common": "Lv. 3 Key Sphere x1", "rare": "Lv. 3 Key Sphere x2"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Magic +20%"],
        "armor_abilities": ["SOS Shell", "SOS Protect", "SOS Haste"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Doom", "Demi", "Distill", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Seymour-Omnis-1-.webp"
    },

    "Shiva (Calm Lands)": {
        "zanmato_lv": 1,
        "hp": 15000,
        "hp_overkill": 1432,
        "mp": 900,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Calm Lands (Central Area)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 20, "def": 180, "mdef": 180,
            "acc": 1, "agl": 21, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Shiva-FFX.webp"
    },

    "Shiva (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 20000,
        "hp_overkill": 20000,
        "mp": 950,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 25, "mag": 31, "def": 1, "mdef": 1,
            "acc": 15, "agl": 22, "eva": 50, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {
            "Doom": "0 (5 turns)"
        },
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Shiva-FFX.webp"
    },

    "Shiva (Sin)": {
        "zanmato_lv": 3,
        "hp": "Varies",
        "hp_overkill": 4000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Shiva-FFX.webp"
    },

    "Sin (Core)": {
        "zanmato_lv": 4,
        "hp": 36000,
        "hp_overkill": 3000,
        "mp": 999,
        "ap": 18000,
        "ap_overkill": 27000,
        "location": "Fahrenheit",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 30, "def": 100, "mdef": 100,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 10000,
        "steal": {"common": "Stamina Spring x3", "rare": "Stamina Spring x4"},
        "bribe": None,
        "drop": {"common": "MP Sphere x1", "rare": "MP Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Slowstrike"],
        "armor_abilities": ["Slowproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Doom", "Reflect", "Haste", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sin_Core-enemy-ffx.webp"
    },

    "Sin (Fin)": {
        "zanmato_lv": 4,
        "hp": 2000,
        "hp_overkill": 1000,
        "mp": 100,
        "ap": 10,
        "ap_overkill": 20,
        "location": "S.S. Liki (Deck)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 6, "eva": 0, "luck": 15
        },
        "gil": 100,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Mana Sphere x1", "rare": "Mana Sphere x1"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Icestrike"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Doom", "Shell", "Protect", "Reflect", "Haste", "Regen", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sin_Fin-enemy-ffx.webp"
    },

    "Sin (Head)": {
        "zanmato_lv": 1,
        "hp": 140000,
        "hp_overkill": 16000,
        "mp": 999,
        "ap": 20000,
        "ap_overkill": 30000,
        "location": "Fahrenheit, above Bevelle",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 30, "def": 40, "mdef": 40,
            "acc": 1, "agl": 30, "eva": 0, "luck": 15
        },
        "gil": 12000,
        "steal": {"common": "Ether", "rare": "Supreme Gem"},
        "bribe": None,
        "drop": {"common": "Lv. 3 Key Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "3-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Darkstrike", "Silencestrike", "Sleepstrike", "Slowstrike"],
        "armor_abilities": ["Silenceproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Threaten", "Death", "Provoke", "Doom", "Haste", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/BOSS-SIN.webp"
    },

    "Sinspawn Ammes": {
        "zanmato_lv": 1,
        "hp": 2400,
        "hp_overkill": 1000,
        "mp": 400,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Dream Zanarkand",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 5, "def": 1, "mdef": 1,
            "acc": 1, "agl": 9, "eva": 0, "luck": 10
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Sleep", "Poison", "Petrify", "Zombie", "Threaten", "Death", "Doom", "Demi", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinspawn_Ammes-enemy-ffx.webp"
    },

    "Sinspawn Echuilles": {
        "zanmato_lv": 4,
        "hp": 2000,
        "hp_overkill": 400,
        "mp": 20,
        "ap": 12,
        "ap_overkill": 18,
        "location": "S.S. Liki (Underwater)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 10, "mag": 15, "def": 1, "mdef": 1,
            "acc": 15, "agl": 5, "eva": 0, "luck": 15
        },
        "gil": 115,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Ability Sphere x2", "rare": "Ability Sphere x2"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Waterstrike"],
        "armor_abilities": ["Water Ward"],
        "immunities": ["Sleep", "Petrify", "Zombie", "Death", "Provoke", "Bribe", "Berserk", "Capture"],
        "status_resistances": {"Poison": "0 (25 max HP removed each turn)", "Doom": "0 (3 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinspawn_Echuilles-enemy-ffx.webp"
    },

    "Sinspawn Genais": {
        "zanmato_lv": 4,
        "hp": 20000,
        "hp_overkill": 2000,
        "mp": 200,
        "ap": 1800,
        "ap_overkill": 2700,
        "location": "Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 35, "def": 80, "mdef": 50,
            "acc": 1, "agl": 25, "eva": 0, "luck": 15
        },
        "gil": 10000,
        "steal": {"common": "Star Curtain", "rare": "Shining Gem"},
        "bribe": None,
        "drop": {"common": "Return Sphere x1", "rare": "Return Sphere x1"},
        "equipment_drop": "3-4 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Zombiestrike"],
        "armor_abilities": ["Zombieproof"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Reflect", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Silence": "100", "Zombie": "80", "Doom": "0 (30 turns until death)"},
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinspawn_Genais.webp"
    },

    "Sinspawn Geneaux": {
        "zanmato_lv": 4,
        "hp": 3000,
        "hp_overkill": 900,
        "mp": 30,
        "ap": 48,
        "ap_overkill": 72,
        "location": "Kilika Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 15, "mag": 10, "def": 1, "mdef": 1,
            "acc": 100, "agl": 7, "eva": 0, "luck": 1
        },
        "gil": 300,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Power Sphere x2", "rare": "Power Sphere x3"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Darktouch"],
        "armor_abilities": ["Dark Ward"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Death", "Provoke", "Doom", "Demi", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": ["Fire"],
            "resisted": [],
            "immune": [],
            "absorb": ["Water"]
        },
        "image": "./images/Sinspawn_Geneaux-enemy-ffx.webp"
    },

    "Sinspawn Gui (1st Body)": {
        "zanmato_lv": 4,
        "hp": 12000,
        "hp_overkill": 800,
        "mp": 30,
        "ap": 400,
        "ap_overkill": 600,
        "location": "Mushroom Rock Road",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 29, "mag": 20, "def": 1, "mdef": 30,
            "acc": 100, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 1000,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 0% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Doom", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinspawn_Gui-enemy-ffx.webp"
    },

    "Sinspawn Gui (2nd Body)": {
        "zanmato_lv": 4,
        "hp": 6000,
        "hp_overkill": 800,
        "mp": 30,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Mushroom Rock Road",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 29, "mag": 20, "def": 1, "mdef": 30,
            "acc": 100, "agl": 10, "eva": 0, "luck": 15
        },
        "gil": 1000,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": {"common": "Lv. 1 Key Sphere x3", "rare": "Lv. 1 Key Sphere x3"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Sleepstrike"],
        "armor_abilities": ["Sleepproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Doom", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinspawn_Gui-enemy-ffx.webp"
    },

    "Sinspawn Gui (Head)": {
        "zanmato_lv": 4,
        "hp": "4,000 / 1,000",
        "hp_overkill": 800,
        "mp": 200,
        "ap": 48,
        "ap_overkill": 72,
        "location": "Mushroom Rock Road",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 20, "def": 1, "mdef": 1,
            "acc": 1, "agl": 15, "eva": 0, "luck": 1
        },
        "gil": 200,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 0% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Doom", "Distill", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinspawn_Gui-enemy-ffx.webp"
    },

    "Sinspawn Gui (Arms)": {
        "zanmato_lv": 4,
        "hp": 800,
        "hp_overkill": 500,
        "mp": 1,
        "ap": 37,
        "ap_overkill": 55,
        "location": "Mushroom Rock Road",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 1, "eva": 0, "luck": 1
        },
        "gil": 300,
        "steal": {"common": "Potion", "rare": "Potion"},
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 0% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Doom", "Distill", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Sinspawn_Gui-enemy-ffx.webp"
    },

    "Spathi": {
        "zanmato_lv": 1,
        "hp": 20000,
        "hp_overkill": 2550,
        "mp": 1500,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Via Purifico (Land)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 31, "mag": 38, "def": 1, "mdef": 1,
            "acc": 1, "agl": 20, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Doom": "0 (5 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Bahamut_Render_FFX.webp"
    },

    "Spectral Keeper": {
        "zanmato_lv": 4,
        "hp": 52000,
        "hp_overkill": 8000,
        "mp": 500,
        "ap": 12000,
        "ap_overkill": 18000,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 36, "mag": 1, "def": 100, "mdef": 100,
            "acc": 8, "agl": 36, "eva": 0, "luck": 15
        },
        "gil": 7000,
        "steal": {"common": "Ether", "rare": "Turbo Ether"},
        "bribe": None,
        "drop": {"common": "Lv. 4 Key Sphere x1", "rare": "Lv. 4 Key Sphere x1"},
        "equipment_drop": "2-3 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["Fireproof", "Lightningproof", "Waterproof", "Iceproof"],
        "immunities": ["Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Threaten", "Death", "Doom", "Demi", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Spectral_Keeper-enemy-ffx.webp"
    },

    "Spherimorph": {
        "zanmato_lv": 4,
        "hp": 12000,
        "hp_overkill": 2000,
        "mp": 100,
        "ap": 3240,
        "ap_overkill": 4860,
        "location": "Macalania Woods",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 20, "def": 100, "mdef": 1,
            "acc": 30, "agl": 15, "eva": 0, "luck": 15
        },
        "gil": 4000,
        "steal": {"common": "Ether", "rare": "Turbo Ether"},
        "bribe": None,
        "drop": {"common": "Lv. 2 Key Sphere x1", "rare": "Lv. 2 Key Sphere x1"},
        "equipment_drop": "2-4 slots, 1-3 abilities, 100% chance",
        "weapon_abilities": ["Piercing", "Firestrike", "Lightningstrike", "Waterstrike", "Icestrike"],
        "armor_abilities": ["Fire Ward", "Lightning Ward", "Water Ward", "Ice Ward"],
        "immunities": ["Silence", "Sleep", "Darkness", "Petrify", "Slow", "Death", "Provoke", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Poison": "90 (5 max HP removed each turn)", "Threaten": "75", "Doom": "0 (20 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Spherimorph-enemy-ffx.webp"
    },

    "Tanker": {
        "zanmato_lv": 1,
        "hp": 1000,
        "hp_overkill": 1000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Dream Zanarkand",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 1, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Shell", "Protect", "Reflect", "Haste", "Regen", "Distill", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Tanker-ffx.webp"
    },

    "Tros": {
        "zanmato_lv": 4,
        "hp": 2200,
        "hp_overkill": 600,
        "mp": 10,
        "ap": 8,
        "ap_overkill": 12,
        "location": "Underwater Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 10, "mag": 1, "def": 1, "mdef": 1,
            "acc": 20, "agl": 12, "eva": 0, "luck": 15
        },
        "gil": 100,
        "steal": {"common": "Grenade", "rare": "Grenade x3"},
        "bribe": None,
        "drop": {"common": "Power Sphere x2", "rare": "Power Sphere x2"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Petrify", "Zombie", "Threaten", "Death", "Provoke", "Doom", "Demi", "Bribe", "Berserk"],
        "status_resistances": {"Poison": "0 (0 max HP removed each turn)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Tros-enemy-ffx.webp"
    },

    "Ultima Weapon (NTSC)": {
        "zanmato_lv": 4,
        "hp": 70000,
        "hp_overkill": 13560,
        "mp": 1,
        "ap": 40000,
        "ap_overkill": 50000,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 50, "mag": 45, "def": 60, "mdef": 60,
            "acc": 1, "agl": 28, "eva": 0, "luck": 15
        },
        "gil": 20000,
        "steal": {"common": "Door to Tomorrow x10", "rare": "Door to Tomorrow x20"},
        "bribe": ["Pendulum x99 (1,750,000 gil)"],
        "drop": {"common": "Lv. 3 Key Sphere x3", "rare": "Lv. 3 Key Sphere x3"},
        "equipment_drop": "2-3 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Double Overdrive"],
        "armor_abilities": ["Break MP Limit"],
        "immunities": ["Sleep", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Scan", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Silence": "95", "Darkness": "95", "Doom": "0 (99 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ultima_Weapon.webp"
    },

    "Ultima Weapon (PAL/Int./HD)": {
        "zanmato_lv": 4,
        "hp": 99999,
        "hp_overkill": 13560,
        "mp": 99,
        "ap": 40000,
        "ap_overkill": 50000,
        "location": "Omega Ruins",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 50, "mag": 45, "def": 60, "mdef": 60,
            "acc": 1, "agl": 32, "eva": 0, "luck": 15
        },
        "gil": 20000,
        "steal": {"common": "Door to Tomorrow x10", "rare": "Door to Tomorrow x20"},
        "bribe": ["Pendulum x99 (2,499,975 gil)"],
        "drop": {"common": "Lv. 3 Key Sphere x3", "rare": "Lv. 3 Key Sphere x3"},
        "equipment_drop": "2-3 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Double Overdrive"],
        "armor_abilities": ["Break MP Limit"],
        "immunities": ["Sleep", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Scan", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Silence": "95", "Darkness": "95", "Doom": "0 (99 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Ultima_Weapon.webp"
    },

    "Valefor (Remiem Temple)": {
        "zanmato_lv": 4,
        "hp": 20000,
        "hp_overkill": 20000,
        "mp": 500,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 35, "mag": 48, "def": 85, "mdef": 1,
            "acc": 1, "agl": 17, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Doom": "0 (5 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Valefor-FFX.webp"
    },

    "Valefor (Sin)": {
        "zanmato_lv": 3,
        "hp": "Varies",
        "hp_overkill": 1000,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Valefor-FFX.webp"
    },

    "Wendigo": {
        "zanmato_lv": 1,
        "hp": 18000,
        "hp_overkill": 1432,
        "mp": 32,
        "ap": 2000,
        "ap_overkill": 3000,
        "location": "Lake Macalania",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 40, "mag": 1, "def": 1, "mdef": 1,
            "acc": 1, "agl": 18, "eva": 0, "luck": 15
        },
        "gil": 3000,
        "steal": {"common": "Hi-Potion", "rare": "X-Potion"},
        "bribe": None,
        "drop": {"common": "Power Sphere x1", "rare": "Power Sphere x2"},
        "equipment_drop": "1-2 slots, 1-2 abilities, 50% chance",
        "weapon_abilities": ["Piercing", "Counterattack"],
        "armor_abilities": ["SOS Haste", "HP +10%"],
        "immunities": ["Poison", "Petrify", "Slow", "Zombie", "Death", "Reflect", "Bribe", "Capture"],
        "status_resistances": {"Silence": "20", "Sleep": "20", "Darkness": "20", "Doom": "0 (5 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Wendigo-enemy-ffx.webp"
    },

    "Yenke Ronso": {
        "zanmato_lv": 4,
        "hp": "Varies",
        "hp_overkill": 2500,
        "mp": 200,
        "ap": 4500,
        "ap_overkill": 6750,
        "location": "Mt. Gagazet",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": 30, "mdef": 10,
            "acc": 100, "agl": "Varies", "eva": 0, "luck": 15
        },
        "gil": 1500,
        "steal": {"common": "Lv. 3 Key Sphere x1", "rare": "Lv. 3 Key Sphere x2"},
        "bribe": None,
        "drop": {"common": "Return Sphere x1", "rare": "Friend Sphere x1"},
        "equipment_drop": "2-3 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Piercing"],
        "armor_abilities": ["MP +20%"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Threaten", "Death", "Provoke", "Reflect", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Doom": "0 (20 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yenke_Ronso_Render.webp"
    },

    "Yojimbo (Sunken Cave)": {
        "zanmato_lv": 1,
        "hp": 33000,
        "hp_overkill": 4060,
        "mp": 2000,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Cavern of the Stolen Fayth",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 34, "mag": 35, "def": 80, "mdef": 1,
            "acc": 1, "agl": 32, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Doom": "0 (5 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yojimbo-FFX.webp"
    },

    "Yojimbo (Remiem Temple)": {
        "zanmato_lv": 1,
        "hp": 32000,
        "hp_overkill": 32000,
        "mp": 1200,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Remiem Temple",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 30, "mag": 45, "def": 1, "mdef": 1,
            "acc": 15, "agl": 25, "eva": 50, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Demi", "Distill", "Sensor", "Scan", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Doom": "0 (5 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yojimbo-FFX.webp"
    },

    "Yojimbo (Sin)": {
        "zanmato_lv": 3,
        "hp": "Varies",
        "hp_overkill": 169,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": "Varies", "mag": "Varies", "def": "Varies", "mdef": "Varies",
            "acc": "Varies", "agl": "Varies", "eva": "Varies", "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yojimbo-FFX.webp"
    },

    "Yu Pagoda": {
        "zanmato_lv": 5,
        "hp": 5000,
        "hp_overkill": 0,
        "mp": 5000,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Sin (Dream's End)",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 20, "def": 1, "mdef": 50,
            "acc": 0, "agl": 40, "eva": 0, "luck": 15
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Threaten", "Death", "Provoke", "Doom", "Shell", "Protect", "Reflect", "Regen", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {"Slow": "50"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yu_Pagoda.webp"
    },

    "Yu Yevon": {
        "zanmato_lv": 5,
        "hp": 99999,
        "hp_overkill": 99999,
        "mp": 1,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Inside Sin",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 1, "mag": 200, "def": 1, "mdef": 1,
            "acc": 1, "agl": 44, "eva": 0, "luck": 1
        },
        "gil": 0,
        "steal": None,
        "bribe": None,
        "drop": None,
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Petrify", "Threaten", "Death", "Scan", "Bribe", "Berserk", "Capture"],
        "status_resistances": {"Poison": "0 (10 max HP removed each turn)", "Doom": "0 (3 turns until death)"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yu_Yevon.webp"
    },

    "Yunalesca (First)": {
        "zanmato_lv": 4,
        "hp": 24000,
        "hp_overkill": 0,
        "mp": 500,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 30, "def": 50, "mdef": 50,
            "acc": 1, "agl": 40, "eva": 0, "luck": 20
        },
        "gil": 0,
        "steal": {"common": "Stamina Tablet", "rare": "Farplane Wind"},
        "bribe": None,
        "drop": {"common": "Lv. 3 Key Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Death", "Provoke", "Doom", "Demi", "Distill", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Threaten": "75"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yunalesca-enemy-ffx.webp"
    },

    "Yunalesca (Second)": {
        "zanmato_lv": 4,
        "hp": 48000,
        "hp_overkill": 0,
        "mp": 500,
        "ap": 0,
        "ap_overkill": 0,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 30, "def": 50, "mdef": 50,
            "acc": 1, "agl": 40, "eva": 0, "luck": 20
        },
        "gil": 0,
        "steal": {"common": "Stamina Tablet", "rare": "Farplane Wind"},
        "bribe": None,
        "drop": {"common": "Lv. 3 Key Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "0 slots, 0 abilities, 25% chance",
        "weapon_abilities": [],
        "armor_abilities": [],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Death", "Provoke", "Doom", "Demi", "Distill", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Threaten": "75"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yunalesca_2-enemy-ffx.webp"
    },

    "Yunalesca (Third)": {
        "zanmato_lv": 4,
        "hp": 60000,
        "hp_overkill": 10000,
        "mp": 500,
        "ap": 14000,
        "ap_overkill": 21000,
        "location": "Zanarkand Dome",
        "monster_arena": "Does not appear",
        "stats": {
            "str": 20, "mag": 30, "def": 50, "mdef": 50,
            "acc": 1, "agl": 40, "eva": 0, "luck": 20
        },
        "gil": 9000,
        "steal": {"common": "Stamina Tablet", "rare": "Farplane Wind"},
        "bribe": None,
        "drop": {"common": "Lv. 3 Key Sphere x1", "rare": "Lv. 3 Key Sphere x1"},
        "equipment_drop": "2-4 slots, 1 ability, 100% chance",
        "weapon_abilities": ["Piercing", "Zombiestrike"],
        "armor_abilities": ["Zombieproof"],
        "immunities": ["Silence", "Sleep", "Darkness", "Poison", "Petrify", "Slow", "Zombie", "Power Break", "Magic Break", "Armor Break", "Mental Break", "Death", "Provoke", "Doom", "Demi", "Distill", "Bribe", "Delay", "Berserk", "Capture"],
        "status_resistances": {"Threaten": "75"},
        "elemental_affinities": {
            "weak": [],
            "resisted": [],
            "immune": [],
            "absorb": []
        },
        "image": "./images/Yunalesca_3-enemy-ffx.webp"
    },

}


def get_enemy_names():
    """Returns a sorted list of all enemy names."""
    return sorted(ENEMIES.keys())


def get_enemy_zanmato_level(enemy_name):
    """
    Returns the Zanmato level for a given enemy.
    Returns None if enemy not found or has no Zanmato level.
    """
    enemy = ENEMIES.get(enemy_name)
    if enemy:
        return enemy.get("zanmato_lv")
    return None


def get_enemy_info(enemy_name):
    """Returns full enemy information dictionary."""
    return ENEMIES.get(enemy_name)


def search_enemies(query):
    """Search for enemies by partial name match."""
    query_lower = query.lower()
    matches = []
    for name in ENEMIES:
        if query_lower in name.lower():
            matches.append(name)
    return sorted(matches)


def get_enemy_full_stats(enemy_name):
    """Returns detailed stats for an enemy including all combat stats."""
    enemy = ENEMIES.get(enemy_name)
    if not enemy:
        return None
    return enemy.get("stats", {})


def get_enemy_immunities(enemy_name):
    """Returns list of status effects the enemy is immune to."""
    enemy = ENEMIES.get(enemy_name)
    if not enemy:
        return []
    return enemy.get("immunities", [])


def get_enemy_weaknesses(enemy_name):
    """Returns dictionary of enemy weaknesses (status effects with % chance)."""
    enemy = ENEMIES.get(enemy_name)
    if not enemy:
        return {}
    return enemy.get("weaknesses", {})


def get_enemy_drops(enemy_name):
    """Returns dictionary with common and rare item drops."""
    enemy = ENEMIES.get(enemy_name)
    if not enemy:
        return None
    return enemy.get("drop", {})


def get_enemy_steal(enemy_name):
    """Returns dictionary with common and rare items that can be stolen."""
    enemy = ENEMIES.get(enemy_name)
    if not enemy:
        return None
    return enemy.get("steal", {})
