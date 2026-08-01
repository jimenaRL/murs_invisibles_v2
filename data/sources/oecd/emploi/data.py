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
            'temps_partial_freq.csv': 'sep_save',
            'temps_plein_freq.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'temps_partial_freq.csv': ['get_wm_oecd_2026', 'diffFH'],
            'temps_plein_freq.csv': ['get_wm_oecd_2026', 'diffFH'],
        },
        'rename': {
            'country': ['Reference area'],
            'year': ['TIME_PERIOD'],
            'indicator': ['Working time arrangement'],
            'value': ['OBS_VALUE'],
        },
    },
    "mapper": {
        'fns': {
            'temps_partial_freq.csv': 'diffFH_100',
            'temps_plein_freq.csv': 'diffFH_100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'temps_partial_freq.csv': 2000,
            'temps_plein_freq.csv': 2000,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'temps_partial_freq.csv': 'diff_pp',
            'temps_plein_freq.csv': 'diff_pp',
        }
    },
    "sorter": {
        'fns': {
            'temps_partial_freq.csv': 'date_country',
            'temps_plein_freq.csv': 'date_country',
        }
    },
}

Processer(config).process()
