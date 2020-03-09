from unittest import TestCase
from A01162209_1510_assignments.A3.navigation import move_character


class TestMove_character(TestCase):
    def test_move_character_West(self):
        character = {"Position": [3, 3]}
        move_choice = 1
        move_character(character, move_choice)
        expected_output = {"Position": [2, 3]}
        self.assertEqual(expected_output, character)

    def test_move_character_left(self):
        character = {"Position": [3, 3]}
        move_choice = 2
        move_character(character, move_choice)
        expected_output = {"Position": [4, 3]}
        self.assertEqual(expected_output, character)

    def test_move_character_north(self):
        character = {"Position": [3, 3]}
        move_choice = 3
        move_character(character, move_choice)
        expected_output = {"Position": [3, 2]}
        self.assertEqual(expected_output, character)

    def test_move_character_south(self):
        character = {"Position": [3, 3]}
        move_choice = 4
        move_character(character, move_choice)
        expected_output = {"Position": [3, 4]}
        self.assertEqual(expected_output, character)