from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWait():
    def test(self):
        URL = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        driver.implicitly_wait(.5)
        driver.maximize_window()
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

        #Try to click on the NonStop checkbox
        #driver.find_element(By.XPATH, "//label/span[@data-test-id='stops-0-label']//parent::label//parent::div//parent::div//input").click()


        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//label/span[@data-test-id='stops-0-label']//parent::label//parent::div//parent::div//input")))
        element.click()

        time.sleep(5)
        driver.quit()

object1 = ExplicitWait()
object1.test()