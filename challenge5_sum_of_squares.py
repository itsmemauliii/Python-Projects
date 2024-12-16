# challenge5_sum_of_squares.py

# Get the user's input and calculate the sum of squares of numbers from 1 to that number
number = int(input("Enter a number: "))
total = 0

for i in range(1, number + 1):
    total += i ** 2

print(f"The sum of squares from 1 to {number} is {total}")
