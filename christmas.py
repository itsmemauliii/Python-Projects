import time
from datetime import datetime

def calculate_time_remaining():
    """Calculates the time remaining until Christmas."""
    now = datetime.now()
    christmas_date = datetime(now.year, 12, 25)
    if now > christmas_date:
        christmas_date = datetime(now.year + 1, 12, 25)
    time_left = christmas_date - now
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return days, hours, minutes, seconds

def display_christmas_tree():
    """Displays a festive ASCII art Christmas tree."""
    tree = """
          🎄 Merry Christmas 🎄
                *
               /|\\
              /*|O\\
             /*/|\\*\\
            /X/O|*\\X\\
           /*/X/|\\X\\*\\
          /O/*/X|O\\X\\X\\
               |X|
               |X|
    """
    print(tree)

def interactive_countdown():
    """Displays a dynamic interactive Christmas countdown."""
    print("🎅 Welcome to the Unique Christmas Countdown! 🎅")
    print("Watch the time tick away as we approach Christmas 🎄\n")
    print("Press Ctrl+C to exit at any time.\n")
    
    try:
        while True:
            days, hours, minutes, seconds = calculate_time_remaining()
            
            # Clear the screen for a dynamic effect (works in most terminals)
            print("\033[H\033[J", end="")
            
            # Show the Christmas tree
            display_christmas_tree()
            
            # Show the countdown
            print(f"⏳ Time Until Christmas 🎄:")
            print(f"   {days} Days, {hours:02} Hours, {minutes:02} Minutes, {seconds:02} Seconds")
            print("\n✨ Stay festive and joyful! 🎉")
            
            time.sleep(1)  # Update the countdown every second
    
    except KeyboardInterrupt:
        print("\n🎄 Countdown interrupted. Wishing you a Merry Christmas in advance! 🎅")

if __name__ == "__main__":
    interactive_countdown()
