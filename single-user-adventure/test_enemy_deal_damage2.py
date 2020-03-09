from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.combat import enemy_deal_damage2


class TestEnemy_deal_damage2(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=3)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_deal_damage2_but_not_kill_printed_output(self, mock_stdout, mock_input, mock_choice):
        player = {"Health": [10, 5]}
        enemy_deal_damage2(player, "Demon")
        self.assertEqual(mock_stdout.getvalue(), "You lost 3 HP!!\nYou stumble back, dazed.\n")

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=6)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_deal_damage2_and_kill_player_printed_output(self, mock_stdout, mock_input, mock_choice):
        demon = {"Health": [10, 5]}
        enemy_deal_damage2(demon, "Demon")
        self.assertEqual(mock_stdout.getvalue(), "The Demon kills you.\n")

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=3)
    def test_enemy_deal_damage2_but_not_kill_return_value(self, mock_input, mock_choice):
        expected_output = 1
        demon = {"Health": [10, 5]}
        actual_output = enemy_deal_damage2(demon, "Demon")
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=6)
    def test_enemy_deal_damage2_and_kill_enemy_return_value(self, mock_input, mock_choice):
        expected_output = "over"
        demon = {"Health": [5, 5]}
        actual_output = enemy_deal_damage2(demon, "Demon")
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', return_value=3)
    def test_if_enemy_deal_damage_alter_enemy_stats(self, mock_input, mock_choice):
        player = {"Health": [10, 10]}
        enemy_deal_damage2(player, "James")
        expected_new_player_health_value = 7
        self.assertEqual(expected_new_player_health_value, player["Health"][1])