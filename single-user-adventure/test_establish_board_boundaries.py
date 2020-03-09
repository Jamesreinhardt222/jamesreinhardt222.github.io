from unittest import TestCase
from A01162209_1510_assignments.A3.navigation import establish_board_boundaries


class TestEstablish_board_boundaries(TestCase):
    def test_establish_board_boundaries(self):
        self.assertEqual({"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}, establish_board_boundaries())