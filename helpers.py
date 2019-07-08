import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Removes schoolkid's bad marks and chaisements and adding commadations")
    parser.add_argument('full_name', help='Schoolkid name. For example "Фролов Иван"')
    parser.add_argument('subject', help='Subject. For example "Математика"')
    parser.add_argument('--qty', help='Qty of commadations')
    return parser.parse_args()


def load_compliments():
    with open('datacenter/compliments.txt') as file:
        return file.read().split('\n')
