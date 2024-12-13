# A simple text-based adventure game


def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself standing in front of a mysterious castle.")
    print("The air is cold, and the castle's gates creak in the wind.")
    print("You have two options:")
    print("1. Enter the castle")
    print("2. Walk around the castle")


def enter_castle():
    print("\nYou enter the castle. The inside is dark and musty.")
    print("There are two doors in front of you.")
    print("1. Go through the left door")
    print("2. Go through the right door")

    choice = input("> ")
    if choice == "1":
        left_door()
    elif choice == "2":
        right_door()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        enter_castle()


def left_door():
    print("\nYou open the left door and enter a small room.")
    print("In the center of the room is a pedestal with a glowing gem on it.")
    print("Do you:")
    print("1. Take the gem")
    print("2. Leave the room")

    choice = input("> ")
    if choice == "1":
        print(
            "\nAs you grab the gem, the floor beneath you collapses and you fall into a pit. Game Over!"
        )
    elif choice == "2":
        print("\nYou leave the room and head back to the main hallway.")
        enter_castle()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        left_door()


def right_door():
    print(
        "\nYou open the right door and find a treasure chest in the corner of the room."
    )
    print("There are strange markings on the chest. Do you:")
    print("1. Open the chest")
    print("2. Leave the chest alone")

    choice = input("> ")
    if choice == "1":
        print(
            "\nInside the chest, you find piles of gold and jewels! You win!")
    elif choice == "2":
        print(
            "\nYou decide to leave the chest alone and return to the main hallway."
        )
        enter_castle()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        right_door()


def start_game():
    intro()
    choice = input("> ")
    if choice == "1":
        enter_castle()
    elif choice == "2":
        print(
            "\nYou walk around the castle but nothing interesting happens. Maybe you should try entering it?"
        )
        start_game()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        start_game()


# Start the game
start_game()
