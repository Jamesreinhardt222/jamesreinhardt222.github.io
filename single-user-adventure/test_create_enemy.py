from unittest import TestCase
from A01162209_1510_assignments.A3.combat import create_enemy


class TestCreate_enemy(TestCase):
    def test_create_enemy(self):
        self.assertEqual({"Character name": "Bat", "Health": 5}, create_enemy("Bat"))
