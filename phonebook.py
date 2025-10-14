"""Phonebook application;
Functionality:
    - Add data into database
    - Delete data from database by id
    - Find contact by:
        - name
        - phone number
    - Update contact
    - List all contacts

Data format:
    - id
    - phone number
    - name
    - city

DATABASE_FORMAT_EXAMPLE:
{
  "contacts": [
      {
          "phone_number": 123,
          "name": "",
          "city": ""
      },
    ]
}
"""
import json
import os.path

from add_module import add_contact
from edit_module import edit_contact
from find_module import find_contact
from delete_module import delete_contact
from list_module import list_contact


DEFAULT_DATABASE_NAME = os.path.join(os.path.dirname(__file__), "phonebook.json")


def validate_user_input(data):
    clean_data = data.strip()
    if not clean_data.isnumeric():
        raise ValueError('Use numbers to enter action')
    action_number = int(clean_data)
    if action_number not in [1, 2, 3, 4, 5]:
        raise ValueError('Action should be one off ...')
    return action_number

AVAILABLE_FUNCTIONAL_INFO = """\n
This is a phone book application.
Available options are:
    1) Add
    2) Search
    3) Update
    4) Delete
    5) List
your contacts. Else - EXIT
"""


def ensure_database(name=DEFAULT_DATABASE_NAME):
    if not os.path.exists(name):
        empty_db = {'contacts': []}
        json.dump(empty_db, open(name, 'w'))


if __name__ == '__main__':
    ensure_database()
    
    while True:
        print(AVAILABLE_FUNCTIONAL_INFO)
        user_input = input('Choose an action (1-5, anything else to exit): ').strip()
        
        if not user_input.isdigit():
            print("Exiting program.")
            break
        
        action_number = int(user_input)
        
        if action_number == 1:
            add_contact(DEFAULT_DATABASE_NAME)
        elif action_number == 2:
            find_contact(DEFAULT_DATABASE_NAME)
        elif action_number == 3:
            edit_contact(DEFAULT_DATABASE_NAME)
        elif action_number == 4:
            delete_contact(DEFAULT_DATABASE_NAME)
        elif action_number == 5:
            list_contact(DEFAULT_DATABASE_NAME)
        else:
            print("Exiting program.")
            break