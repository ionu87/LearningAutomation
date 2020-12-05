from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class RadioButtonsAndCheckboxes():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        bmw = driver.find_element(By.ID, 'bmwradio')
        bmw.click()
        bmwState = bmw.is_selected()
        print(f'The BMW radio button is {bmwState}')

        time.sleep(1)

        benz = driver.find_element(By.ID, 'benzradio')
        benz.click()
        benzState = benz.is_selected()
        print(f'The Benz radio button is {benzState}')
        time.sleep(1)

        bmwcheck = driver.find_element(By.ID, 'bmwcheck')
        bmwcheck.click()
        bmwState = bmwcheck.is_selected()
        print(f'The BMW checkbox button is {bmwState}')

        time.sleep(1)

        benzcheck = driver.find_element(By.ID, 'benzcheck')
        benzcheck.click()
        benzState = benzcheck.is_selected()
        print(f'The Benz checkbox button is {benzState}')

        time.sleep(1)

element1 = RadioButtonsAndCheckboxes()
element1.test()