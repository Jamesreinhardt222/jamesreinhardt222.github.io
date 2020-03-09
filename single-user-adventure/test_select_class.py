from unittest import TestCase
from unittest.mock import patch
from A01162209_1510_assignments.A3.create_character import select_class


class TestSelect_class(TestCase):

    @patch('builtins.input', return_value=1)
    def test_select_class_barbarian(self, mock_input):
        self.assertEqual("Barbarian", select_class())

    @patch('builtins.input', return_value=2)
    def test_select_class_bard(self, mock_input):
        self.assertEqual("Bard", select_class())

    @patch('builtins.input', return_value=3)
    def test_select_class_fighter(self, mock_input):
        self.assertEqual("Fighter", select_class())

    @patch('builtins.input', return_value=4)
    def test_select_class_cleric(self, mock_input):
        self.assertEqual("Cleric", select_class())

    @patch('builtins.input', return_value=5)
    def test_select_class_druid(self, mock_input):
        self.assertEqual("Druid", select_class())

    @patch('builtins.input', return_value=6)
    def test_select_class_rogue(self, mock_input):
        self.assertEqual("Rogue", select_class())

    @patch('builtins.input', return_value=7)
    def test_select_class_ranger(self, mock_input):
        self.assertEqual("Ranger", select_class())

    @patch('builtins.input', return_value=8)
    def test_select_class_monk(self, mock_input):
        self.assertEqual("Monk", select_class())

    @patch('builtins.input', return_value=9)
    def test_select_class_paladin(self, mock_input):
        self.assertEqual("Paladin", select_class())

    @patch('builtins.input', return_value=10)
    def test_select_class_sorcerer(self, mock_input):
        self.assertEqual("Sorcerer", select_class())

    @patch('builtins.input', return_value=11)
    def test_select_class_warlock(self, mock_input):
        self.assertEqual("Warlock", select_class())

    @patch('builtins.input', return_value=12)
    def test_select_class_wizard(self, mock_input):
        self.assertEqual("Wizard", select_class())

    @patch('builtins.input', return_value=13)
    def test_select_class_cst_student(self, mock_input):
        self.assertEqual("CST Student", select_class())
