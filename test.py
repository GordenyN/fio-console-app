import unittest

class TestFioFunctions(unittest.TestCase):
    def setUp(self):
        self.names = [
            "Иванов Иван Иванович",
            "Петров Петр Петрович",
            "Сидоров Сидор Сидорович"
        ]
    
    def test_search_names(self):
        self.assertEqual(search_names(self.names, "Иван"), ["Иванов Иван Иванович"])
        self.assertEqual(search_names(self.names, "Петр"), ["Петров Петр Петрович"])
        self.assertEqual(search_names(self.names, "Сид"), ["Сидоров Сидор Сидорович"])
        self.assertEqual(search_names(self.names, "НетТакого"), [])
    
    def test_add_name(self):
        new_names = add_name(self.names.copy(), "Александров Алексей Алексеевич")
        self.assertIn("Александров Алексей Алексеевич", new_names)
        self.assertEqual(sorted(new_names), new_names)  # Должно быть отсортировано
    
    def test_delete_name(self):
        new_names = self.names.copy()
        new_names.remove("Петров Петр Петрович")
        self.assertNotIn("Петров Петр Петрович", new_names)

# Запуск тестов в Jupyter Notebook
unittest.main(argv=[''], verbosity=2, exit=False)
