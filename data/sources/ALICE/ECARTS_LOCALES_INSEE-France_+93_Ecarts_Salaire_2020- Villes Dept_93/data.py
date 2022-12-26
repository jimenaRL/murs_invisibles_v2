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
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - FUSION_ECART_Locales_93.csv": "one_save",
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - Villes_DPT_93_Ecarts_salaires_2020.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - FUSION_ECART_Locales_93.csv": ["percRel100"],
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - Villes_DPT_93_Ecarts_salaires_2020.csv": ["percRel100"],
        },
        'rename': {
            'country': ['pays'],
            'year': ['annee'],
            'indicator': ['nom'],
            'value': ['value'],
            'value_men': ['taux hommes parmi hommes', 'salaire hommes'],
            'value_women': ['taux femmes parmi femmes', 'salaire femmes'],
        },
    },
    "mapper": {
        'fns': {
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - FUSION_ECART_Locales_93.csv": "diffHFPROP",
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - Villes_DPT_93_Ecarts_salaires_2020.csv": "diffHFPROP",
            }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - FUSION_ECART_Locales_93.csv": 2010,
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - Villes_DPT_93_Ecarts_salaires_2020.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - FUSION_ECART_Locales_93.csv": "diff_perc",
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - Villes_DPT_93_Ecarts_salaires_2020.csv": "diff_perc",
        }
    },
    "sorter": {
        'fns': {
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - FUSION_ECART_Locales_93.csv": "none",
            "ECARTS_LOCALES_INSEE-France_+93_Ecarts_Salaire_2020- Villes Dept_93 - Villes_DPT_93_Ecarts_salaires_2020.csv": "none",
        }
    },
}

Processer(config).process()
