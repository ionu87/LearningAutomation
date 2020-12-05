from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class FindByDemo():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        elementById = driver.find_element(By.ID, 'name')
        elementById.send_keys('hello')
        time.sleep(10)
        if elementById is not None:
            print('Element by id found.')

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='name']")
        if elementByXpath is not None:
            print(f'Element by Xpath found.')

obj1 = FindByDemo()
obj1.test()