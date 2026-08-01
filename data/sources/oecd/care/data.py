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
            'unpaid_care_and_domestic_work.csv': 'sep_save'
        },
    },
    "preprocesser": {
        'fns': {
            'unpaid_care_and_domestic_work.csv': ['get_wm_oecd_2026', 'diffFH', 'dropna'],
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
            'unpaid_care_and_domestic_work.csv': 'abstanh_4'
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'unpaid_care_and_domestic_work.csv': 2000
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'unpaid_care_and_domestic_work.csv': 'diff_hours'
        }
    },
    "sorter": {
        'fns': {
            'unpaid_care_and_domestic_work.csv': 'date_country'
        }
    },
}

Processer(config).process()
