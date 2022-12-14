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
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "one_save",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": ["remove_prop"],
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": ["remove_prop"],
        },
        'rename': {
            'country': ['PAYS'],
            'year': ['DATE'],
            'indicator': ['DATA'],
            'value': ['Part de femmes %', 'Ecart %'],
        },
    },
    "mapper": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "proportion100",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": 2010,
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "perc",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "none",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "none",
        }
    },
}

Processer(config).process()
