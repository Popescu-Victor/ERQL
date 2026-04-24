from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def hw_scrape(username, password):
    driver = webdriver.Edge() 

    driver.get("https://roarmy.adlunap.ro")
    time.sleep(2)
 
    username = driver.find_element(By.ID, "username")  # change selector
    username.send_keys(username)

    password = driver.find_element(By.ID, "password")  # change selector
    password.send_keys(password)

    password.send_keys(Keys.RETURN)
    
    time.sleep(5)

    print("Logged in (hopefully)")

    driver.quit()