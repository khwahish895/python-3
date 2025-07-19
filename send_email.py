import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "khwahishsingh2005@gmail.com"  # Replace with your email
receiver_email = "khwahishsingh2005@gmail.com"  # Replace with recipient's email
password = "xxxxxxxx"  # Replace with your email password

# Create the email subject and body
subject = "Test Email from Python"
body = "Hello, this is a test email sent from Python!"

# Create a multipart email
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the email body to the message
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(sender_email, password)  # Log in to your email account
    server.send_message(msg)  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the connection
