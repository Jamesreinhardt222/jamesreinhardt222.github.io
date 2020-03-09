from unittest import TestCase
from A01162209_1510_assignments.A3.navigation import check_if_exit_reached


class TestCheck_if_exit_reached(TestCase):
    def test_check_if_exit_reached_successful(self):
        exit_coordinates = {"End": [5, 5]}
        your_coordinates = {"Position": [5, 5]}
        self.assertTrue(check_if_exit_reached(exit_coordinates, your_coordinates))

    def test_check_if_exit__reached_not_reached(self):
        exit_coordinates = {"End": [5, 5]}
        your_coordinates = {"Position": [3, 2]}
        self.assertFalse(check_if_exit_reached(exit_coordinates, your_coordinates))
