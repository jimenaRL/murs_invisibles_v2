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
            "Montreuil-93 - NAT2-MONTREUIL-FH.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": [],
            "Montreuil-93 - NAT2-MONTREUIL-FH.csv": ["remove_div_and_zero"],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['valeur femmes / valeur hommes'],
        },
    },
    "mapper": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": "fois_plus_moins_1",
            "Montreuil-93 - NAT2-MONTREUIL-FH.csv": "fois_plus_moins_01",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": 2010,
            "Montreuil-93 - NAT2-MONTREUIL-FH.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": "fois_plus_moins",
            "Montreuil-93 - NAT2-MONTREUIL-FH.csv": "fois_plus_moins",
        }
    },
    "sorter": {
        'fns': {
            "Montreuil-93 - DD91_Familles monoparentales.csv": "none",
            "Montreuil-93 - NAT2-MONTREUIL-FH.csv": "none",
        }
    },
}

Processer(config).process()
