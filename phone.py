   from twilio.rest import Client

   # Your Twilio account SID and Auth Token
   account_sid = 'your_account_sid'  # Replace with your Account SID
   auth_token = 'your_auth_token'      # Replace with your Auth Token
   twilio_number = 'your_twilio_number'  # Replace with your Twilio phone number
   to_number = 'recipient_phone_number'  # Replace with the recipient's phone number

   # Create a Twilio client
   client = Client(account_sid, auth_token)

   # Make a call
   call = client.calls.create(
       to=to_number,
       from_=twilio_number,
       url='http://demo.twilio.com/docs/voice.xml'  # URL for TwiML instructions
   )

   print(f"Call initiated: {call.sid}")
   