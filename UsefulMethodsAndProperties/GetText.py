from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        openTab = driver.find_element(By.ID, 'opentab')
        element = openTab.text
        print(f'The name of the button is {element}')


text = GetText()
text.test()