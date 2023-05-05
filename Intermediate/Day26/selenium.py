from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the list of email addresses
emails = ['20152447@stu.uob.edu.bh', '20162100@stu.uob.edu.bh', '20174676@stu.uob.edu.bh', '20175184@stu.uob.edu.bh', '20176499@stu.uob.edu.bh', '20178652@stu.uob.edu.bh', '20180206@stu.uob.edu.bh', '20180867@stu.uob.edu.bh', '20180942@stu.uob.edu.bh', '20182315@stu.uob.edu.bh', '20183709@stu.uob.edu.bh', '20186302@stu.uob.edu.bh', '20191446@stu.uob.edu.bh', '20192449@stu.uob.edu.bh', '20192476@stu.uob.edu.bh', '20192727@stu.uob.edu.bh', '20192823@stu.uob.edu.bh', '20194439@stu.uob.edu.bh', '20194541@stu.uob.edu.bh', '20194896@stu.uob.edu.bh', '20195070@stu.uob.edu.bh', '20195239@stu.uob.edu.bh', '20196964@stu.uob.edu.bh', '20197790@stu.uob.edu.bh', '20197825@stu.uob.edu.bh', '20198783@stu.uob.edu.bh', '202002021@stu.uob.edu.bh', '202003303@stu.uob.edu.bh', '202008533@stu.uob.edu.bh', '202009254@stu.uob.edu.bh']


# Launch the browser and go to the Microsoft Teams login page
driver = webdriver.Chrome()
driver.get("https://teams.microsoft.com/")

# Wait for the page to load and find the email input field
time.sleep(5)  # wait for the page to load
email_input = driver.find_element_by_name("loginfmt")

# Enter the email address and submit the form
email_input.send_keys("202009254@stu.uob.edu.bh")
email_input.send_keys(Keys.RETURN)

# Wait for the page to load and find the password input field
time.sleep(5)  # wait for the page to load
password_input = driver.find_element_by_name("passwd")

# Enter the password and submit the form
password_input.send_keys("$")
password_input.send_keys(Keys.RETURN)

# Wait for the page to load and find the search input field
time.sleep(10)  # wait for the page to load
search_input = driver.find_element_by_xpath("//input[@aria-label='Search teams and channels']")

# Loop through the email list and search for each user
for email in emails:
    # Enter the email address in the search input field and submit the form
    search_input.send_keys(email)
    search_input.send_keys(Keys.RETURN)

    # Wait for the page to load and find the user name
    time.sleep(5)  # wait for the page to load
    try:
        user_name = driver.find_element_by_xpath("//span[contains(text(), '@')]")
        print(f"{email}: {user_name.text}")
    except:
        print(f"{email}: User not found")

    # Clear the search input field for the next search
    search_input.clear()

# Close the browser
driver.quit()