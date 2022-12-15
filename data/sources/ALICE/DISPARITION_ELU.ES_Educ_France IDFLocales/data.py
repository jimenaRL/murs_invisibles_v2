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
            "DISPARITION_ELU.ES_Educ_France_ IDF_Locales - FUSION_Disparition_FR_locales_93.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "DISPARITION_ELU.ES_Educ_France_ IDF_Locales - FUSION_Disparition_FR_locales_93.csv": [],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['Valeur Part de femmes %'],
        },
    },
    "mapper": {
        'fns': {
            "DISPARITION_ELU.ES_Educ_France_ IDF_Locales - FUSION_Disparition_FR_locales_93.csv": "proportion100",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "DISPARITION_ELU.ES_Educ_France_ IDF_Locales - FUSION_Disparition_FR_locales_93.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "DISPARITION_ELU.ES_Educ_France_ IDF_Locales - FUSION_Disparition_FR_locales_93.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "DISPARITION_ELU.ES_Educ_France_ IDF_Locales - FUSION_Disparition_FR_locales_93.csv": "none",
        }
    },
}

Processer(config).process()
