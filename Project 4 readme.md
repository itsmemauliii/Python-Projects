# Quiz Game

This is a simple command-line quiz game written in Python. Players are presented with a series of multiple-choice questions and must choose the correct option to score points.

## Features
- Multiple-choice questions.
- Real-time feedback on whether the answer is correct or incorrect.
- Keeps track of the score and provides feedback at the end of the game.

## Prerequisites
- Python 3.x installed on your system.

## How to Play
1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory containing the script.
3. Run the game using the command:
   ```
   python quiz_game.py
   ```
4. Follow the on-screen instructions to answer the questions by entering the number corresponding to your chosen option.

## Example Gameplay
```
Welcome to the Quiz Game!

Question 1: What is the capital of France?
1. Paris
2. Berlin
3. Rome
4. Madrid
Enter the number of your answer: 1
Correct!

Question 2: Which programming language is known as the backbone of web development?
1. Python
2. JavaScript
3. C++
4. Java
Enter the number of your answer: 2
Correct!

Your final score is: 2/2
Excellent! You got all questions right!
```

## Customization
You can easily customize the questions and answers by modifying the `data` variable in the `quiz_game.py` file. Each question should be a dictionary containing:
- `question`: The text of the question.
- `options`: A list of answer choices.
- `answer`: The correct answer (must match one of the options).

## License
This project is open-source and available for personal and educational use.
