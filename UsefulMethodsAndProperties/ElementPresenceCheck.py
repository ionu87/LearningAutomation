from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from UsefulMethodsAndProperties.handy_wrapper_to_find_elements import HandyWrappers

class ElementPresence():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)

        elementResult = hw.isElementPresent('name', By.ID)
        print(str(elementResult))


        elementResult2 = hw.isElementPresent('//input[@id="name"]', By.XPATH)
        print(str(elementResult2))


text = ElementPresence()
text.test()