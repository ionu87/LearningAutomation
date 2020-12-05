from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PopUpWindow():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        driver.find_element(By.ID, 'name').send_keys('python')
        driver.find_element(By.ID, 'alertbtn').click()
        time.sleep(3)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)

        driver.find_element(By.ID, 'name').send_keys('python')
        driver.find_element(By.ID, 'confirmbtn').click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(3)

chromeBrowser = PopUpWindow()
chromeBrowser.test()