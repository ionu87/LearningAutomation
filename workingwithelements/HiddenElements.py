from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HiddenElements():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        #Find the state of the text box
        textBox = driver.find_element(By.ID, 'displayed-text')
        tB1 = textBox.is_displayed()
        print(f'Text box is {tB1}')

        #Click the Hide button
        driver.find_element(By.ID, 'hide-textbox').click()
        time.sleep(2)

        #Find the state of the text box
        tB1 = textBox.is_displayed()
        print(f'Text box is {tB1}')

        #Click the Show button
        driver.find_element(By.ID, 'show-textbox').click()
        time.sleep(2)

        #Find the state of the text box
        tB1 = textBox.is_displayed()
        print(f'Text box is {tB1}')
        time.sleep(2)

        #Browser close
        driver.quit()

    def testExpedia(self):
        URL = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        #The element is not visible, the test should fail
        el = driver.find_element(By.ID, 'd2-btn')
        print(f'Element is visible {el.is_displayed()}')

hidden = HiddenElements()
hidden.test()
hidden.testExpedia()