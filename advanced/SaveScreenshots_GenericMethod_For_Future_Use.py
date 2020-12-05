from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Screenshots2():
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
        passwordField.send_keys('Passwordddd')

        driver.find_element(By.NAME, 'commit').click()

        #Call the generif method for taking screenshots created below
        self.takeScreenshot(driver)

    #Define generic method for taking screenshots
    def takeScreenshot(self, driver):
        fileName = str(round(time.time() * 1000)) + '.png'
        screenshotDestination2 = "/Users/ip/Desktop/"
        destinationFile = screenshotDestination2 + fileName

        try:
            driver.save_screenshot(destinationFile)
            print(f'Screenshot saved at: {destinationFile}')
        except NotADirectoryError:
            print('Not a directory issue.')


if __name__ == '__main__':
    chromeBrowser = Screenshots2()
    chromeBrowser.test()
    print(__name__)

