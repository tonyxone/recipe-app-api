from django.test import SimpleTestCase

from . import calc

class CalcTests(SimpleTestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 11), 6)