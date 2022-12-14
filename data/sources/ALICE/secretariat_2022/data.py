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
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": ["remove_prop"],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['part de femmes'],
        },
    },
    "mapper": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "proportion100",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "none",
        }
    },
}

Processer(config).process()
