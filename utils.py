import json
import sys
import os
sys.path.append(os.path.dirname(__file__))

def load_database(db_name):
    """Відкрити файл JSON або створити новий, якщо він відсутній."""
    if not os.path.exists(db_name):
        print(f"Database '{db_name}' not found. Creating new one...")
        return {"contacts": []}
    try:
        with open(db_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        print("File corrupted or empty. Creating new database...")
        return {"contacts": []}


def save_database(db_name, data):
    """Зберегти БД у JSON з відступами та підтримкою кирилиці."""
    with open(db_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def print_contacts(data):
    """Вивести всі контакти (для дебагу)."""
    print("Contacts in file:")
    for contact in data.get("contacts", []):
        print(contact)


def normalize_number(value):
    """Повертає номер як рядок (для уніфікації int/str)."""
    return str(value).strip()