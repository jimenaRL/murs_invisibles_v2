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
            "VIOLENCES_LOCALES_93 - Violences locales 93_2022.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "VIOLENCES_LOCALES_93 - Violences locales 93_2022.csv": ["virg2point"],
        },
        'rename': {
            'country': ['PAYS'],
            'year': ['Année'],
            'indicator': ['Data'],
            'value': ['Valeur %'],
        },
    },
    "mapper": {
        'fns': {
            "VIOLENCES_LOCALES_93 - Violences locales 93_2022.csv": "proportion100",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "VIOLENCES_LOCALES_93 - Violences locales 93_2022.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "VIOLENCES_LOCALES_93 - Violences locales 93_2022.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "VIOLENCES_LOCALES_93 - Violences locales 93_2022.csv": "none",
        }
    },
}

Processer(config).process()
