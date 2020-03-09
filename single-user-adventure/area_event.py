from A01162209_1510_assignments.A3.combat import create_enemy
from A01162209_1510_assignments.A3.combat import combat
from A01162209_1510_assignments.A3.create_character import roll_die
from A01162209_1510_assignments.A3.navigation import enemy_action

# Set an enemy to have a 25% chance of appearing.
def enemy_appear():
    """
    Cause an enemy to appear 25% of the time this function is called.

    :postcondition: returns True if an enemy appears and False if the enemy does not.
    :return: a boolean.
    """
    enemy_appearance = roll_die(1, 4)
    if enemy_appearance == 1:
        return True
    else:
        return False


# Give the character the option to flee if an enemy appears.
def flee(player: dict, enemy: str):
    """
    Describes the player running away from the enemy.

    There is a 10% chance the enemy will attack the player and inflict damage if the player tries to flee.
    :param player: a dictionary.
    :param enemy: a string.
    :precondition player: must have the key "Health" attached to a list of at least two integers as a key, value pair.
    :precondition enemy: must be a string.
    """
    print("You decide to flee")

    # There's a 10% chance the enemy will hit you when you run away.
    enemy_attack = roll_die(1, 10)
    if enemy_attack==1:
        damage = (roll_die(1, 4))
        player["Health"][1] -= damage
        print(f"The {enemy} strikes you as you flee.  You lost {damage} HP!")
    else:
        print("The enemy tries to strike you, but you get away!")


# Create a function for fighting monsters.
def room_event(player: dict, enemy_detail: str):
    """
    Describe an altercation with a monster,

    This function calls helper functions to print location-specific enemy details if an enemy appears,
    and if the player chooses to fight the enemy or run away.  The function calls a combat function for fighting the
    enemy or a fleeing function for running away.
    If there is no monster, the player gains two health points.
    :param player: A dictionary
    :param enemy_detail: a String
    :precondition player: player must have a "Health" key.
    """
    # Player Gains 2 health points every time they move and don't encounter a monster.
    monster = enemy_appear()
    if not monster and player["Health"][1] <= 8:
        player["Health"][1] += 2
    enemy = create_enemy(enemy_detail)
    enemy_scenario = enemy_action()

    # Give the player the option to run or fight, and call corresponding functions
    # to describe the battle or running away.
    while monster:
        print(enemy_scenario[enemy_detail])
        fight_or_not = int(input("1 for fight, 2 or flee"))
        if fight_or_not == 2:
            flee(player, enemy_detail)
            monster = False
        elif fight_or_not == 1:
            combat(player, enemy)
            monster = False

        # If the player enters an invalid choice.
        else:
            print("Invalid choice")


