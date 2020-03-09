from A01162209_1510_assignments.A3.create_character import roll_die

import random


# Create enemy health and name stats
def create_enemy(enemy_detail: str):
    """
    Creates enemy name and health statistics.

    :param enemy_detail: A string.
    :prostcondition: Will return a dictionary with a "Character name" key and a "Health" key.
    :return: a dictionary.
    """
    return {"Character name": enemy_detail, "Health": 5}


# Choose which fighter goes first.
def first_fighter():
    """
    See which of two fighters go first by comparing random roll numbers.

    Simulates rolling a die for each character and compares the two values.  The player with the higher
    die roll goes first.
    :Postcondition: Returns a string that can be used in conditional statements in the combat_round function
    to determine the next step in the battle, specifically which fighter goes first.
    :return: A string.
    """
    # See who goes first by rolling a die.
    input("Press enter to roll to see who goes "
          "first.")
    opponent1_roll = roll_die(1, 20)
    print("Player rolled", opponent1_roll)
    opponent2_initial_roll = roll_die(1, 20)
    print("Enemy rolled", opponent2_initial_roll)
    step = 1
    if opponent1_roll == opponent2_initial_roll:
        print("Tie! Roll again!")
    elif opponent1_roll > opponent2_initial_roll:
        print("Player goes first!!!")
        step = "player first attack"
    else:
        print("Enemy goes first!!")
        step = "enemy first attack"
    return step


# Determine if the player manages to hit the enemy.
def player_attack(enemy_name: str):
    """
    Determines if the player successfully hits the enemy or not.

    Randomly chooses whether the player's is successful.  If it is, the next step is to see how much damage is
    done. If it is not, the attack misses and the round of combat is over.  Another round will be necessary to
    determine the winner.  This function returns what the next step should be.
    :param enemy_name: A string.
    :precondition enemy_name: Must be a string.
    :postcondition: The next step in the battle.  Either the player hits and it is time to see how much damage
    was inflicted, or the player misses and it is the enemy's turn to retaliate.
    :return: a string.
    """
    input("You do a karate chop at the enemy!")
    opponent1_attack_roll = random.choice([True, False])

    # The player successfully hits the opponent and it is time to see how much damage is done..
    if opponent1_attack_roll:
        print("Your attack lands!")
        step = "player deal damage"

    # The player misses and the enemy gets to retaliate..
    else:
        print(f"Your attack misses and you fall forward!! The {enemy_name} prepares to retaliate.")
        step = "enemy retaliates"
    return step


# Determine how much damage the player does.
def player_deal_damage(enemy_stats: dict, enemy_name: str):
    """
    Determine how much damage the player inflicts on the enemy.

    :param enemy_stats: An dictionary
    :param enemy_name: A string.
    :postcondition: Will reduce the enemy's health by a certain amount if the player successfully hits.
    :return:
    """
    input("Roll to see how much damage you do.")
    damage_inflicted = roll_die(1, 5)

    # Subtract the damage from the enemy's initial health to get their remaining health.
    enemy_stats["Health"] -= damage_inflicted

    # If their remaining health is above zero,
    # They survive and now it is their turn.
    if enemy_stats["Health"] > 0:
        print(f"The {enemy_name} lost {damage_inflicted} HP!!")
        step = "enemy retaliates"

        # If their health reaches zero they are dead and the battle is over.
    else:
        print(f"You kill the {enemy_name}!")
        step = "over"
    return step


# Determine if the enemy successfully lands an attack.
def enemy_attack(enemy_name: str):
    """
    Determine if the enemy successfully hits the player.

    :param enemy_name: A string.
    :Postconditions: Let's the user know if the enemy hit them or not and returns the next step of the combat round.
    :return: A string.
    """
    input(f"As the {enemy_name} attacks, you try to evade...")
    opponent2_attack_roll = random.choice([True, False])

    # The player dodges if the enemy msses.
    if opponent2_attack_roll:
        print(f"But you are too slow! The {enemy_name} hits you!!")
        step = "enemy deal damage"

    # If the enemy successfully hits, then the next step is to determine how much damage was done.
    else:
        print(f"You do a triple back-flip out of the way, dodging the {enemy_name}'s attack!")
        step = "player retaliates"
    return step


def enemy_deal_damage(your_stats: dict, enemy_name: str):
    """
    Decide how much damage the enemy attack does.

    Randomly chooses an integer from one to five and subtracts that amount from the player's health stat.
    :param your_stats: A dictionary with a 'Health' key.
    This function returns what the next step.
    :param enemy_name: A string
    :postcondition: a string describing the next step in the interaction, either the player retaliates,
    or the player dies and the battle is over.
    :return: a string.
    """
    damage_inflicted = roll_die(1, 5)
    your_stats["Health"][1] -= damage_inflicted

    # If your remaining health is above zero, state how much health was lost
    # Now it's your turn.
    if your_stats["Health"][1] > 0:
        print("You lost " + str(damage_inflicted) + " HP!!\nYou stumble back, dazed.")
        step = "player retaliates"

    # If your health reaches zero, you are dead and the round is over.
    else:
        print(f"The {enemy_name} kills you.")
        step = "over"
    return step


# Determine if the player hits the enemy back or not.
def player_retaliate(enemy_name: str):
    """
    Determines if the player successfully hits the enemy or not.

    Randomly chooses whether the player's is successful.  If it is, the next step is to see how much damage is
    done. If it is not, the attack misses and the round of combat is over.  Another round will be necessary to
    determine the winner.  This function returns what the next step should be.
    :param enemy_name: A string.
    :precondition enemy_name: Must be a string.
    :postcondition: The next step in the interaction.  Either the player misses and the round is over, or the player
    hits and now it is time to determine how much damage is inflicted on the enemy.
    :return: a string.
    """
    input(f"You do a flying side kick at the {enemy_name}!\n"
          f"Roll to see if you hit")
    opponent1_attack_roll = random.choice([True, False])

    # If you successfully hit the enemy,
    # the next step is to see how much damage you deliver.
    if opponent1_attack_roll:
        print("Your attack lands!")
        step = "player deal damage2"

    # If you miss, the round is over.
    else:
        print("Your attack misses!!")
        step = 1
    return step


# Determine if the enemy hits the player back or not.
def enemy_retaliate(enemy_name: str):
    """
    Determines if the enemy successfully hits your character or not.

    Randomly chooses whether the enemy's attack is successful.  If it is, the next step is to see how much damage is
     done. If it is not, the attack misses and the round of combat is over.  Another round will be necessary to
    determine the winner.  This function returns what the next step should be.
    :param enemy_name: A string.
    :precondition enemy_name: Must be a string.
    "postcondition: The next step in the interaction.  Either the enemy hit the player and now it is time to determine
    how much damage was inflicted, or the enemy missed and the round is over.
    :return: A string.
    """

    input(f"As {enemy_name} attacks you try to evade...\n"
          f"Roll to see if you dodge successfully.")

    # Enemy rolls to see if they hit you.
    # If they roll higher than your dexterity, they hit you.
    opponent2_attack_roll = random.choice([True, False])
    if opponent2_attack_roll:
        print(f"But you are too slow! The {enemy_name} hits you!!")

        # Next step is to determine how uch damage they did.
        step = "enemy deal damage2"

    # If they roll too low, you dodge the attack and the round is over.
    else:
        print(f"You roll out of the way!")
        step = 1
    return step


# Determine how much damage the enemy does.
def enemy_deal_damage2(your_stats: dict, enemy_name: str):
    """
    Decide how much damage the enemy attack does.

    Randomly chooses an integer from one to five and subtracts that amount from the player's health stat.
    :param your_stats: A dictionary with a 'Health' key.
    This function returns what the next step.
    :param enemy_name: A string
    :postcondition: a string saying the round is over.
    :return: a string.
    """
    damage_inflicted = roll_die(1, 5)
    your_stats["Health"][1] = (your_stats["Health"][1] - damage_inflicted)

    # If your remaining health is above zero, state how much health was lost
    # Now it's your turn.
    if your_stats["Health"][1] > 0:
        print("You lost " + str(damage_inflicted) + " HP!!\nYou stumble back, dazed.")
        step = 1

    # If your health reaches zero, you are dead and the round is over.
    else:
        print(f"The {enemy_name} kills you.")
        step = "over"
    return step


def player_deal_damage2(enemy_stats: dict, enemy_name: str):
    """
    Decide how much damage the player's attack does.

    Randomly chooses an integer from one to five and subtracts that amount from the enemy's health stat.
    :param enemy_stats: A dictionary with a 'Health' key.
    This function returns what the next step.
    :param enemy_name: A string
    :postcondition: a string saying the round is over.
    :return: a string.
    """
    input("Roll to see how much damage you do.")
    damage_inflicted = roll_die(1, 10)

    # Subtract the damage from the enemy's initial health to get their remaining health.
    enemy_stats["Health"] -= damage_inflicted

    # If their remaining health is above zero,
    # They survive and now it is their turn.
    if enemy_stats["Health"] > 0:
        print(f"The {enemy_name} lost {damage_inflicted} HP!!")
        step = 1
        return step

        # If their health reaches zero they are dead and the battle is over.
    else:
        print(f"You kill the {enemy_name}.")
        step = "over"
        return step


def combat_round(opponent1: dict, opponent2: dict):
    """
    Describe a battle round between two characters

    Roll to see who goes first, then roll to see if the attacker hits the defender.  If the attacker misses, it is the
    defendants turn to attack.  If the attacker hits, roll to see how much damage is inflicted.  If the damage is
    greater than the defendant's health, the defendant dies and the battle is over.  If the damage is less than the
    defendant's health, the attacker's turn is over and it is the defendant's turn. Repeat the process during the
    defendants turn, except once the defendant's turn is over, the round is over.
    :param opponent1: A dictionary
    :param opponent2: A dictionary
    :Precondition opponent1 and opponent 2: Must follow the format specified by the create_character function,
    Specifically both dictionaries need a "Character name" key, an "HP" key with a list of at least two integers for its value, and a "Dexterity" Key.
    :return: Does not return anything
    """
    # Declare variables for character attributes that will be used in the battle.
    enemy_name = opponent2["Character name"]

    # When a character's health reaches zero, that character dies.
    step = 1

    # Create a sentinel variable to keep the battle running until certain events.
    # If character dies, or the characters both complete one turn each, the round is over.

    if step == 1:
        step = first_fighter()

        # If player goes first, roll to see if player successfully hits.
    if step == "player first attack":
        step = player_attack(enemy_name)

        # If the enemy goes first, then they roll to see if they hit the player.
    if step == "enemy first attack":
        step = enemy_attack(enemy_name)

        # If the player successfully hit the enemy,
        # roll to see how much damage was delivered.
    if step == "player deal damage":
        step = player_deal_damage(opponent2, enemy_name)

        # If the enemy hits the player,
        # Roll to see how much damage is delivered.
    if step == "enemy deal damage":
        step = enemy_deal_damage(opponent1, enemy_name)

        # If the enemy attacks first and you survive, you can attack back.
        # Roll to see if you hit the enemy.
    if step == "player retaliates":
        step = player_retaliate(enemy_name)

        # If you go first and don't kill the enemy, the enemy gets to retaliate.
    if step == "enemy retaliates":
        step = enemy_retaliate(enemy_name)

    if step == "player deal damage2":
        step = player_deal_damage2(opponent2, enemy_name)

    if step == "enemy deal damage2":
        step = enemy_deal_damage2(opponent1, enemy_name)

    return step


def combat(player: dict, enemy_stats: dict):
    """
    Calls the combat_round function until the battle is over.

    :param player: a dictionary
    :param enemy_stats: a dictionary
    :precondition: Both parameters must have a "Health Key"
    :return:
    """
    print("Your health:", player["Health"][1])
    print("Enemy health:", enemy_stats["Health"])
    battle = "ongoing"
    # make a while loop to keep the battle going until one of the combatants die.
    while battle == "ongoing":
        step_of_the_battle = combat_round(player, enemy_stats)

        #If a combatant dies, one of the functions will return "over" as a step value,
        # which will end the battle.
        if step_of_the_battle == "over":
            battle = "over"

