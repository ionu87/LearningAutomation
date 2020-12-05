from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWait():
    def test(self):
        URL = 'https://letskodeit.teachable.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//a[contains(@href,'/sign_in')]")
        loginLink.click()

        emailField = driver.find_element(By.ID, 'user_email')
        emailField.send_keys('test@email.com')

        passwordField = driver.find_element(By.ID, 'user_password')
        passwordField.send_keys('abcabc')

        loginButton = driver.find_element(By.NAME, 'commit')
        loginButton.click()

object = ImplicitWait()
object.test()