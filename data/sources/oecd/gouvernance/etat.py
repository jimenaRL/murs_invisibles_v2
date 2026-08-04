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
            'OECD.GOV.GIP,DSD_GOV@DF_GOV_EMPPS_REP_2023,1.0+A.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'OECD.GOV.GIP,DSD_GOV@DF_GOV_EMPPS_REP_2023,1.0+A.csv': ['no_process'],
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
            'OECD.GOV.GIP,DSD_GOV@DF_GOV_EMPPS_REP_2023,1.0+A.csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'OECD.GOV.GIP,DSD_GOV@DF_GOV_EMPPS_REP_2023,1.0+A.csv': 2016,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'OECD.GOV.GIP,DSD_GOV@DF_GOV_EMPPS_REP_2023,1.0+A.csv': 'perc_2v',
        }
    },
    "sorter": {
        'fns': {
            'OECD.GOV.GIP,DSD_GOV@DF_GOV_EMPPS_REP_2023,1.0+A.csv': 'date_country',
        }
    },
}

Processer(config).process()
