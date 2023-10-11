#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
driver = webdriver.Firefox() 

def Search(SearchTerm):
    time.sleep(random.randint(1, 8)) #sleep to not spam the system
    #Intialise Elements
    SearchBar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")

    #Do Actions
    SearchBar.send_keys(SearchTerm)
    time.sleep(random.randint(1, 8))
    SearchBar.send_keys(Keys.RETURN)

def ClickOnTabNavbar(TabToSelect):
    time.sleep(random.randint(5, 15)) #sleep to not spam the system 
     #Intialise Elements\
    TopNavBar = driver.find_elements(By.CLASS_NAME, "global-nav__primary-link")
    
    #Store Default Vars
    TabsAvailable = ["Home", "My Network", "Jobs", "Messaging", "Notifications"]
    print(TabsAvailable.index(TabToSelect))
    MyNetworkButton = TopNavBar[TabsAvailable.index(TabToSelect)]

    #Do Actions
    time.sleep(random.randint(1, 8))#sleep to not spam the sysytem
    MyNetworkButton.click()