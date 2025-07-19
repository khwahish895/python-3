from twilio.rest import Client

# Twilio credentials
account_sid = 'ACcb2ce42f2a0fa69acb693fcf558df7d5'  # Replace with your Account SID
auth_token = 'a76a9343e5a67ba5e1562f993f27f765'      # Replace with your Auth Token
client = Client(account_sid, auth_token)

# Send a WhatsApp message
message = client.messages.create(
    body='Hello from Python via Twilio!',
    from_='whatsapp:+14155238886',  # Your Twilio WhatsApp number
    to='whatsapp:+917424988589'        # Recipient's phone number
)

print(f"Message sent successfully. Message ID: {message.sid}")
