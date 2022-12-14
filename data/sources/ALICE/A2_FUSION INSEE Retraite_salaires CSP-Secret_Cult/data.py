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
            "A2_FUSION INSEE Retraite_salaires CSP-Secret_Cult - FUSION INSEE Salaires Retraites et Inc 18_A2.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "A2_FUSION INSEE Retraite_salaires CSP-Secret_Cult - FUSION INSEE Salaires Retraites et Inc 18_A2.csv": ["virg2point"],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['valeur %'],
        },
    },
    "mapper": {
        'fns': {
            "A2_FUSION INSEE Retraite_salaires CSP-Secret_Cult - FUSION INSEE Salaires Retraites et Inc 18_A2.csv": "diffHFPROP",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "A2_FUSION INSEE Retraite_salaires CSP-Secret_Cult - FUSION INSEE Salaires Retraites et Inc 18_A2.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "A2_FUSION INSEE Retraite_salaires CSP-Secret_Cult - FUSION INSEE Salaires Retraites et Inc 18_A2.csv": "diff_perc_0v",
        }
    },
    "sorter": {
        'fns': {
            "A2_FUSION INSEE Retraite_salaires CSP-Secret_Cult - FUSION INSEE Salaires Retraites et Inc 18_A2.csv": "none",
        }
    },
}

Processer(config).process()
