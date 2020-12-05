from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from UsefulMethodsAndProperties.handy_wrapper_to_find_elements import HandyWrappers

class UsingWrappers():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)

        textField = hw.getElement('name')



        textField.send_keys('text')
        time.sleep(3)

        textField2 = hw.getElement("//input[@id='name']", locatorType='xpath')
        textField2.clear()
        time.sleep(5)

text = UsingWrappers()
text.test()