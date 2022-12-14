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
            # "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "one_save",
            # "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "one_save",
            # "OCDE_MISE-à_JOUR_2022DE---OCDE_TPS_Partiel_MàJ_2022.csv": "one_save",
            # "OCDE_MISE-à_JOUR_2022DE---OCDE_ENT_Inventrices_fusion_Poste_Directi_MàJ_2022.csv": "one_save",
            # "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_Titres_fonciers_MàJ_2022.csv": "one_save",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP4_TV.csv": "one_save",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP5_arts culture.csv": "one_save",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP3_arts.csv": "one_save",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - Observatoire_group2_TH_.csv": "one_save",
        },
    },
    "preprocesser": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": ["remove_prop"],
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": ["remove_prop"],
            "OCDE_MISE-à_JOUR_2022DE---OCDE_TPS_Partiel_MàJ_2022.csv": ["remove_prop"],
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ENT_Inventrices_fusion_Poste_Directi_MàJ_2022.csv": ["remove_prop"],
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_Titres_fonciers_MàJ_2022.csv": ["virg2point"],
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP4_TV.csv": ["remove_prop"],
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP5_arts culture.csv": ["remove_prop"],
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP3_arts.csv": ["remove_prop"],
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - Observatoire_group2_TH_.csv": ["remove_prop"],
        },
        'rename': {
            'country': ['PAYS', 'pays'],
            'year': ['DATE', 'annee'],
            'indicator': ['DATA', 'nom'],
            'value': ['Part de femmes %', 'Ecart %', 'Value %', 'valeur'],
        },
    },
    "mapper": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "proportion100",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "diffHFPROP",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_TPS_Partiel_MàJ_2022.csv": "proportion100",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ENT_Inventrices_fusion_Poste_Directi_MàJ_2022.csv": "proportion100",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_Titres_fonciers_MàJ_2022.csv": "proportion100",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP4_TV.csv": "proportion100",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP5_arts culture.csv": "proportion100",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP3_arts.csv": "proportion100",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - Observatoire_group2_TH_.csv": "proportion100",
        }
    },
    "filter": {
        'filter_indicator_path': None,
        'year': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": 2010,
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": 2010,
            "OCDE_MISE-à_JOUR_2022DE---OCDE_TPS_Partiel_MàJ_2022.csv": 2010,
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ENT_Inventrices_fusion_Poste_Directi_MàJ_2022.csv": 2010,
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_Titres_fonciers_MàJ_2022.csv": 2010,
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP4_TV.csv": 2010,
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP5_arts culture.csv": 2010,
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP3_arts.csv": 2010,
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - Observatoire_group2_TH_.csv": 2010,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "perc",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "diff_perc",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_TPS_Partiel_MàJ_2022.csv": "perc",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ENT_Inventrices_fusion_Poste_Directi_MàJ_2022.csv": "perc",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_Titres_fonciers_MàJ_2022.csv": "perc",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP4_TV.csv": "perc",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP5_arts culture.csv": "perc",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP3_arts.csv": "perc",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - Observatoire_group2_TH_.csv": "perc",
        }
    },
    "sorter": {
        'fns': {
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ONU_GOV_Minist_Parlement_MàJ_2022.csv": "none",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_SALAIRE_MàJ_2022.csv": "none",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_TPS_Partiel_MàJ_2022.csv": "none",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ENT_Inventrices_fusion_Poste_Directi_MàJ_2022.csv": "none",
            "OCDE_MISE-à_JOUR_2022DE---OCDE_ECARTS_Titres_fonciers_MàJ_2022.csv": "none",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP4_TV.csv": "none",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP5_arts culture.csv": "none",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - OBS_GROUP3_arts.csv": "none",
            "Observatoire_MàJ_2022_Fusion MàJ Audiens - Observatoire_group2_TH_.csv": "none",
        }
    },
}

Processer(config).process()
