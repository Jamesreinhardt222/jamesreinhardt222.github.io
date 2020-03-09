from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.combat import player_retaliate


class TestPlayer_retaliate(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_retaliate_and_hit_printed_output(self, mock_stdout, mock_input, mock_choice):
        player_retaliate("Blob")
        self.assertEqual(mock_stdout.getvalue(), "Your attack lands!\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_retaliate_and_miss_printed_output(self, mock_stdout, mock_input, mock_choice):
        player_retaliate("Blob")
        self.assertEqual(mock_stdout.getvalue(), "Your attack misses!!\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    def test_player_retaliate_and_hit_return_value(self, mock_input, mock_choice):
        actual_output = player_retaliate("Blob")
        expected = "player deal damage2"
        self.assertEqual(expected, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    def test_player_retaliate_and_miss_return_value(self, mock_input, mock_choice):
        actual_output = player_retaliate("Blob")
        expected = 1
        self.assertEqual(expected, actual_output)
