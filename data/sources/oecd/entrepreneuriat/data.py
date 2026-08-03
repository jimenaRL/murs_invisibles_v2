import os
from murs_invisibles import Processer


file_dir = os.path.dirname(os.path.realpath(__file__))
filter_indicator_path = os.path.join(file_dir, 'indicator_filter.txt')

config = {
    "base_path": os.path.dirname(os.path.realpath(__file__)),
    "origin_language": "en",
    "io": {
        "header": 0,
        "encoding": 'utf-8',
        "fns": {
            'OECD.DEV.NPG,DSD_GID@DF_GID_2023,+.RAPFR_AFS_PCT_1.PT_POP.....csv': 'sep_save',
            "OECD.ENV.EPI,DSD_PAT_DEV@DF_PAT_DEV,1.0+.A.ENV_PAT.PT_PATN.ONE.F.csv": 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'OECD.DEV.NPG,DSD_GID@DF_GID_2023,+.RAPFR_AFS_PCT_1.PT_POP.....csv': ['get_wm_oecd_2026', 'diffFH'],
            'OECD.ENV.EPI,DSD_PAT_DEV@DF_PAT_DEV,1.0+.A.ENV_PAT.PT_PATN.ONE.F.csv': ['no_process'],
        },
        'rename': {
            'country': ['Reference area'],
            'year': ['TIME_PERIOD'],
            'indicator': ['Measure'],
            'value': ['OBS_VALUE'],
        },
    },
    "mapper": {
        'fns': {
            'OECD.DEV.NPG,DSD_GID@DF_GID_2023,+.RAPFR_AFS_PCT_1.PT_POP.....csv': 'diffFH_100',
            'OECD.ENV.EPI,DSD_PAT_DEV@DF_PAT_DEV,1.0+.A.ENV_PAT.PT_PATN.ONE.F.csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'OECD.DEV.NPG,DSD_GID@DF_GID_2023,+.RAPFR_AFS_PCT_1.PT_POP.....csv': 2000,
            'OECD.ENV.EPI,DSD_PAT_DEV@DF_PAT_DEV,1.0+.A.ENV_PAT.PT_PATN.ONE.F.csv': 2000,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'OECD.DEV.NPG,DSD_GID@DF_GID_2023,+.RAPFR_AFS_PCT_1.PT_POP.....csv': 'diff_pp1',
            'OECD.ENV.EPI,DSD_PAT_DEV@DF_PAT_DEV,1.0+.A.ENV_PAT.PT_PATN.ONE.F.csv': 'perc_2v',
        }
    },
    "sorter": {
        'fns': {
            'OECD.DEV.NPG,DSD_GID@DF_GID_2023,+.RAPFR_AFS_PCT_1.PT_POP.....csv': 'date_country',
            'OECD.ENV.EPI,DSD_PAT_DEV@DF_PAT_DEV,1.0+.A.ENV_PAT.PT_PATN.ONE.F.csv': 'date_country',
        }
    },
}

Processer(config).process()
