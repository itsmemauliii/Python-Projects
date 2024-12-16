# challenge3_dice_roll.py

import random

# Roll two dice and ask the user to guess the sum until correct
correct_answer = random.randint(1, 6) + random.randint(1, 6)
guess = None

while guess != correct_answer:
    guess = int(input("What is the total (2-12)? "))
    if guess != correct_answer:
        print("Try again!")

print("You got it!")
