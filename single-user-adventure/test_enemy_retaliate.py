from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.combat import enemy_retaliate

class TestEnemy_retaliate(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_retaliate_and_hit_printed_output(self, mock_stdout, mock_input, mock_choice):
        enemy_retaliate("Ghost")
        self.assertEqual(mock_stdout.getvalue(), "But you are too slow! The Ghost hits you!!\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_retaliate_and_miss_printed_output(self, mock_stdout, mock_input, mock_choice):
        enemy_retaliate("Angel")
        self.assertEqual(mock_stdout.getvalue(),
                         "You roll out of the way!\n")

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=True)
    def test_enemy_retaliate_and_hit_return_value(self, mock_input, mock_choice):
        actual_output = enemy_retaliate("Gangster")
        expected = "enemy deal damage2"
        self.assertEqual(expected, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('random.choice', return_value=False)
    def test_enemy_retaliate_and_miss_return_value(self, mock_input, mock_choice):
        actual_output = enemy_retaliate("Bob")
        expected = 1
        self.assertEqual(expected, actual_output)
