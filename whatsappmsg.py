import pyautogui
import time

def send_whatsapp_message(contact, message):
    # Open WhatsApp Web
    pyautogui.hotkey("ctrl", "t")  # Open a new tab
    pyautogui.typewrite("https://web.whatsapp.com", interval=0.1)
    pyautogui.hotkey("enter")
    time.sleep(10)  # Wait for WhatsApp Web to load

    # Search for the contact
    pyautogui.hotkey("ctrl", "f")  # Open search
    pyautogui.typewrite(contact, interval=0.1)
    time.sleep(2)  # Wait for search results
    pyautogui.hotkey("enter")  # Select the contact
    time.sleep(2)  # Wait for chat to open

    # Type the message
    pyautogui.typewrite(message, interval=0.1)
    pyautogui.hotkey("enter")  # Send the message

# Example usage
send_whatsapp_message("Contact Name", "Hello, how are you?")
