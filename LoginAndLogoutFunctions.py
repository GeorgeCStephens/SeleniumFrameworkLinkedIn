#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
driver = webdriver.Firefox() 

def OpenWebPage(URL): driver.get(URL)

def QuitWebPage(): driver.quit()

def Login(Username, Password):
    #Intialise Elements
    UsernameInput = driver.find_element(By.ID, "session_key")
    PasswordInput = driver.find_element(By.ID, "session_password")

    #Input Text and Click "Sign In"
    time.sleep(random.randint(1, 8)) #sleep to not spam the sysytem
    UsernameInput.send_keys(Username)
    time.sleep(random.randint(1, 8))
    PasswordInput.send_keys(Password)
    time.sleep(random.randint(1, 8))
    PasswordInput.send_keys(Keys.RETURN)