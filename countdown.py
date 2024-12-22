import time

# Fun challenges for each day leading up to 2025
challenges = [
    "Day 9: Reflect on your biggest achievement in 2024. 🏆",
    "Day 8: Set one bold goal for 2025. 🎯",
    "Day 7: Take a moment to appreciate your growth this year. 🌱",
    "Day 6: Write a letter to your future self. ✍️",
    "Day 5: Help someone today, spread kindness! 🤝",
    "Day 4: Identify a skill you want to master in 2025. 🔧",
    "Day 3: Commit to a new habit that will improve your well-being. 🧘‍♂️",
    "Day 2: Plan your first step towards a new adventure in 2025. 🚀",
    "Day 1: Celebrate your progress, no matter how small. 🎉"
]

# Function to show the countdown and daily challenge
def countdown_to_new_year():
    print("🎉 Countdown to 2025! 🎉")
    for i in range(9, 0, -1):
        print(f"\n✨ {i} days left to go! ✨")
        print(challenges[9 - i])  # Show the challenge for that day
        time.sleep(1)  # Pause for 1 second before moving to the next day

    print("\n🎆 Welcome 2025! 🎆")
    print("Let's make it our best year yet! 🌟")

# Main function to run the project
if __name__ == "__main__":
    countdown_to_new_year()
