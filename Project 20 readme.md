# Automated Wishes Application

This Python application creates an interactive graphical user interface (GUI) using the `tkinter` module. The application displays automated wishes (e.g., "Good Morning," "Good Afternoon," etc.) based on the time of day. Additionally, it provides a simple exit button to close the application.

## Features

- **Automated Wishes**: Displays appropriate greetings based on the current time.
  - Morning: 5 AM to 12 PM
  - Afternoon: 12 PM to 6 PM
  - Evening: 6 PM to 9 PM
  - Night: 9 PM to 5 AM
- **Interactive Buttons**:
  - **Get Wish**: Displays the wish in the application window.
  - **Exit**: Closes the application.
- **User-Friendly Interface**: Simple and attractive design with a light blue background.

## Requirements

- Python 3.x
- `tkinter` module (comes pre-installed with Python on most platforms)

## Installation

1. Ensure that Python is installed on your system.
2. Clone this repository or download the source code.
3. Save the script as `automated_wishes.py`.

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory where `automated_wishes.py` is saved.
3. Run the script using the following command:
   ```bash
   python automated_wishes.py
   ```

## Code Overview

The application uses `tkinter` to create the GUI and `datetime` to determine the current hour for generating wishes.

### Key Functions

- `display_wishes()`: Determines the appropriate greeting based on the time and updates the GUI.
- `exit_app()`: Closes the application when the "Exit" button is clicked.

## Customization

- **Greetings**: Modify the greetings in the `display_wishes()` function to personalize the messages.
- **Design**: Update the `bg` (background) or `font` parameters in the `tk.Label` and `tk.Button` widgets to customize the appearance.

## License

This project is open-source and free to use. Feel free to modify and distribute it as needed.

---

Enjoy your automated wishes application! 😊
