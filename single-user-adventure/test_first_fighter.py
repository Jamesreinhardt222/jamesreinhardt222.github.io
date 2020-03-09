from unittest import TestCase
from A01162209_1510_assignments.A3.combat import first_fighter
import unittest.mock
from unittest.mock import patch
import io


class TestFirst_fighter(TestCase):

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', side_effect=[20, 19])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_first_fighter_player_first_printed_output(self, mock_stdout, mock_roll_die, mock_input):
        first_fighter()
        self.assertEqual(mock_stdout.getvalue(), "Player rolled 20\nEnemy rolled 19\n"
                                                 "Player goes first!!!\n")
    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', side_effect=[17, 19])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_first_fighter_enemy_first_printed_output(self, mock_stdout, mock_roll_die, mock_input):
        first_fighter()
        self.assertEqual(mock_stdout.getvalue(), "Player rolled 17\nEnemy rolled 19\n"
                                                 "Enemy goes first!!\n")

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', side_effect=[20, 20])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_first_fighter_tie_printed_output(self, mock_stdout, mock_roll_die, mock_input):
        first_fighter()
        self.assertEqual(mock_stdout.getvalue(), "Player rolled 20\nEnemy rolled 20\n"
                                                 "Tie! Roll again!\n")

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', side_effect=[20, 19])
    def test_first_fighter_player_first_return_value(self, mock_roll_die, mock_input):
        actual_output = first_fighter()
        expected = "player first attack"
        self.assertEqual(expected, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', side_effect=[18, 19])
    def test_first_fighter_enemy_first_return_value(self, mock_roll_die, mock_input):
        actual_output = first_fighter()
        expected = "enemy first attack"
        self.assertEqual(expected, actual_output)