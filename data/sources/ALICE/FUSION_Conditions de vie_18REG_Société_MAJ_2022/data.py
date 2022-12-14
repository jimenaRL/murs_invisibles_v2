import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Données sociales_MàJ_2022.csv": "one_save",
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Conditions de vie_MàJ_2022_temps.csv": "one_save"
        },
    },
    "preprocesser": {
        'fns': {
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Données sociales_MàJ_2022.csv": ["virg2point"],
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Conditions de vie_MàJ_2022_temps.csv": [],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['valeur ecart neg ou pos', 'différence en minutes'],
        },
    },
    "mapper": {
        'fns': {
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Données sociales_MàJ_2022.csv": "proportion100",
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Conditions de vie_MàJ_2022_temps.csv": "diff_fm_minutes",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Données sociales_MàJ_2022.csv": 2010,
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Conditions de vie_MàJ_2022_temps.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Données sociales_MàJ_2022.csv": "diff_perc",
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Conditions de vie_MàJ_2022_temps.csv": "diff_minutes",
        }
    },
    "sorter": {
        'fns': {
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Données sociales_MàJ_2022.csv": "none",
            "FUSION_Conditions de vie_18REG_Société_MAJ_2022 - Conditions de vie_MàJ_2022_temps.csv": "none",
        }
    },
}

Processer(config).process()
