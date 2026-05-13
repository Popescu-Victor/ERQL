from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import dotenv
import os


def load_env_variables():

    dotenv.load_dotenv()
    LOGIN_URL = os.getenv("LOGIN_URL")
    HW_PAGE = os.getenv("HW_PAGE")

    return LOGIN_URL, HW_PAGE


def hw_scrape(username, password):
    load_env_variables()
    LOGIN_URL, HW_PAGE = load_env_variables()

    driver = webdriver.Edge() 
    driver.get(LOGIN_URL)
    time.sleep(2)
 
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    time.sleep(5)
    print("Logged in (hopefully)")

    driver.get(HW_PAGE)
    time.sleep(5)

    print("Navigated to HW page")

    urls = [
    link.get_attribute("href")
    for link in driver.find_elements(By.TAG_NAME, "a")
    if link.get_attribute("href")
]
    print("Extracted URLs:")
    for url in urls:
        print(url)  

    driver.quit()



def get_login_info():
    username_input = input("Write your username: ")
    password_input = input("Write your password: ")
    return username_input, password_input

user_data = get_login_info()
hw_scrape(user_data[0], user_data[1])