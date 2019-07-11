import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Schoolkid
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from helpers import parse_args, load_compliments, filter_list


def main():
    args = parse_args()
    full_name = args.full_name
    subject = args.subject
    qty = args.qty or 1
    scripts_to_run = args.script or 'frc'

    try:
        compliments = filter_list(load_compliments())
    except FileNotFoundError:
        print('Compliments list not found. \
Please check that "./datacenter/compliments.txt" exists and run script again')
        return

    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except ObjectDoesNotExist:
        print(f"Schoolkid {full_name} didn't found")
        return
    except MultipleObjectsReturned:
        print('More than one schoolkid found. Please run script again and specify fullname')
        schoolkids = Schoolkid.objects.filter(full_name__contains=full_name)
        for schoolkid in schoolkids:
            print(schoolkid)
        return

    if 'f' in scripts_to_run:
        marks_num = schoolkid.fix_marks()
        print(f'{marks_num} marks fixed')
    if 'r' in scripts_to_run:
        chastisements_num = schoolkid.remove_chastisements()
        print(f'{chastisements_num} chastisements deleted')
    if 'c' in scripts_to_run:
        commendations_num = schoolkid.create_commendation(subject, compliments, qty)
        if commendations_num:
            print(f'{commendations_num} commendations created')
        else:
            print('No lessons found to create commendations!')


if __name__ == "__main__":
    main()