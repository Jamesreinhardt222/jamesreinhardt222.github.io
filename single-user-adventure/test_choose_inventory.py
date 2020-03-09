from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.create_character import choose_inventory


class TestChoose_inventory(TestCase):

    @patch('builtins.input', side_effect=[1, 12, 4, -2])
    def test_choose_inventory_expected_varied_selection(self, mock_input):
        self.assertEqual(["Amulet", 'The first four seasons of Breaking Bad.', "Avocado"], choose_inventory())

    @patch('builtins.input', side_effect=[-40])
    def test_choose_inventory_only_negative(self, mock_input):
        self.assertEqual([], choose_inventory())

    @patch('builtins.input', side_effect=[1, 1, 1, 1, -3])
    def test_choose_inventory_all_the_same_selection(self, mock_input):
        self.assertEqual(["Amulet", "Amulet", "Amulet", "Amulet"], choose_inventory())

    @patch('builtins.input', side_effect=[1, 0, 1, -3])
    def test_choose_inventory_zero_in_selection(self, mock_input):
        self.assertEqual(["Amulet", "Amulet"], choose_inventory())

    @patch('builtins.input', side_effect=[1, 123, 1, -3])
    def test_choose_inventory_too_large_number_in_selection(self, mock_input):
        self.assertEqual(["Amulet", "Amulet"], choose_inventory())
