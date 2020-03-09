from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.area_event import flee


class TestFlee(TestCase):
    @patch('builtins.input',return_value=2)
    @patch('A01162209_1510_assignments.A3.area_event.roll_die', side_effect=[1, 2])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_enemy_hits_you(self, mock_stdout, mock_input, mock_roll_die):
        player = {"Health": [10, 10]}
        enemy = "tarantuala"
        flee(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), "You decide to flee\nThe tarantuala strikes you as you flee.  You lost 2 HP!\n")


    @patch('builtins.input', return_value=2)
    @patch('A01162209_1510_assignments.A3.area_event.roll_die', return_value=2)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_enemy_does_not_hits_you(self, mock_stdout, mock_input, mock_roll_die):
        player = {"Health": [10, 10]}
        enemy = "tarantuala"
        flee(player, enemy)
        self.assertEqual(mock_stdout.getvalue(), "You decide to flee\nThe enemy tries to strike you, but you get away!\n")
