# Christmas Note Taker 🎅🎄

A simple Python application to send festive Christmas notes via email. This program combines email automation with a user-friendly graphical interface to share your holiday cheer.

## Features
- Create festive notes with a friendly GUI using `tkinter`.
- Send personalized emails directly from the app.
- Securely collects sender credentials using `simpledialog`.
- Festive-themed subject and message body for emails.

---

## Requirements

Before running the program, ensure you have the following:
- Python 3.6 or above installed.
- Required Python libraries:
  - `smtplib`
  - `email`
  - `tkinter`
- Access to a Gmail account for sending emails (or other SMTP configurations if modified).

---

## Setup Instructions

1. Clone or download this repository:
   ```bash
   git clone https://github.com/itsmemauliii/Python-Projects/
   ```
2. Open a terminal and navigate to the project directory:
   ```bash
   cd Python-Projects
   ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: `tkinter` is included with most Python installations and does not require additional installation.)*

---

## Running the Program

Run the script using Python:
```bash
python christmas_note_taker.py
```

---

## How It Works

1. **Create a Note:**  
   Write your festive message in the text box provided in the app.

2. **Recipient's Email:**  
   Enter the recipient's email address in the input field.

3. **Send Email:**  
   - The app will prompt you to enter your email address and password securely.  
   - Click "Send Note 🎅" to send your message.

4. **Receive Confirmation:**  
   A success or error message will indicate the status of your email.

---

## Customizing SMTP Settings

Currently, the app uses Gmail's SMTP server. To use another email provider, update the following lines in the `send_email` function:
```python
with smtplib.SMTP("smtp.gmail.com", 587) as server:
```
Replace `"smtp.gmail.com"` and `587` with the SMTP server and port of your email provider.

---

## Security Note

- The app does **not** store your email credentials. However, to avoid sharing your primary account credentials, consider generating an **App Password** for Gmail.
- For more information on App Passwords, refer to [Google's documentation](https://support.google.com/accounts/answer/185833?hl=en).

---

## Example Email

**Subject:** 🎅 Your Christmas Note from the Note Taker 🎄  
**Body:**
```
Ho Ho Ho! 🎅

Here's a special Christmas-themed note you just added:

<Your Note>

Wishing you a Merry Christmas and a Happy New Year! 🎄✨
```

---

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

---

## Contributing

Contributions are welcome! If you have ideas to improve this app, feel free to submit a pull request or open an issue.

---

### 🎄 Merry Christmas and Happy Coding! 🎅✨
