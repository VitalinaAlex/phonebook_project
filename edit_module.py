import os
import json
from utils import load_database, save_database, print_contacts, normalize_number

def edit_contact(db_name):
    print(f"Opening file: {db_name}")
    data = load_database(db_name)
    print_contacts(data)

    search_value = input('Enter search criteria (number): ').strip()
    for contact in data.get("contacts", []):
        if normalize_number(contact.get("number")) == search_value:
            print(f"Found contact: {contact}")

            new_name = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ").strip()
            new_city = input(f"Enter new city (or press Enter to keep '{contact['city']}'): ").strip()
            new_number = input(f"Enter new number (or press Enter to keep '{contact['number']}'): ").strip()

            if new_name:
                contact["name"] = new_name
            if new_city:
                contact["city"] = new_city
            if new_number:
                if new_number.isdigit():
                    contact["number"] = int(new_number)
                else:
                    print("ONLY digits for number. Number not changed.")

            save_database(db_name, data)
            print("Contact updated successfully!")
            return contact

    print("\nExiting")
    print("Contact not found.")
    return None

if __name__ == '__main__':
    from phonebook import DEFAULT_DATABASE_NAME
    result = edit_contact(DEFAULT_DATABASE_NAME)
    print(result)