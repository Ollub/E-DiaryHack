import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser(
        description="Removes schoolkid's bad marks and chaisements and adding commendations")
    parser.add_argument('full_name', help='Schoolkid name. For example "Фролов Иван"')
    parser.add_argument('subject', help='Subject. For example "Математика"')
    parser.add_argument('--qty', help='Qty of commedations', type=int)
    parser.add_argument('-s', '--script', help=
        '''Define wich script to run.
        "f" - to fix bad marks;
        "r" - remove chastisements;
        "c" - create commendations.
        If no param passed, all scripts will be runed'''
    )
    return parser.parse_args()


def load_compliments():
    with open('datacenter/compliments.txt') as file:
        return file.readlines()


def filter_list(list_to_filter: list, condition=r'\w{3,}') -> list:
    regexp = re.compile(condition)
    filtered_list = list(filter(lambda element: regexp.search(element), list_to_filter))
    return filtered_list