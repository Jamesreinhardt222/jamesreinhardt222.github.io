from unittest import TestCase
import unittest.mock
import io
from A01162209_1510_assignments.A3.create_character import print_class


class TestPrint_class(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class(self, mock_stdout):
        print_class()
        self.assertEqual(mock_stdout.getvalue(), "Pick a class from the following options:\n" + "1. Barbarian\n" +
                         "2. Bard\n" + "3. Fighter\n" + "4. Cleric\n" + "5. Druid\n6. Rogue\n" +
                         "7. Ranger\n8. Monk\n9. Paladin\n10. Sorcerer\n11. Warlock\n12. Wizard\n13. CST Student\n")

