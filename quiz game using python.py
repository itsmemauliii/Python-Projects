# Quiz Game

# List of questions and answers
data = [
    {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Rome", "Madrid"], "answer": "Paris"},
    {"question": "Which programming language is known as the backbone of web development?", "options": ["Python", "JavaScript", "C++", "Java"], "answer": "JavaScript"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"question": "What does CPU stand for?", "options": ["Central Processing Unit", "Central Process Unit", "Computer Processing Unit", "Core Processing Unit"], "answer": "Central Processing Unit"},
    {"question": "Who wrote the novel '1984'?", "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "Ernest Hemingway"], "answer": "George Orwell"}
]

score = 0

print("Welcome to the Quiz Game!\n")

# Loop through questions
for i, item in enumerate(data):
    print(f"Question {i + 1}: {item['question']}")
    for idx, option in enumerate(item["options"], 1):
        print(f"{idx}. {option}")

    # Take user input
    while True:
        try:
            choice = int(input("Enter the number of your answer: "))
            if 1 <= choice <= len(item["options"]):
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a number.")

    # Check answer
    if item["options"][choice - 1] == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {item['answer']}\n")

# Final score
print(f"Your final score is: {score}/{len(data)}")
if score == len(data):
    print("Excellent! You got all questions right!")
elif score > len(data) / 2:
    print("Great job! You scored above average.")
else:
    print("Better luck next time!")
