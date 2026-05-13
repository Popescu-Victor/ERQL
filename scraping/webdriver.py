from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def hw_scrape(username, password):
    driver = webdriver.Edge() 
    driver.get("https://roarmy.adlunap.ro")
    time.sleep(2)
 
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    time.sleep(5)
    print("Logged in (hopefully)")
    driver.quit()

def get_login_info():
    username_input = input("Write your username: ")
    password_input = input("Write your password: ")
    return username_input, password_input

user_data = get_login_info()
hw_scrape(user_data[0], user_data[1])