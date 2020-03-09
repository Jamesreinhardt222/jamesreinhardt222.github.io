from unittest import TestCase
from unittest.mock import patch
from A01162209_1510_assignments.A3.area_event import room_event


class TestRoom_event(TestCase):
    @patch('A01162209_1510_assignments.A3.area_event.enemy_appear', return_value=False)
    def test_room_event_increase_player_health(self, mock_enemy_appear):
        player={"Health": [2, 3]}
        room_event(player, "Darth Vader")
        expected_health = 5
        actual_health = player["Health"][1]
        self.assertEqual(actual_health, expected_health)
