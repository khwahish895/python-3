import smtplib
from email.mime.text import MIMEText

def send_email_via_smtp(to_email, subject, message):
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    smtp_user = 'your_email@example.com'  # Your email
    smtp_password = 'your_password'  # Your email password

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'fake_email@example.com'  # Fake email address
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

# Example usage
send_email_via_smtp("recipient@example.com", "Hello!", "This is a test email.")
