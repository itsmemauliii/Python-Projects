import random

mood_to_songs = {
    "happy": ["Happy - Pharrell Williams", "Uptown Funk - Mark Ronson ft. Bruno Mars", "Can't Stop the Feeling - Justin Timberlake"],
    "sad": ["Someone Like You - Adele", "Let Her Go - Passenger", "Fix You - Coldplay"],
    "relaxed": ["Weightless - Marconi Union", "Breezin' - George Benson", "Dreams - Fleetwood Mac"],
    "energetic": ["Eye of the Tiger - Survivor", "Lose Yourself - Eminem", "Stronger - Kanye West"],
    "romantic": ["Perfect - Ed Sheeran", "Thinking Out Loud - Ed Sheeran", "All of Me - John Legend"]
}

def get_user_mood():
    print("Welcome to the Mood-Based Music Recommender!")
    print("Moods to choose from: happy, sad, relaxed, energetic, romantic")
    mood = input("Enter your current mood: ").strip().lower()
    return mood

def recommend_song(mood):
    if mood in mood_to_songs:
        song = random.choice(mood_to_songs[mood])
        print(f"Based on your mood '{mood}', we recommend: {song}")
    else:
        print("Sorry, we don't have recommendations for that mood yet.")

if __name__ == "__main__":
    user_mood = get_user_mood()
    recommend_song(user_mood)
