from A01162209_1510_assignments.A3.create_character import create_character
from A01162209_1510_assignments.A3.create_character import print_inventory
from A01162209_1510_assignments.A3.create_character import choose_inventory
from A01162209_1510_assignments.A3.area_event import room_event
from A01162209_1510_assignments.A3.navigation import establish_board_boundaries
from A01162209_1510_assignments.A3.navigation import make_board_details
from A01162209_1510_assignments.A3.navigation import room_enemy_details
from A01162209_1510_assignments.A3.navigation import get_user_choice
from A01162209_1510_assignments.A3.navigation import check_if_exit_reached
from A01162209_1510_assignments.A3.navigation import move_character
from A01162209_1510_assignments.A3.navigation import validate_move
from A01162209_1510_assignments.A3.combat import combat
import doctest


def main():
    """
    Drive all the games in this function.

    :return:
    """

    print("Hello Adventurer, welcome to the fantastic realm of Jamesland. "
          " Normally it is very nice, but dark forces of evil have taken"
          "over and there are monsters everywhere now."
          "The only way you can save James Land is to travel to the "
          "Castle on evil mountain and battle Mecha-Hitler.  If you defeat him, James land will be sunny and happy "
          "again.")
    board = establish_board_boundaries()
    board_details = make_board_details()
    character = create_character()

    # Make a while loop to keep the game going until the exit is reached.
    found_exit = False
    while not found_exit:
        character_position = (character["Position"][0], character["Position"][1])
        position_details = board_details[character_position]
        enemy_action = room_enemy_details()
        if character_position == (3, 3):
            print_inventory()
            item = choose_inventory()
            character["Inventory"].append(item)

        enemy_details = enemy_action[character_position]
        print(position_details)
        room_event(character, enemy_details)
        if character["Health"][1] <= 0:
            print("Oh no! you died!")
            break
        direction = get_user_choice()
        if direction == "quit":
            break
        else:
            valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            found_exit = check_if_exit_reached(board, character)
        else:
            print("Choose another direction")
    if found_exit:
        print("The doors swing open and out comes Mecha-Hitler.")
        mecha_hitler = {"Character name": "Evil Nazi Cyborg Hitler", "Health": 3}
        combat(character, mecha_hitler)
        if character["Health"][1] > 0:
            print("You won!! James land is saved!!")
        else:
            print("Mecha Hitler kills you with his terrifying mustache. You were the last hope,"
                  "now James land will be shrouded in darkness for 5000 years.")
    else:
        print("Game Over")


if __name__ == "__main__":
    doctest.testmod()
    main()
