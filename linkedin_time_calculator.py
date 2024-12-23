# LinkedIn Time Calculator

def calculate_reading_time(words_count, words_per_minute=200):
    """Calculate the reading time in minutes."""
    reading_time = words_count / words_per_minute
    return round(reading_time, 2)

def calculate_typing_time(words_count, typing_speed=40):
    """Calculate the typing time in minutes."""
    typing_time = words_count / typing_speed
    return round(typing_time, 2)

def main():
    """Main function to calculate LinkedIn post time metrics."""
    print("Welcome to the LinkedIn Time Calculator!")
    words_count = int(input("Enter the total word count of your LinkedIn post: "))

    reading_time = calculate_reading_time(words_count)
    typing_time = calculate_typing_time(words_count)

    print(f"\nFor a LinkedIn post with {words_count} words:")
    print(f"Estimated reading time: {reading_time} minutes")
    print(f"Estimated typing time: {typing_time} minutes")
    
    print("Happy Exploring!❄️😊")

if __name__ == "__main__":
    main()
