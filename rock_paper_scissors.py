from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")
    player = False
    computer = t[randint(0, 2)]
