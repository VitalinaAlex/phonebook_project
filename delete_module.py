import os
import json
from utils import load_database, save_database, print_contacts, normalize_number

def delete_contact(db_name):
    print(f"Opening file: {db_name}")
    data = load_database(db_name)
    print_contacts(data)

    search_value = input("Enter search criteria (number): ").strip()

    contact_delete = None
    for contact in data.get("contacts", []):
        if normalize_number(contact.get("number")) == search_value:
            contact_delete = contact
            break

    if contact_delete:
        print(f"Found contact: {contact_delete}")
        data["contacts"] = [
            c for c in data["contacts"]
            if normalize_number(c["number"]) != search_value
        ]
        save_database(db_name, data)
        print("Contact deleted successfully!")
        return contact_delete
    else:
        print("Contact not found.")

    print("\nExiting")
    return None

if __name__ == '__main__':
    from phonebook import DEFAULT_DATABASE_NAME
    result = delete_contact(DEFAULT_DATABASE_NAME)
    print(result)