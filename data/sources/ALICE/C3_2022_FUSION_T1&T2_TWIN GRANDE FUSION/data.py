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
            "C3_2022_FUSION_T1&T2_TWIN GRANDE FUSION - Fusion_T2_ECarts_C3.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "C3_2022_FUSION_T1&T2_TWIN GRANDE FUSION - Fusion_T2_ECarts_C3.csv": ["remove_prop", "virg2point"],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['valeur  %'],
        },
    },
    "mapper": {
        'fns': {
            "C3_2022_FUSION_T1&T2_TWIN GRANDE FUSION - Fusion_T2_ECarts_C3.csv": "diffHFPROP",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "C3_2022_FUSION_T1&T2_TWIN GRANDE FUSION - Fusion_T2_ECarts_C3.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "C3_2022_FUSION_T1&T2_TWIN GRANDE FUSION - Fusion_T2_ECarts_C3.csv": "diff_perc",
        }
    },
    "sorter": {
        'fns': {
            "C3_2022_FUSION_T1&T2_TWIN GRANDE FUSION - Fusion_T2_ECarts_C3.csv": "none",
        }
    },
}

Processer(config).process()
