import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Schoolkid
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from helpers import parse_args, load_compliments


def main():
    args = parse_args()
    full_name = args.full_name
    subject = args.subject
    qty = args.qty or 1

    try:
        compliments = load_compliments()
    except:
        print('Compliments list not found')

    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    except ObjectDoesNotExist:
        print(f"Schoolkid {full_name} didn't found")
        return
    except MultipleObjectsReturned:
        print('More than one schoolkid found. Please specify fullname')
        return

    print(schoolkid.fix_marks())
    print(schoolkid.remove_chastisements())
    print(schoolkid.create_commendation(subject, compliments, qty))


if __name__ == "__main__":
    main()