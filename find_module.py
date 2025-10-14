import os
import json
from utils import load_database, print_contacts, normalize_number

def find_contact(db_name):
    data = load_database(db_name)
    print(f"Opening file: {db_name}")
    print_contacts(data)

    try:
        print("""\nFind contact by:
    1) name 
    2) phone number""")
        action_number = int(input(''))
        if action_number == 1:
            search_value = input('Enter search criteria...').strip().lower()
            for contact in data.get("contacts", []):
                if contact.get("name", "").strip().lower() == search_value:
                    return contact
        if action_number == 2:
            search_value = input('Enter search criteria...').strip()
            for contact in data.get("contacts", []):
                if normalize_number(contact.get("number")) == search_value:
                    return contact

        print('\nExiting')
    except ValueError:
        print('\nInvalid literal for int()')
    print("Contact not found.")
    return None

if __name__ == '__main__':
    from phonebook import DEFAULT_DATABASE_NAME
    result = find_contact(DEFAULT_DATABASE_NAME)
    print(result)