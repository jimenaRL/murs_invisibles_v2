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
            'OECD.WISE.RSB,DSD_SDG@DF_SDG_G_5,2.0+..5_5.C050501.._T.._T._T._T..csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'OECD.WISE.RSB,DSD_SDG@DF_SDG_G_5,2.0+..5_5.C050501.._T.._T._T._T..csv': ['no_process'],
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
            'OECD.WISE.RSB,DSD_SDG@DF_SDG_G_5,2.0+..5_5.C050501.._T.._T._T._T..csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'OECD.WISE.RSB,DSD_SDG@DF_SDG_G_5,2.0+..5_5.C050501.._T.._T._T._T..csv': 2000,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'OECD.WISE.RSB,DSD_SDG@DF_SDG_G_5,2.0+..5_5.C050501.._T.._T._T._T..csv': 'perc_2v',
        }
    },
    "sorter": {
        'fns': {
            'OECD.WISE.RSB,DSD_SDG@DF_SDG_G_5,2.0+..5_5.C050501.._T.._T._T._T..csv': 'date_country',
        }
    },
}

Processer(config).process()
