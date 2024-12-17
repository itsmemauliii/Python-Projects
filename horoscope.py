import random

horoscopes = {
    "aries": ["Today is a great day to start something new!", 
              "You may feel energetic and motivated to take charge.",
              "Stay patient—good things are on the way."],
    "taurus": ["Focus on your goals; hard work pays off!", 
               "You may find peace in small pleasures today.",
               "Avoid unnecessary stress and take it slow."],
    "gemini": ["Your curiosity will lead you to exciting discoveries.", 
               "Communication will open new doors for you today.",
               "Stay flexible and adapt to changes gracefully."],
    "cancer": ["It's a good day to connect with loved ones.", 
               "Your intuition is strong—trust your instincts.",
               "Embrace self-care and relaxation."],
    "leo": ["You are shining bright today—share your enthusiasm!", 
            "Take pride in your achievements and keep going.",
            "A small challenge may come your way; stay confident."],
    "virgo": ["Focus on the details—your precision is your strength.", 
              "Organize your plans for a productive day.",
              "Don't overthink; trust your process."],
    "libra": ["Balance is key today; find time for yourself.", 
              "Good vibes are headed your way—stay open.",
              "Harmony in relationships will bring joy."],
    "scorpio": ["Today is full of transformation and renewal.", 
                "Your focus will help you achieve big things.",
                "Keep your emotions balanced and positive."],
    "sagittarius": ["Adventure is calling—step out of your comfort zone.", 
                    "An opportunity for learning awaits.",
                    "Your optimism will inspire those around you."],
    "capricorn": ["Your determination will help you overcome obstacles.", 
                  "Focus on long-term goals and stay committed.",
                  "Take pride in your efforts today."],
    "aquarius": ["Innovation and creativity are your strengths today.", 
                 "A new idea might surprise you—embrace it!",
                 "Stay true to yourself and your goals."],
    "pisces": ["Your compassion will touch someone's life today.", 
               "Take time to dream and reflect on your goals.",
               "Go with the flow and trust the universe."]
}

def get_horoscope(sign):
    """Fetch a random horoscope for the given zodiac sign."""
    sign = sign.lower()
    if sign in horoscopes:
        return random.choice(horoscopes[sign])
    else:
        return "Sorry, that's not a valid zodiac sign. Please try again."

def main():
    print("🌟 Welcome to the Daily Horoscope Generator 🌟")
    print("Available Zodiac Signs: Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces\n")
    while True:
        user_sign = input("Enter your zodiac sign (or type 'exit' to quit): ").strip()
        if user_sign.lower() == 'exit':
            print("Goodbye! Have a great day ahead! 🌟")
            break
        message = get_horoscope(user_sign)
        print(f"🔮 Your Horoscope: {message}\n")

if __name__ == "__main__":
    main()
