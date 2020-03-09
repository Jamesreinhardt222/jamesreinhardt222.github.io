from unittest import TestCase
from A01162209_1510_assignments.A3.navigation import make_board_details

class TestMake_board_details(TestCase):
    def test_make_board_details(self):
        self.assertEqual({(0, 0): 'You start out on a barren field beside your home town.  You remember '
         'playing with your friends here as a child before the dark forces '
         'took over.  Your fellow villagers live in fear and poverty, and you '
         'decide you must do something about it.  You grab your weapon and set '
         'out to end the tyrrany of Mecha-Hitler once and for all.',
 (0, 1): 'You come across an open plain, and in the distance you see some '
         'buildings. It looks like a city',
 (0, 2): 'You are in the center of a volcano surrounded by benevolent gnomes.  '
         'You offered to help them rebuild their library that burned down in a '
         "tragic fire.  You tell them that maybe they shouldn't be building in "
         'the center of a live volcanoe, there are better places to build.  '
         'But they say the current real-estate market is so bad, this was the '
         'only place they could afford.',
 (0, 3): 'You are in the mirror dimension, which is filled with mirrors.  You '
         'have no idea how to get out of it, but you figure you might as well '
         'try.',
 (0, 4): 'You made it!  Just kidding, you still have a ways to go.  This is '
         'just a random mountain.  You went to the wrong mountain, silly.  '
         'Evil Mountain is to the east.',
 (1, 0): 'You travel just outside of your small village and pass the '
         'graveyard, where so many of your friends and family rest.  You '
         'quietly pay your respects to them before moving on.',
 (1, 1): 'You come up to the border of JamesTown, a bustling megacity filled '
         'with the latest culture. It is one of the few places where people '
         'still have joy in this realm.You decide to hit up the local '
         'nightlife and get wasted.',
 (1, 2): 'Now you are in a scary dark field with skeletons everywhere.  Crows '
         'circle overhead omminously',
 (1, 3): 'You find yourself inside a massive spiderweb.  This is a sticky '
         'situation',
 (1, 4): 'You are in the candy realm, where everything is made of candy.  You '
         'need to eat your way out of here without getting diabetes.',
 (2, 0): 'You enter a secluded forests. Light breaks through the canopy '
         'overhead and makes the forest appear alive and sparkling.  You stop '
         'at a stream for some water.',
 (2, 1): 'RYou find yourself in outerspace.  You must have taken a wrong turn '
         'somewhere.',
 (2, 2): 'You are in the bustling town of wiggleville, you decide to buy a '
         "horse so you don't have to walk around so much",
 (2, 3): 'You are in the sewers of James Land.  Mario lives down here '
         'apparently.  Anyways, you need to get out of here before you stink '
         'up your clothes.',
 (2, 4): 'You are totally lost now.  I have no idea where this is.  If you '
         "didn't cheap out and bought a cell-phone plan with data you could "
         'just use google maps instead of always asking me to tell you where '
         'you are.',
 (3, 0): 'You enter into the desert.  The scorching heat weighs down on you as '
         'you trek through the endless sand dunes.',
 (3, 1): "You're on top of an interdimensional rainbow riding a unicorn made "
         'of lightning.',
 (3, 2): 'You trip over a rock and hit your head on the ground.  When you wake '
         'up you find yourself in a hospital surrounded by elves.  They tell '
         'you not to worry, james-land still has universal health care.  '
         "Mecha-hitler hasn't taken that away yet",
 (3, 3): 'You find yourself in the batcave.  Batman is there, and he '
         'congratulates you on your abs.  You knew all those sit-ups would pay '
         'off.',
 (3, 4): 'You are almost there, you see evil mountain yay!!  You just have to '
         'get across a massive field filed with mines.  No biggie.',
 (4, 0): 'You find a valley with some shelter from the elements. While '
         'beautiful, you find yourself lost in the jungle.You come across an '
         'ancient temple.  It is falling apart, but you decide to enter '
         'anyways, hoping you might find something useful. ',
 (4, 1): 'You end up in Surrey, yikes.',
 (4, 2): "You're in las vegas and it is awesome.  You might just stay here, "
         "because Mecha-hitler really isn't that big of a deal... and you lost "
         'all your money.  Better continue on with your quest.  You might need '
         "to use your mom's credit card to survive.",
 (4, 3): "You are in a creepy sex dungeon.  Normally you're into this kind of "
         "thing, but you don't have time to hang around.",
 (4, 4): 'You made it!!!'}, make_board_details())
