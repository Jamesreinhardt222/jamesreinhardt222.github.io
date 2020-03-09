import unittest.mock
from unittest import TestCase
from A01162209_1510_assignments.A3.navigation import get_user_choice
from unittest.mock import patch
import io


class TestGet_user_choice(TestCase):

    @patch('builtins.input', return_value="Quit")
    def test_get_user_choice_quit_option_title(self, mock_input):
        self.assertEqual("quit", get_user_choice())

    @patch('builtins.input', return_value="QUIT")
    def test_get_user_choice_quit_option_caps_lock(self, mock_input):
        self.assertEqual("quit", get_user_choice())

    @patch('builtins.input', return_value="quit")
    def test_get_user_choice_quit_lower(self, mock_input):
        self.assertEqual("quit", get_user_choice())

    @patch('builtins.input', return_value="1")
    def test_get_user_choice_Left(self, mock_input):
        self.assertEqual(1, get_user_choice())

    @patch('builtins.input', return_value='2')
    def test_get_user_choice_right(self, mock_input):
        self.assertEqual(2, get_user_choice())

    @patch('builtins.input', return_value='3')
    def test_get_user_choice_up(self, mock_input):
        self.assertEqual(3, get_user_choice())

    @patch('builtins.input', return_value='4')
    def test_get_user_choice_down(self, mock_input):
        self.assertEqual(4, get_user_choice())

    @patch('builtins.input', side_effect=['5', '1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_number_too_big(self, mock_stdout, mock_input):
        get_user_choice()
        self.assertEqual(mock_stdout.getvalue(), "Not a valid move\n")

    @patch('builtins.input', side_effect=['-2,', '1'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_number_too_small(self, mock_stdout, mock_input):
        get_user_choice()
        self.assertEqual(mock_stdout.getvalue(), "Not a valid move\n")

    @patch('builtins.input', side_effect=["Just", "1"])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_choice_string_variable(self, mock_stdout, mock_input):
        get_user_choice()
        self.assertEqual(mock_stdout.getvalue(), "Not a valid move\n")