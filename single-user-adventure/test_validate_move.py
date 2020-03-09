from unittest import TestCase
from A01162209_1510_assignments.A3.navigation import validate_move


class TestValidate_move(TestCase):
    def test_validate_move_left_at_left_edge(self):
        player = {"Position": [0, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 1
        self.assertFalse(validate_move(dungeon, player, move))

    def test_validate_move_right_at_left_edge(self):
        player = {"Position": [0, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 2
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_up_at_left_edge(self):
        player = {"Position": [0, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 3
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_down_at_left_edge(self):
        player = {"Position": [0, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 4
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_right_at_right_edge(self):
        player = {"Position": [4, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 2
        self.assertFalse(validate_move(dungeon, player, move))

    def test_validate_move_left_at_right_edge(self):
        player = {"Position":[4, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 1
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_up_at_right_edge(self):
        player = {"Position": [4, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 3
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_down_at_right_edge(self):
        player = {"Position": [4, 3]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 4
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_up_at_top_edge(self):
        player = {"Position": [3, 0]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 3
        self.assertFalse(validate_move(dungeon, player, move))

    def test_validate_move_down_at_top_edge(self):
        player = {"Position": [3, 0]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 4
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_right_at_top_edge(self):
        player = {"Position": [3, 0]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 2
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_left_at_top_edge(self):
        player = {"Position": [3, 0]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 1
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_down_at_bottom_edge(self):
        player = {"Position": [3, 4]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 4
        self.assertFalse(validate_move(dungeon, player, move))

    def test_validate_move_up_at_bottom_edge(self):
        player = {"Position": [3, 4]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 3
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_left_at_bottom_edge(self):
        player = {"Position": [3, 4]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 1
        self.assertTrue(validate_move(dungeon, player, move))

    def test_validate_move_right_at_bottom_edge(self):
        player = {"Position": [3, 4]}
        dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
        move = 2
        self.assertTrue(validate_move(dungeon, player, move))

