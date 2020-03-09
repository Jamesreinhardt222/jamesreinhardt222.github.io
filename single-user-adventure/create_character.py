import random


# Create a roll ide function to andomly generate a number
def roll_die(number_of_rolls: int, number_of_sides: int):
    """
    Generate a random number.

    Multiplies the number of sides of a dice by the amount of rolls to get the maximum possible value.
    Randomly chooses a number greater than or equal to the number of rolls and less than or equal to the maximum value.

    :param number_of_rolls: an integer
    :param number_of_sides: an integer
    :return: a random number greater than or equal to the number of rolls and less than or
    equal to the number of sides multiplied by the number of rolls.

    >>> roll_die(1, 1)
    1
    >>> roll_die(0, 0)
    0


    """
    # Find the maximum number the dice can roll
    max_value = number_of_rolls * number_of_sides

    # randomly generate a number from a certain range
    roll_value = random.randint(number_of_rolls, max_value)

    # Specify a zero return value if any of the arguments are zero.
    if number_of_rolls < 0:
        roll_value = 0
    elif number_of_sides < 0:
        roll_value = 0
    return roll_value


# Display a list of inventory options
def print_inventory():
    """
   display a list of inventory options

   The function removes brackets, displays each mini list below the previous one,
   and separates the contents of the mini lists by a period and a space.
    :return: A vertical list of inventory items with their associated numbers.
    """
    # Present list
    selection = [[1, "Amulet"], [2, "Wooden Staff"], [3, "Spider Webs"],
                 [4, "Avocado"], [5, "Map of BCIT"], [6, "Silly Putty"], [7, "Dagger"], [8, "AK-47"],
                 [9, "A bunch of drugs"],
                 [10, "A Jonas Brothers poster"], [11, "Chocolate Milk"],
                 [12, "The first four seasons of Breaking Bad."],
                 [13, "A magic pendant"], [14, "Silver Chalice"], [15, "Dragon Scale Helmet"], [16, "Radiator Coolant"],
                 [17, "A bottle of Tequila"]]
    print("You come across a travelling Merchant!\n"
          "Here is what he has for sale:")

    for i in selection:
        print(*i, sep=". ")
    return selection


# Create a function to generate your character's inventory.
# Choose a specific number of items from a list and make a sorted copy.
def choose_inventory():
    """
    Select items from a list and add them to the character's own list of items.

    Ask for user input and if the input is the same as any of the numbers in the list,
    the corresponding list item is added to the character list.
    If the number is too large, the function prints a message telling the user their choice is out of range.
    If the number is negative, the

    :precondition: User input must be an integer.
    :return: A list of items
    """
    # Create list of items
    selection = print_inventory()
    choice = 0

    # Create an empty list to append the inventory items.
    inventory = []

    # Add items to the inventory in a loop that ends when a negative number is entered.
    while choice >= 0:
        choice = int(input("What would you like to buy? (Enter the number for your item. -1 to finish)"))

        # If a number is too large,print a helpful message to the user.
        if choice > len(selection):
            print("your number is too large")

        if choice == 0:
            print("No item for zero")

        # Append items the user selects to the list.
        for value in selection:
            if choice == (value[0]):
                item = value[1]
                inventory.append(item)

    return inventory


# Generate character name and attributes
def create_character():
    """
    Generate a character

    Asks for user input and matches it with characters from a list in the print character function.
    :return: A dictionary of all the character's stats.
    """
    name = input("What's your name?")
    race = select_race()
    class_stats = select_class()
    max_hp = 10
    current_hp = max_hp
    attack_damage = 6
    # Return all of the character attributes as a dictionary.
    character_stats = {"Character name": name, "Character Race": race, "Attack" : attack_damage, "Position": [0, 0],
                       "Character Class": class_stats, "Health": [max_hp, current_hp], "Inventory": []}
    return character_stats


# display a list of classes.
def print_class():
    """
    Display a list of classes

    The classes are lists of length three.  The first index is a number the player can select to choose that particular
    class.The second index is the name of the class.  Each class has a specified dice size they can use to determine
    their health. The third index is the number of dice rolls and the fourth is the number of sides on that dice.
    :return: The list of classes.
    """
    classes = [[1, "Barbarian"], [2, "Bard"],
             [3, "Fighter"],
             [4, "Cleric"],
             [5, "Druid"],
             [6, "Rogue"],
             [7, "Ranger"],
             [8, "Monk"],
             [9, "Paladin"],
             [10, "Sorcerer"],
             [11, "Warlock"],
             [12, "Wizard"],
             [13, "CST Student"]]

    # Loop through options and print them without brackets or spaces.
    print("Pick a class from the following options:")
    for choice in classes:
        print(*choice[:2], sep=". ")
    return classes


# Choose a class for your character.
def select_class():
    """
    Choose a class based on user input

    :param: user must enter an integer that corresponds to a number associated with a class in the
    list generated by print_class.
    :return: The chosen class's name as a string
    """
    # Display class options as a numbered list.
    options = print_class()

    # Ask for user input.
    choice = int(input("Select a number to choose a class"))

    # Match input with class number and return the corresponding class as the user selection.
    for value in options:
        if choice == value[0]:
            character_class = value[1]
    return character_class


# Display a list of races.
def print_race():
    """
    Display a list of races

    Each item in the list is a list of length two.  The second items in the minilists are the race names,
    while the first items are numbers associated with them.  The function displays each mini-list below
    the previous one with no brackets and a period with a space separating the number from the name.

    :return: a list of races
    """
    races = [[1, "Dragonborn"], [2, "Dwarf"], [3, "Elf"], [4, "Gnome"], [5, "Half-Elf"],
             [6, "Halfling"], [7, "Half-Orc"], [8, "Human"], [9, "Aarakocra"],
             [10, "Genasi"], [11, "Aasimar"], [12, "Ratling"], [13, "Firbolg"], [14, "Hobgoblin"],
             [15, "Kobold"], [16, "Lizardfolk"], [17, "Tiefling"], [18, "Goliath"], [19, "Goblin"],
             [20, "Kenku"], [21, "Orc"], [22, "Tabaxi"], [23, "Triton"], [24, "Feral Tiefling"],
             [25, "Tortle"], [26, "Gith"], [27, "Changeling"], [29, "Kalashtar"], [30, "Shifter"],
             [31, "Warforged"], [32, "Centaur"], [33, "Loxodon"], [34, "Minotaur"], [35, "Simic Hybrid"],
             [36, "Vedelken"], [37, "Locathah"], [38, "Verdan"]]

    # loop through the list and print each item without brackets and separate them with a period.
    for choice in races:
        print(*choice, sep=". ")
    return races


# Select a race
def select_race():
    """
    Choose a race based on user input

    :param: user must enter an integer that corresponds to a number associated with a race in the
    list generated by print_class.
    :return: Return the selected race's name as a string.
    """
    # Print a numbered list for the user.
    options = print_race()

    # Ask for user input.
    choice = int(input("Pick a number to choose a race."))

    # See if the user choice matches any numbers in the lst.
    for value in options:

        # Return the race corresponding with the chosen number.
        if choice == value[0]:
            character_race = value[1]
    return character_race





