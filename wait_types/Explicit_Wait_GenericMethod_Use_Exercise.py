from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.Explicit_Wait_GenericMethod_For_Future_Use import ExplicitWaitType
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitGeneral():
    def test(self):
        URL = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(URL)
        #driver.implicitly_wait(10)

        #Click on Flights button
        driver.find_element(By.XPATH, "//ul[@id='uitk-tabs-button-container']/li[2]/a[@role='tab']").click()

        #Click on the Leaving From element
        driver.find_element(By.XPATH, "//button[@data-stid='location-field-leg1-origin-menu-trigger']").click()
        driver.find_element(By.XPATH, "//input[@placeholder='Where are you leaving from?']").send_keys('Chicago')
        #Find the drop-down xpath and click on the first value
        driver.find_element(By.XPATH, "(//div[@class='uitk-typeahead-button-label uitk-type-medium uitk-type-300 truncate'])[1]").click()

        # Click on the Going To element
        driver.find_element(By.XPATH, "//button[@data-stid='location-field-leg1-destination-menu-trigger']").click()
        driver.find_element(By.ID, 'location-field-leg1-destination').send_keys('New York')
        # Find the drop-down xpath and click on the first value
        driver.find_element(By.XPATH, "//button[@data-stid='location-field-leg1-destination-result-item-button']").click()
        driver.find_element(By.XPATH, "//button[@data-testid='submit-button']").click()

        element = wait.waitForElement(By.NAME, "searchButton")
        element.click()

        time.sleep(5)
        driver.quit()


object1 = ExplicitWaitGeneral()
object1.test()