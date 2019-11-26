from django.test import TestCase
from app.calc import add

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Tested add this numbers"""
        self.assertEqual(add(3, 8), 11)
