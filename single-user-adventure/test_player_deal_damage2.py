from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.combat import player_deal_damage2


class TestPlayer_deal_damage2(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_deal_damage2_but_not_kill_printed_output(self, mock_stdout, mock_input, mock_choice):
        demon = {"Health": 5}
        player_deal_damage2(demon, "Demon")
        self.assertEqual(mock_stdout.getvalue(), "The Demon lost 3 HP!!\n")

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=6)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_player_deal_damage_and_kill_enemy_printed_output(self, mock_stdout, mock_input, mock_choice):
        demon = {"Health": 5}
        player_deal_damage2(demon, "Demon")
        self.assertEqual(mock_stdout.getvalue(), "You kill the Demon.\n")

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=3)
    def test_player_deal_damage2_but_not_kill_return_value(self, mock_input, mock_choice):
        expected_output = 1
        demon = {"Health": 5}
        actual_output = player_deal_damage2(demon, "Demon")
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=6)
    def test_player_deal_damage2_and_kill_enemy_return_value(self, mock_input, mock_choice):
        expected_output = "over"
        demon = {"Health": 5}
        actual_output = player_deal_damage2(demon, "Demon")
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=3)
    def test_if_player_deal_damage2_alter_enemy_stats(self, mock_input, mock_choice):
        enemy = {"Health": 5}
        player_deal_damage2(enemy, "Demon")
        expected_new_enemy_health_value = 2
        self.assertEqual(expected_new_enemy_health_value, enemy["Health"])
