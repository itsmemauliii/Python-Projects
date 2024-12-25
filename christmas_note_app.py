import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

def send_email(subject, body, recipient_email):
    """
    Sends an email with the given subject and body to the specified recipient email.
    """
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def send_note():
    """
    Collects user input and sends the note via email.
    """
    note = note_entry.get("1.0", tk.END).strip()
    email = email_entry.get().strip()
    
    if not note or not email:
        messagebox.showerror("Error", "Please enter both a note and an email address.")
        return
    
    subject = "🎅 Your Christmas Note from the Note Taker 🎄"
    body = (
        "Ho Ho Ho! 🎅\n\n"
        "Here's a special Christmas-themed note you just added:\n\n"
        f"{note}\n\n"
        "Wishing you a Merry Christmas and a Happy New Year! 🎄✨"
    )
    
    success = send_email(subject, body, email)
    if success:
        messagebox.showinfo("Success", "Your note was emailed successfully!")
    else:
        messagebox.showerror("Error", "Failed to send the email. Please try again.")

# Create the GUI
app = tk.Tk()
app.title("Christmas Note Taker 🎄")

tk.Label(app, text="Enter your festive note:", font=("Arial", 12)).pack(pady=10)
note_entry = tk.Text(app, height=10, width=40, font=("Arial", 10))
note_entry.pack(pady=5)

tk.Label(app, text="Enter your email address:", font=("Arial", 12)).pack(pady=10)
email_entry = tk.Entry(app, width=40, font=("Arial", 10))
email_entry.pack(pady=5)

send_button = tk.Button(app, text="Send Note 🎅", font=("Arial", 12), command=send_note)
send_button.pack(pady=20)

app.mainloop()
