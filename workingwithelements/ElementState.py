from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class ElementState():
    def isEnabled(self):
        URL = 'https://www.emag.ro/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        element1 = driver.find_element(By.ID, 'searchboxTrigger')
        e1State = element1.is_enabled() #True of False
        print(f'The search field is {e1State}')
        element1.send_keys('hello')

chromePage = ElementState()
chromePage.isEnabled()