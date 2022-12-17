import os
import json
import pandas as pd
from murs_invisibles import Processer


config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "fr",
    "merge": {
        "secretariat_2022 - secret_ECART_PP%": [
            "secretariat_2022 - secret_ECART_PP%_HF.csv",
            "secretariat_2022 - secret_ECART_PP%_FF.csv"
        ]
    },
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            # "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "one_save",
            "secretariat_2022 - secret_ECART_PP%_HF.csv": "one_save",
            "secretariat_2022 - secret_ECART_PP%_FF.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": ["remove_prop"],
            "secretariat_2022 - secret_ECART_PP%_HF.csv": [],
            "secretariat_2022 - secret_ECART_PP%_FF.csv": [],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': [
                'part de femmes',
                'taux femmes / taux hommes',
                'taux femmes / taux autre'
            ],
        },
    },
    "mapper": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "proportion100",
            "secretariat_2022 - secret_ECART_PP%_HF.csv": "fois_plus_moins",
            "secretariat_2022 - secret_ECART_PP%_FF.csv": "fois_plus_moins",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": 2010,
            "secretariat_2022 - secret_ECART_PP%_HF.csv": 2010,
            "secretariat_2022 - secret_ECART_PP%_FF.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "perc",
            "secretariat_2022 - secret_ECART_PP%_HF.csv": "fois_plus_moins",
            "secretariat_2022 - secret_ECART_PP%_FF.csv": "fois_plus_moins",
        }
    },
    "sorter": {
        'fns': {
            "secretariat_2022 - secret_part de femmes_MàJ_2022.csv": "none",
            "secretariat_2022 - secret_ECART_PP%_HF.csv": "none",
            "secretariat_2022 - secret_ECART_PP%_FF.csv": "none",
        }
    },
}

Processer(config).process()
