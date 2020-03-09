from unittest import TestCase
from unittest.mock import patch
from A01162209_1510_assignments.A3.combat import combat_round


class TestCombat_round(TestCase):
    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', side_effect=[3, 1, 1, 2])
    @patch('random.choice', return_value=True)
    def test_combat_round_battle_still_going_on(self, mock_input, mock_roll_die, mock_choice):
        player = {"Health": [10, 10]}
        enemy = {"Character name": "Wolf", "Health": 5}
        self.assertEqual(1, combat_round(player, enemy))

    @patch('builtins.input', return_value=1)
    @patch('A01162209_1510_assignments.A3.combat.roll_die', side_effect=[1,2,4,5,6])
    @patch('random.choice', return_value=True)
    def test_combat_round_battle_over(self, mock_input, mock_roll_die, mock_choice):
        player = {"Health": [10, 10]}
        enemy = {"Character name": "Wolf", "Health": 5}
        self.assertEqual("over", combat_round(player, enemy))

