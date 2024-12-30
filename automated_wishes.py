import tkinter as tk
from datetime import datetime

# Function to display automated wishes
def display_wishes():
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        wish = "Good Morning! Have a wonderful day ahead!"
    elif 12 <= current_hour < 18:
        wish = "Good Afternoon! Hope you're having a great day!"
    elif 18 <= current_hour < 21:
        wish = "Good Evening! Relax and enjoy your evening!"
    else:
        wish = "Good Night! Sweet dreams and take care!"

    label.config(text=wish)

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Automated Wishes")
root.geometry("400x200")
root.configure(bg="lightblue")

# Create a label to display the wishes
label = tk.Label(root, text="Click the button to see your wish!", font=("Arial", 14), bg="lightblue", wraplength=350)
label.pack(pady=20)

# Create a button to trigger the wishes
button_wish = tk.Button(root, text="Get Wish", font=("Arial", 12, "bold"), bg="white", fg="blue", command=display_wishes)
button_wish.pack(pady=10)

# Create an exit button
button_exit = tk.Button(root, text="Exit", font=("Arial", 12, "bold"), bg="white", fg="red", command=exit_app)
button_exit.pack(pady=10)

# Run the main event loop
root.mainloop()
