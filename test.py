"""Task 2
Write tests for the Phonebook application, which you have implemented in module 1. 
Design tests for this solution and write tests using unittest library"""

import unittest
from unittest.mock import patch, MagicMock
from add_module import add_contact
from delete_module import delete_contact
from utils import normalize_number
import edit_module,find_module,list_module

class TestPhoneBook(unittest.TestCase):
    #використовуємо моки функцій, що не будемо перевіряти
    @patch("add_module.save_database")
    @patch("add_module.load_database")
    @patch("builtins.input", side_effect=["1234567890", "Alice", "Kyiv"])
    def test_add_success(self, mock_input, mock_load_db, mock_save_db):
        # МОК бази
        mock_load_db.return_value = {"contacts": []}

        #Виклик функції
        result = add_contact("test_db.json")

        #Перевірка результату функції
        self.assertEqual(result, {"number": 1234567890, "name": "Alice", "city": "Kyiv"})

        #save_database викликалася
        mock_save_db.assert_called_once()

        #Перевіряємо доданий контакт
        self.assertEqual(mock_load_db.return_value["contacts"][0], result)
    
    @patch("add_module.save_database")
    @patch("add_module.load_database")
    @patch("builtins.input", side_effect=["12345678"])
    def test_add_fail(self, mock_input, mock_load_db, mock_save_db):
        # МОК бази
        mock_load_db.return_value = {"contacts": []}

        #Виклик функції
        result = add_contact("test_db.json")

        #Перевірка результату функції
        self.assertEqual(result, "ONLY digits for number. Max number of digits - 12, min - 10")

        #Перевіряємо контакт НЕ додано
        self.assertEqual(mock_load_db.return_value["contacts"], [])

    @patch("delete_module.save_database")
    @patch("delete_module.load_database")
    @patch("delete_module.print_contacts")
    @patch("delete_module.normalize_number", side_effect=lambda x: str(x).strip())
    @patch("builtins.input", side_effect=["1234567890"])
    def test_del_success(self, mock_input, mock_norm, mock_print, mock_load_db, mock_save_db):

        # МОК бази
        mock_load_db.return_value = {
        "contacts": [{"number": "1234567890", "name": "Alice", "city": "Kyiv"}]
        }

        #Виклик функції
        result = delete_contact("test_db.json")

        #Перевіряємо контакт видалено
        self.assertTrue(mock_save_db.called)
        args, kwargs = mock_save_db.call_args
        saved_data = args[1]
        #Перевіряємо видалення
        self.assertEqual(saved_data["contacts"], [])
        #Перевіряємо функцію
        self.assertEqual(result, {"number": "1234567890", "name": "Alice", "city": "Kyiv"})
    @patch("delete_module.save_database")
    @patch("delete_module.print_contacts")
    @patch("delete_module.load_database")
    @patch("builtins.input", return_value="9999999999")
    def test_delete_contact_not_found(self, mock_input, mock_load, mock_print, mock_save):
        mock_load.return_value = {
            "contacts": [{"name": "Alice", "number": "1234567890"}]
        }

        result = delete_contact("test_db.json")

        self.assertIsNone(result)
        mock_save.assert_not_called()

    @patch("delete_module.save_database")
    @patch("delete_module.print_contacts")
    @patch("delete_module.load_database")
    @patch("builtins.input", return_value="1234567890")
    def test_delete_contact_empty_list(self, mock_input, mock_load, mock_print, mock_save):
        mock_load.return_value = {"contacts": []}

        result = delete_contact("test_db.json")

        self.assertIsNone(result)
        mock_save.assert_not_called()



    @patch("delete_module.save_database")
    @patch("delete_module.print_contacts")
    @patch("delete_module.load_database")
    @patch("builtins.input", return_value="1234567890")
    def test_delete_contact_no_contacts_key(self, mock_input, mock_load, mock_print, mock_save):
        mock_load.return_value = {}

        result = delete_contact("test_db.json")

        self.assertIsNone(result)
        mock_save.assert_not_called()


if __name__ == "__main__":
    unittest.main()