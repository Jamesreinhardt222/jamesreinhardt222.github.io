from unittest import TestCase
from A01162209_1510_assignments.A3.create_character import roll_die


class Test_roll_die(TestCase):

    def test_roll_die_upper_bound(self):
        value = roll_die(3,6)
        self.assertTrue(value <= 18)

    def test_roll_die_lowerbound(self):
        value = roll_die(3,6)
        self.assertTrue(value >= 3)

    def test_roll_die_zero(self):
        self.assertEqual(0, roll_die(0, 0))

    def test_roll_die_negative(self):
        self.assertEqual(0, roll_die(-3, -2))
