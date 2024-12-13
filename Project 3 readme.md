# Automate Secret Santa Emails with SMTP

## Overview

This project automates the process of sending Secret Santa emails using the Simple Mail Transfer Protocol (SMTP). The system randomly assigns Secret Santa pairs and sends personalized emails to participants, making the holiday season more enjoyable and less time-consuming.

## Features

- Randomly assigns Secret Santa pairs
- Sends personalized emails to each participant using SMTP
- Customizable email template
- Simple to set up and use

## Requirements

- Python 3.x
- SMTP server (e.g., Gmail, Outlook)
- `smtplib` and `random` libraries (included in Python's standard library)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/automate-secret-santa-emails.git
cd automate-secret-santa-emails
```

### 2. Install Dependencies

No additional dependencies are required for this project, as it uses Python's built-in libraries.

### 3. Configure Your SMTP Server

Make sure to update the SMTP server configuration in the code with your email provider's details.

- For Gmail, you will need to enable **Less secure apps** or set up an **App password**.
- For Outlook, use the **SMTP settings for Outlook**.

In the script, modify the following variables:
- `SMTP_SERVER`
- `SMTP_PORT`
- `SENDER_EMAIL`
- `SENDER_PASSWORD`

### 4. Add Participants

Create a file named `participants.csv` with the list of participants and their email addresses. The CSV should have the following format:

```csv
Name,Email
Mauli Patel,maulipatel18@gmail.com
Snowflake crystal,crystal@gmail.com
...
```

### 5. Run the Script

Run the script to start the Secret Santa email process:

```bash
python secret_santa.py
```

The script will:
- Randomly pair participants
- Send personalized Secret Santa emails with the assignment

### 6. Customize Email Template (Optional)

You can customize the email body and subject in the `secret_santa.py` file. The template uses placeholders for names and assignments, which will be replaced dynamically for each participant.

## Example Email

```txt
Subject: Your Secret Santa Assignment!

Dear [Name],

You are the Secret Santa for [Recipient Name]! Please make sure to keep your identity a secret!

Happy Holidays!

Best,
Your Secret Santa Team
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Python's `smtplib` library for email sending
- Python's `random` library for generating random Secret Santa pairs
```
