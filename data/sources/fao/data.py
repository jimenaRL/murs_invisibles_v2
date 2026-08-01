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
            'FAO-DF_SDG_5_A_1-1.0-all.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'FAO-DF_SDG_5_A_1-1.0-all.csv': ['no_process'],
        },
        'rename': {
            'country': ['Area', 'LOCATION'],
            'year': ['TIME_PERIOD', 'TIME'],
            'indicator': ['SDG Series', 'SUBJECT'],
            'value': ['OBS_VALUE'],
        },
    },
    "mapper": {
        'fns': {
            'FAO-DF_SDG_5_A_1-1.0-all.csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'FAO-DF_SDG_5_A_1-1.0-all.csv': 2000,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'FAO-DF_SDG_5_A_1-1.0-all.csv': 'perc',
        }
    },
    "sorter": {
        'fns': {
            'FAO-DF_SDG_5_A_1-1.0-all.csv': 'date_country',
        }
    },
}

Processer(config).process()
