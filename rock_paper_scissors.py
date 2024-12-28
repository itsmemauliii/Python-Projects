from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
