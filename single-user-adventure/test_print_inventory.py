from unittest import TestCase
import unittest.mock
import io
from A01162209_1510_assignments.A3.create_character import print_inventory


class TestPrint_inventory(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_inventory(self, mock_stdout):
        print_inventory()
        self.assertEqual(mock_stdout.getvalue(), "You come across a travelling Merchant!\n"+
                                                 "Here is what he has for sale:\n1. Amulet\n" +
                                                 "2. Wooden Staff\n3. Spider Webs\n4. Avocado""\n5. Map of BCIT\n"+
                                                 "6. Silly Putty\n7. Dagger\n8. AK-47\n9. A bunch of drugs\n10. A "+
                                                 "Jonas Brothers poster\n11. Chocolate Milk\n"+
                                                 "12. The first four seasons of Breaking Bad.\n13. A magic pendant"
                                                 "\n14. Silver Chalice\n15. Dragon Scale Helmet\n16. Radiator Coolant" +
                                                 "\n17. A bottle of Tequila\n")

