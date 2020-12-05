from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():
    def test(self):
        URL = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        # Click on Flights button
        driver.find_element(By.XPATH, "//ul[@id='uitk-tabs-button-container']/li[2]/a[@role='tab']").click()

        #Click on Departing
        driver.find_element(By.XPATH, "//div[@class='uitk-flex uitk-flex-row uitk-flex-gap-three uitk-new-date-fields']/div[1]").click()
        time.sleep(5)

        #Select a date
        calendar = driver.find_element(By.XPATH, "/html//div[@id='wizard-flight-tab-roundtrip']/div/div[2]/div[@class='Dates']/div/div/div[1]/div/div[2]//div[@class='uitk-new-date-picker-menu-months-container']/div[1]/table[@class='uitk-new-date-picker-weeks']//tbody//tr//td//button")
        validDays = calendar.find_elements(By.TAG_NAME, 'data-day')
        print('Departure section found.')

        for date in validDays:
            if date == '1':
                date.click()
                break

        time.sleep(5)


        # #Click Done
        # driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']//span[1]").click()
        # time.sleep(5)

        driver.quit()

object1 = CalendarSelection()
object1.test()