from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.combat import player_attack


class TestPlayer_attack(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_attack_and_hit_printed_output(self, mock_stdout, mock_input, mock_choice):
        player_attack("Blob")
        self.assertEqual(mock_stdout.getvalue(), "Your attack lands!\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_attack_and_miss_printed_output(self, mock_stdout, mock_input, mock_choice):
        player_attack("Blob")
        self.assertEqual(mock_stdout.getvalue(), "Your attack misses and you fall forward!! The Blob prepares to "
                                                 "retaliate.\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    def test_player_attack_and_hit_return_value(self, mock_input, mock_choice):
        actual_output = player_attack("Blob")
        expected = "player deal damage"
        self.assertEqual(expected, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    def test_player_attack_and_miss_return_value(self, mock_input, mock_choice):
        actual_output = player_attack("Blob")
        expected = "enemy retaliates"
        self.assertEqual(expected, actual_output)