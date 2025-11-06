"""Task 2
Write tests for the Phonebook application, which you have implemented in module 1. 
Design tests for this solution and write tests using unittest library"""

import unittest
from unittest.mock import patch, MagicMock
from add_module import add_contact
import delete_module,edit_module,find_module,list_module

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

        #Перевіряємо, що save_database викликалася
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

        #Перевіряємо доданий контакт НЕ додано
        self.assertEqual(mock_load_db.return_value["contacts"], result)

if __name__ == "__main__":
    unittest.main()