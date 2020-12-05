from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def test(self):
        URL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        loginButton = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginButton.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys('ionut@pop.com')

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys('Password')

        emailField.clear()
        passwordField.clear()

        emailField.send_keys('test')
        passwordField.send_keys('s')
        
chromeBrowser = ClickAndSendKeys()
chromeBrowser.test()