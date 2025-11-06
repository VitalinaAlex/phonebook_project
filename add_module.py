import os
import json
from utils import load_database, save_database

__DEVELOPMENT_MODE__ = os.environ.get('DEVELOPMENT_MODE', False)

def add_contact(db_name):
    phone_number = "123"
    name = ""
    city = ""

    if __DEVELOPMENT_MODE__:
        phone_number = "123"
        name = "User1"
        city = "City1"
    else:
        phone_number = input('enter number, only digits ').strip()
        if not phone_number.isdigit() or len(phone_number) < 10 or len(phone_number) > 12:
            msg = "ONLY digits for number. Max number of digits - 12, min - 10"
            return msg
        phone_number = int(phone_number)
        name = input('enter name ').strip()
        city = input('enter city ').strip()

    datum = {'number': phone_number, 'name': name, 'city': city}

    db = load_database(db_name)
    db['contacts'].append(datum)
    save_database(db_name, db)
    print('Data added to notebook')
    return datum

if __name__ == '__main__':
    from phonebook import DEFAULT_DATABASE_NAME
    result = add_contact(DEFAULT_DATABASE_NAME)
    print(result)