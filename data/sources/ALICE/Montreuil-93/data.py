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
            "Montreuil-93 - DD91_Familles monoparentales.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": [],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['valeur'],
        },
    },
    "mapper": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": "fois_plus_moins",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": "fois_plus_moins",
        }
    },
    "sorter": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": "none",
        }
    },
}

Processer(config).process()
