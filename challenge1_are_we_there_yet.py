# challenge1_are_we_there_yet.py

# Prompt the user until they answer "Yes"
answer = ""
while answer.lower() != "yes":
    answer = input("Are we there yet? ")
    if answer.lower() != "yes":
        print("Keep going...")

print("You got it!")
