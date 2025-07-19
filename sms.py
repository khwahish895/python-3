import requests

def send_sms_via_textbelt(number, message):
    resp = requests.post(
        'https://textbelt.com/text',
        {
            'phone': number,
            'message': message,
            'key': 'textbelt',
        },
    )
    return resp.json()

result = send_sms_via_textbelt('1987654321', 'Hello via TextBelt API!')
print(result)
