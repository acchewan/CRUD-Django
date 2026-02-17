from django.test import TestCase
from .utils import add_numbers


class AddTestCase(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
