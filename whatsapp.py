from twilio.rest import Client

# Twilio credentials
account_sid = ''  # Replace with your Account SID
auth_token = ''      # Replace with your Auth Token
client = Client(account_sid, auth_token)

# Send a WhatsApp message
message = client.messages.create(
    body='Hello from Python via Twilio!',
    from_='whatsapp:',  # Your Twilio WhatsApp number
    to='whatsapp:'        # Recipient's phone number
)

print(f"Message sent successfully. Message ID: {message.sid}")
