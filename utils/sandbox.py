from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()  # or webdriver.Chrome()

# 1. Open login page
driver.get("https://roarmy.adlunap.ro")

time.sleep(2)  # wait for page to load (better: use WebDriverWait in real projects)

# 2. Find username/email field
username = driver.find_element(By.ID, "username")  # change selector
username.send_keys("popescu.victor")

# 3. Find password field
password = driver.find_element(By.ID, "password")  # change selector
password.send_keys("your_password")

# 4. Submit form
password.send_keys(Keys.RETURN)

# OR click login button instead:
# login_button = driver.find_element(By.ID, "loginButton")
# login_button.click()

time.sleep(5)

print("Logged in (hopefully)")

driver.quit()