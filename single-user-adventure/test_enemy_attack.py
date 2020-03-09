from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.combat import enemy_attack


class TestEnemy_attack(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_and_hit_printed_output(self, mock_stdout, mock_input, mock_choice):
        enemy_attack("Ghost")
        self.assertEqual(mock_stdout.getvalue(), "But you are too slow! The Ghost hits you!!\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_and_miss_printed_output(self, mock_stdout, mock_input, mock_choice):
        enemy_attack("Bob")
        self.assertEqual(mock_stdout.getvalue(), "You do a triple back-flip out of the way, dodging the Bob's attack!\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    def test_enemy_attack_and_hit_return_value(self, mock_input, mock_choice):
        actual_output = enemy_attack("Bob")
        expected = "enemy deal damage"
        self.assertEqual(expected, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    def test_enemy_attack_and_miss_return_value(self, mock_input, mock_choice):
        actual_output = enemy_attack("Bob")
        expected = "player retaliates"
        self.assertEqual(expected, actual_output)
