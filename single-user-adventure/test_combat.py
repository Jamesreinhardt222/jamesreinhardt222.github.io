from unittest import TestCase
import unittest.mock
from unittest.mock import patch
import io
from A01162209_1510_assignments.A3.combat import combat


class TestCombat(TestCase):
    @patch('A01162209_1510_assignments.A3.combat.combat_round', return_value="over")
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_combat(self, mock_stdout, mock_combat_round):
        opponent = {"Character name": "Mosquito", "Health": 5}
        player = {"Character name": "James", "Health": [10, 10]}
        combat(player, opponent)
        self.assertEqual(mock_stdout.getvalue(), "Your health: 10\nEnemy health: 5\n")

