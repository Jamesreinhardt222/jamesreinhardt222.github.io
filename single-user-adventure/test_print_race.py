from unittest import TestCase
import unittest.mock
import io
from A01162209_1510_assignments.A3.create_character import print_race

class TestPrint_race(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_race(self, mock_stdout):
        print_race()
        self.assertEqual(mock_stdout.getvalue(), ("1. Dragonborn\n2. Dwarf\n3. Elf\n" +
                                                  "4. Gnome\n5. Half-Elf\n6. Halfling\n" +
                                                  "7. Half-Orc\n8. Human\n9. Aarakocra\n10. Genasi\n" +
                                                  "11. Aasimar\n12. Ratling\n13. Firbolg\n14. Hobgoblin\n" +
                                                  "15. Kobold\n16. Lizardfolk\n17. Tiefling\n18. Goliath\n19. Goblin\n"+
                                                  "20. Kenku\n21. Orc\n22. Tabaxi\n23. Triton\n24. Feral "
                                                  "Tiefling\n25. Tortle\n"+
                                                  "26. Gith\n27. Changeling\n29. Kalashtar\n30. Shifter\n31. "
                                                  "Warforged\n32. Centaur\n"+
                                                  "33. Loxodon\n34. Minotaur\n35. Simic Hybrid\n36. Vedelken\n37. "
                                                  "Locathah\n38. Verdan\n"))