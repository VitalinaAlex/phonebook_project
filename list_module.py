from utils import load_database, print_contacts

def list_contact(db_name):
    db = load_database(db_name)
    print_contacts(db)
    return db