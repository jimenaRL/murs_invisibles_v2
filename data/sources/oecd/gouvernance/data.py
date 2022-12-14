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
            'GOV_2021_13122022145537216.csv': 'sep_save',
        },
    },
    "preprocesser": {
        'fns': {
            'GOV_2021_13122022145537216.csv': ['no_process'],
        },
        'rename': {
            'country': ['Country', 'LOCATION'],
            'year': ['Year', 'TIME'],
            'indicator': ['Indicator', 'SUBJECT'],
            'value': ['Value'],
        },
    },
    "mapper": {
        'fns': {
            'GOV_2021_13122022145537216.csv': 'proportion100',
        }
    },
    "filter": {
        'filter_indicator_path': filter_indicator_path,
        'year': {
            'GOV_2021_13122022145537216.csv': 2019,
        }
    },
    "translator": {
    },
    "postprocesser": {
        'fns': {
            'GOV_2021_13122022145537216.csv': 'perc',
        }
    },
    "sorter": {
        'fns': {
            'GOV_2021_13122022145537216.csv': 'date_country',
        }
    },
}

Processer(config).process()
