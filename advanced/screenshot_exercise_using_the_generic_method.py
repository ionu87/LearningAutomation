from selenium import webdriver
from selenium.webdriver.common.by import By
from advanced.SaveScreenshots_GenericMethod_For_Future_Use import Screenshots2
import time


class TTT(Screenshots2):
    def test2(self):
        URL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        loginButton = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginButton.click()
        time.sleep(3)

        #Call the generic method for taking screenshots from the 'generic_methods_to_save_screenshots' module
        self.takeScreenshot(driver)

        driver.quit()

if __name__ == '__main__':
    chromeBrowser = TTT()
    chromeBrowser.test2()
    print(__name__)

