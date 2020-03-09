from unittest import TestCase
from A01162209_1510_assignments.A3.navigation import room_enemy_details


class TestRoom_enemy_details(TestCase):
    def test_room_enemy_details(self):
        self.assertEqual({(0, 0): 'Robo Nazi',
 (0, 1): 'Apple Sauce Monster',
 (0, 2): 'Drug Dealer',
 (0, 3): 'Frost Giant',
 (0, 4): 'Giant wasp',
 (1, 0): 'Orc',
 (1, 1): 'Bat monster',
 (1, 2): 'Mind Flayer',
 (1, 3): 'Shadow Dragon',
 (1, 4): 'Psycho Clown',
 (2, 0): 'Tiger',
 (2, 1): 'Zombie',
 (2, 2): 'Beholder',
 (2, 3): 'Giant Snake',
 (2, 4): 'Marshmello Monster',
 (3, 0): 'Bear',
 (3, 1): 'Panda',
 (3, 2): 'Dark Elf',
 (3, 3): 'Werewolf',
 (3, 4): 'Vampire',
 (4, 0): 'Dragon',
 (4, 1): 'Fire demon',
 (4, 2): 'Troll',
 (4, 3): 'Mini Hitler',
 (4, 4): 'Super Hitler'}, room_enemy_details())
