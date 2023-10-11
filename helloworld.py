#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import LoginAndLogoutFunctions
import GeneraNavigation as GenNav

def initdriver():
    driver = webdriver.Firefox()
    return driver  

#Functions
def FollowPeople(AmountOfPeopleToFollow):
    time.sleep(random.randint(5, 15)) #sleep to not spam the system 
    #Intialise Elements\
    AllAvailablePeople = driver.find_elements(By.CLASS_NAME, "discover-entity-type-card__container-bottom")

    #Store Default Vars
    for i in range(AmountOfPeopleToFollow):
        PersonToFollow = AllAvailablePeople[i]
        FollowButton = PersonToFollow.find_element(By.CLASS_NAME, "artdeco-button")

        #Do Actions
        time.sleep(random.randint(1, 4))#sleep to not spam the sysytem
        FollowButton.click()    

#Set Some Defaults
URL = "https://www.linkedin.com/" 
Username = "pgfriendlyiggy@gmail.com"
Password = "ThisIsAPassword12345"
SearchTerm = "#Software"

#Main  
LoginAndLogoutFunctions.OpenWebPage(URL)    
time.sleep(random.randint(1, 8))
LoginAndLogoutFunctions.Login(Username, Password)
GenNav.ClickOnTabNavbar("My Network")
FollowPeople(8)
#GenNav.Search(SearchTerm)
LoginAndLogoutFunctions.QuitWebPage()

