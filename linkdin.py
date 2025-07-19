   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.common.keys import Keys
   from webdriver_manager.chrome import ChromeDriverManager
   import time

   # Set up the browser
   driver = webdriver.Chrome(ChromeDriverManager().install())
   driver.get("https://www.linkedin.com/login")

   # Log in to LinkedIn
   username = driver.find_element(By.ID, "username")
   password = driver.find_element(By.ID, "password")
   username.send_keys("your_email@example.com")  # Replace with your LinkedIn email
   password.send_keys("your_password")  # Replace with your LinkedIn password
   driver.find_element(By.XPATH, "//button[@type='submit']").click()
   time.sleep(3)

   # Navigate to the message section
   driver.get("https://www.linkedin.com/messaging/")
   time.sleep(3)

   # Send a message
   message_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
   message_box.send_keys("Hello, this is a test message.")
   message_box.send_keys(Keys.RETURN)  # Press Enter to send the message
   print("Message sent successfully.")

   # Close the browser
   driver.quit()
   