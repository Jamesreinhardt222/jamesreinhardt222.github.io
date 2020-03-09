from unittest import TestCase
from unittest.mock import patch
from A01162209_1510_assignments.A3.area_event import enemy_appear


class TestEnemy_appear(TestCase):
    @patch('A01162209_1510_assignments.A3.area_event.roll_die', return_value=1)
    def test_enemy_appear_enemy_does_show_up(self, mock_roll_die):
        self.assertTrue(enemy_appear())

    @patch('A01162209_1510_assignments.A3.area_event.roll_die', return_value=3)
    def test_enemy_appear_enemy_does_not_appear(self, mock_roll_die):
        self.assertFalse(enemy_appear())
