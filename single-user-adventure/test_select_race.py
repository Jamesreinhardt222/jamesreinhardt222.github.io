from unittest import TestCase
from unittest.mock import patch
from A01162209_1510_assignments.A3.create_character import select_race


class TestSelect_race(TestCase):

    @patch('builtins.input', side_effect=[1])
    def test_select_race_dragonborn(self, mock_input):
        self.assertEqual("Dragonborn", select_race())

    @patch('builtins.input', side_effect=[2])
    def test_select_race_dwarf(self, mock_input):
        self.assertEqual("Dwarf", select_race())

    @patch('builtins.input', side_effect=[3])
    def test_select_race_elf(self, mock_input):
        self.assertEqual("Elf", select_race())

    @patch('builtins.input', side_effect=[4])
    def test_select_race_gnome(self, mock_input):
        self.assertEqual("Gnome", select_race())

    @patch('builtins.input', side_effect=[5])
    def test_select_race_halfelf(self, mock_input):
        self.assertEqual("Half-Elf", select_race())

    @patch('builtins.input', side_effect=[6])
    def test_select_race_halfling(self, mock_input):
        self.assertEqual("Halfling", select_race())

    @patch('builtins.input', side_effect=[7])
    def test_select_race_halforc(self, mock_input):
        self.assertEqual("Half-Orc", select_race())

    @patch('builtins.input', side_effect=[8])
    def test_select_race_human(self, mock_input):
        self.assertEqual("Human", select_race())

    @patch('builtins.input', side_effect=[9])
    def test_select_race_Aarakocra(self, mock_input):
        self.assertEqual("Aarakocra", select_race())

    @patch('builtins.input', side_effect=[10])
    def test_select_race_Genasi(self, mock_input):
        self.assertEqual("Genasi", select_race())

    @patch('builtins.input', side_effect=[11])
    def test_select_race_Aasimar(self, mock_input):
        self.assertEqual("Aasimar", select_race())

    @patch('builtins.input', side_effect=[12])
    def test_select_race_Ratling(self, mock_input):
        self.assertEqual("Ratling", select_race())


    @patch('builtins.input', side_effect=[13])
    def test_select_race_Firbolg(self, mock_input):
        self.assertEqual("Firbolg", select_race())

    @patch('builtins.input', side_effect=[14])
    def test_select_race_Hobgoblin(self, mock_input):
        self.assertEqual("Hobgoblin", select_race())

    @patch('builtins.input', side_effect=[15])
    def test_select_race_Kobold(self, mock_input):
        self.assertEqual("Kobold", select_race())

    @patch('builtins.input', side_effect=[16])
    def test_select_race_lizardfolk(self, mock_input):
        self.assertEqual("Lizardfolk", select_race())

    @patch('builtins.input', side_effect=[17])
    def test_select_race_tiefling(self, mock_input):
        self.assertEqual("Tiefling", select_race())


    @patch('builtins.input', side_effect=[18])
    def test_select_race_Goliath(self, mock_input):
        self.assertEqual("Goliath", select_race())

    @patch('builtins.input', side_effect=[19])
    def test_select_race_Goblin(self, mock_input):
        self.assertEqual("Goblin", select_race())



    @patch('builtins.input', side_effect=[20])
    def test_select_race_Kenku(self, mock_input):
        self.assertEqual("Kenku", select_race())


    @patch('builtins.input', side_effect=[21])
    def test_select_race_Orc(self, mock_input):
        self.assertEqual("Orc", select_race())


    @patch('builtins.input', side_effect=[22])
    def test_select_race_Tabxi(self, mock_input):
        self.assertEqual("Tabaxi", select_race())

    @patch('builtins.input', side_effect=[23])
    def test_select_race_Triton(self, mock_input):
        self.assertEqual("Triton", select_race())

    @patch('builtins.input', side_effect=[24])
    def test_select_race_Feral_Tiefling(self, mock_input):
        self.assertEqual("Feral Tiefling", select_race())


    @patch('builtins.input', side_effect=[25])
    def test_select_race_Tortle(self, mock_input):
        self.assertEqual("Tortle", select_race())

    @patch('builtins.input', side_effect=[26])
    def test_select_race_Gith(self, mock_input):
        self.assertEqual("Gith", select_race())

    @patch('builtins.input', side_effect=[27])
    def test_select_race_changeling(self, mock_input):
        self.assertEqual("Changeling", select_race())

    @patch('builtins.input', side_effect=[29])
    def test_select_race_Kalashtar(self, mock_input):
        self.assertEqual("Kalashtar", select_race())

    @patch('builtins.input', side_effect=[30])
    def test_select_race_shifter(self, mock_input):
        self.assertEqual("Shifter", select_race())


    @patch('builtins.input', side_effect=[31])
    def test_select_race_Warforged(self, mock_input):
        self.assertEqual("Warforged", select_race())

    @patch('builtins.input', side_effect=[32])
    def test_select_race_centaur(self, mock_input):
        self.assertEqual("Centaur", select_race())

    @patch('builtins.input', side_effect=[33])
    def test_select_race_loxadon(self, mock_input):
        self.assertEqual("Loxodon", select_race())

    @patch('builtins.input', side_effect=[34])
    def test_select_race_minotaur(self, mock_input):
        self.assertEqual("Minotaur", select_race())

    @patch('builtins.input', side_effect=[35])
    def test_select_race_Simic_Hybrid(self, mock_input):
        self.assertEqual("Simic Hybrid", select_race())

    @patch('builtins.input', side_effect=[36])
    def test_select_race_Vedelken(self, mock_input):
        self.assertEqual("Vedelken", select_race())


    @patch('builtins.input', side_effect=[37])
    def test_select_race_Locathah(self, mock_input):
        self.assertEqual("Locathah", select_race())

    @patch('builtins.input', side_effect=[38])
    def test_select_race_Verdan(self, mock_input):
        self.assertEqual("Verdan", select_race())

