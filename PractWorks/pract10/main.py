import unittest
from person import Person
from script import fact

class FactTest(unittest.TestCase):
    def test_fact_positive_number(self):
        self.assertEqual(fact(5), 120)

class PersonTest(unittest.TestCase):
    def test_fact_positive_number(self):
        user = Person("sdasd", 12123)
        self.assertEqual(user.get_name(), "sdasd")
        self.assertEqual(user.get_age(), 12123)

if __name__ == '__main__':
    unittest.main()