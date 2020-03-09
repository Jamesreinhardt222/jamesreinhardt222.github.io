# Define the boundaries and end point of the game.


def establish_board_boundaries():
    """
    Makes boundaries of a square dungeon

    describes the top and bottom limits for a character's y-coordinates
    and the left and right limits for a character's x coordinates,
    and the desitination coordinates the character needs to reach to end the game.
    :postcondition:  a dictionary with the top, bottom, right, and left limits,
    and the coordinates of the end location.
    :return: a dictionary
    """
    dungeon = {"Top": 0, "Bottom": 4, "Left": 0, "Right": 4, "End": [4, 4]}
    return dungeon


# Make unique details for the various locations in the game.
def make_board_details():
    """
    Describe the details of the coordinates in the dungeon.

    Can be used to access details about the room the player is in and make an interactive story.
    For now it just says the room number.
    :postcondition: Will return a dictionary with the coordinates in
    tuple form as keys and their corresponding room details.
    :return:  a dictionary
    """
    details = {(0, 0): "You start out on a barren field beside your home town.  You remember playing with your "
                       "friends here as a child before the dark forces took over.  Your fellow villagers live in fear "
                       "and poverty, and you decide you must do something about it.  You grab your weapon and set out "
                       "to end the tyrrany of Mecha-Hitler once and for all.",
               (1, 0): "You travel just outside of your small village and pass the graveyard, where so many of your "
                       "friends and family rest.  You quietly pay your respects to them before moving on.",
               (2, 0): "You enter a secluded forests. Light breaks through the canopy overhead and makes the forest appear alive and sparkling.  You stop at a stream for some water.",
               (3, 0): "You enter into the desert.  The scorching heat weighs down on you as you trek through the endless sand dunes.", (4, 0): "You find a valley with some shelter from the elements. While beautiful, you find yourself lost in the jungle."
                "You come across an ancient temple.  It is falling apart, but you decide to enter anyways, hoping you might find something useful. ",
               (0, 1): "You come across an open plain, and in the distance you see some buildings. It looks like a city", (1, 1): "You come up to the border of JamesTown, a bustling megacity filled with the latest culture. It is one of the few places where people still have joy in this realm."
                "You decide to hit up the local nightlife and get wasted.", (2, 1): "RYou find yourself in outerspace.  You must have taken a wrong turn somewhere.", (3, 1): "You're on top of an interdimensional rainbow riding a unicorn made of lightning.", (4, 1): "You end up in Surrey, yikes.",
               (0, 2): "You are in the center of a volcano surrounded by benevolent gnomes.  You offered to help them "
                       "rebuild their library that burned down in a tragic fire.  You tell them that maybe they "
                       "shouldn't be building in the center of a live volcanoe, there are better places to build.  "
                       "But they say the current real-estate market is so bad, this was the only place they could "
                       "afford.", (1, 2): "Now you are in a scary dark field with skeletons everywhere.  Crows circle overhead omminously", (2, 2): "You are in the bustling town of wiggleville, you decide to buy a horse so you don't have to walk around so much",
               (3, 2): "You trip over a rock and hit your head on the ground.  When you wake up you find yourself in a hospital surrounded by elves.  They tell you not to worry, james-land still has universal health care.  Mecha-hitler hasn't taken that away yet",
             (4, 2): "You're in las vegas and it is awesome.  You might just stay here, because Mecha-hitler really "
                     "isn't that big of a deal... and you lost all your money.  Better continue on with your quest.  "
                     "You might need to use your mom's credit card to survive.",
               (0, 3): "You are in the mirror dimension, which is filled with mirrors.  You have no idea how to get out of it, but you figure you might as well try.", (1, 3): "You find yourself inside a massive spiderweb.  This is a sticky situation",
               (2, 3): "You are in the sewers of James Land.  Mario lives down here apparently.  Anyways, you need to get out of here before you stink up your clothes.", (3, 3): "You find yourself in the batcave.  Batman is there, and he congratulates you on your abs.  You knew all those sit-ups would pay off.",
               (4, 3): "You are in a creepy sex dungeon.  Normally you're into this kind of thing, but you don't have time to hang around.",
               (0, 4): "You made it!  Just kidding, you still have a ways to go.  This is just a random mountain.  You went to the wrong mountain, silly.  Evil Mountain is to the east.", (1, 4): "You are in the candy realm, where everything is made of candy.  You need to eat your way out of here without getting diabetes.",
               (2, 4): "You are totally lost now.  I have no idea where this is.  If you didn't cheap out and bought a cell-phone plan with data you could just use google maps instead of always asking me to tell you where you are.",
               (3, 4): "You are almost there, you see evil mountain yay!!  You just have to get across a massive field filed with mines.  No biggie.", (4, 4): "You made it!!!"}

    return details


def room_enemy_details():
    """
    Describe the details of the coordinates in the dungeon.

    Can be used to access details about the room the player is in and make an interactive story.
    For now it just says the room number.
    :postcondition: Will return a dictionary with the coordinates in
    tuple form as keys and their corresponding room details.
    :return:  a dictionary
    """
    details = {(0, 0): "Robo Nazi", (1, 0): "Orc", (2, 0): "Tiger", (3, 0): "Bear", (4, 0): "Dragon",
               (0, 1): "Apple Sauce Monster", (1, 1): "Bat monster", (2, 1): "Zombie", (3, 1): "Panda", (4, 1): "Fire demon",
               (0, 2): "Drug Dealer", (1, 2): "Mind Flayer", (2, 2): "Beholder", (3, 2): "Dark Elf", (4, 2): "Troll",
               (0, 3): "Frost Giant", (1, 3): "Shadow Dragon", (2, 3): "Giant Snake", (3, 3): "Werewolf", (4, 3): "Mini Hitler",
               (0, 4): "Giant wasp", (1, 4): "Psycho Clown", (2, 4): "Marshmello Monster", (3, 4): "Vampire", (4, 4): "Super Hitler"}

    return details

def enemy_action():
    actions = {"Robo Nazi": "You see a robo nazi marching down the street.",
                "Orc": "An orc appears and tries to grab you with his brutish hands.",
                "Tiger": "You turn around and see a tiger about to pounce. How did it get here?",
                 "Bear": "A bear charges out of nowhere towards you.", "Dragon": "A majestic dragon flies down from the sky, spewing flames from ts mouth.  It is coming rght towards you.",
               "Apple Sauce Monster": "An apple sauce monster appears and tries to eat you.",
                "Bat monster": "A bat monster swoops from the ceiling with it's claws flayed as it tries to snatch you up.",
               "Zombie": "A casket on the side of the room suddenly opens and a zombie crawls out.",
               "Panda": "You see a panda in the corner minding its own business.",
              "Fire demon": "There is an evil cackling and suddenly the walls are engulfed in flames.  A ball of fire spits to the center of the floor and "
                "begins to take shape, forming a terrifying demon that flies towards you.",
               "Drug Dealer": "A guy standing in the corner tries to sell you some weed.",
               "Mind Flayer":  "Suddenly everything goes dark, and you feel an ominous, horrifying presence. You look up and see"
                "the mind flayer, a terrible monster.", "Beholder": "You feel the ground shake and witness a beholder approaching.",
               "Dark Elf": "A creepy dark elf enters the room and starts calling you names." , "Troll": "A troll charges at you",
               "Frost Giant": "A massive frost giant appears and looks at you hungrily.", "Shadow Dragon": "You stumble upon a shadow Dargon.",
               "Giant Snake":"A giant snake appears.", "Werewolf":"A werewolf jumps out at you.",
               "Mini Hitler": "As you open the door, you find yourself face-to-face with none other than Mini-Hitler.",
               "Giant wasp": "You see a big wasp nest so you throw a rock at t, and a massive wasp comes out.",
               "Psycho Clown": "You see a psycho clown approaching.", "Marshmello Monster": "A marshmellow monster appears", "Trump":  "The president of the United states appears.",
               "Vampire": "A vampire leaps out of the shadows."}
    return actions


# Choose which direction to move.
def get_user_choice():
    """
    Select which direction to move.

    :precondition: user input must be an integer.
    :postcondition: The integer the user inputs is the integer that gets returned.
    :return: an int.
    """
    # Create a loop to keep asking for input until the user selects a valid response.
    choice = False
    while not choice:
        move = (input("Which way would you like to travel? 1 for west,"
                         " 2 for east, 3 for north, 4 for south, "
                      "and type 'quit' to exit game."))
        # The choice can only be 1, 2, 3, or 4.
        if move not in (["1", "2", "3", "4", "Quit", "quit", "QUIT"]):
            print("Not a valid move")
        # If the choice is a valid response, break the loop.
        else:
            choice = True
    if move.lower() == "quit":
        return "quit"
    else:
        return int(move)


# Check to see if a movement choice is possible.
def validate_move(board: dict, player: dict, move: int):
    """Make sure a movement is possible.

    If the player is on the edge of the map, they are unable to move off of the edge of
    the map, and this function will monitor their movement choices to make sure the player
    cannot move outside of the specified area.
    The limits are defined by the establish_board_boundaries function.
    :param board: a dictionary.
    :param player: a dictionary.
    :param move: an int.
    :precondition board: a dictionary with values for the keys, Left, Right, Top, and Bottom.
    :precondition player: a dictionary with the key "Position" and a list with an x-coordinate and a y-coordinate for the value.
    :precondition move: an integer.
    :postcondition: a boolean describing if the movement is possible or not.
    :return: a boolean
    """
    # Create variables for the player's x and y coordinates.
    player_x_location = player["Position"][0]
    player_y_location = player["Position"][1]
    if player_y_location == board["Top"] and move == 3:
        print("It smells really bad this way, and Mecha Hitler's lair is the other way, so you decide not to go this "
              "way.")
        return False
    elif player_y_location == board["Bottom"] and move == 4:
        print("You see a bunch of Burnaby cst students that way and decide you don't have the emotional stamina to "
              "deal with them.  You need to choose another way.")
        return False
    elif player_x_location == board["Left"] and move == 1:
        print("Trump built a wall along the border here, and you could climb over it, but it's too much work.")
        return False
    elif player_x_location == board["Right"] and move == 2:
        print("There's open ocean that way.  It's spakling water stretches out as far as the eye can see.  You wish "
              "you could travel and see what lies beyond, but ferry tickets are so overpriced that you need to choose "
              "another way to go.  Sorry.")
        return False
    else:
        return True


# Alter the player's position.
def move_character(player: dict, move: int):
    """
    Change the player's position.

    Alter the character's position value based on a movement choice.
    :postcondition: the character's position value will be altered. Depending on the move,
    it will be either the x-coordinate or the y-coordinate that is changed, and it will either
    be decreased or decreased by one.
    :param player: a dictionary.
    :param move: an int.
    """
    if move == 1:
        player["Position"][0] -= 1
        print("You travel west.")
    elif move == 2:
        player["Position"][0] += 1
        print("You move east to a new location")
    elif move == 3:
        player["Position"][1] -= 1
        print("You navigate north and find yourself in a different area.")
    elif move == 4:
        player["Position"][1] += 1
        print("You leave the current area and travel south")
    else:
        print("Invalid move")


# Create a function for ending the game when the end is reached.
def check_if_exit_reached(boundaries: dict, player: dict):
    """
    Monitor if the end of the game is reached.

    :param boundaries: a dictionary with the key, "End" and a list of coordinates as the value.
    :param player: A dictionary with the key, "Position" and a list of coordinates as the value
    :postcondition: will return true if the player's position is equal to the coordinates of
    the game's finish location.
    :return: a boolean.
    """
    if player["Position"] == boundaries["End"]:
        print("You have reached the castle on evil mountain, now you must face the final boss.")
        return True
    else:
        return False


