from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class RadioButtonsLists():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        radioButtons1 = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtons1)
        print(f'The size of the list is {size}')

        for radioButton in radioButtons1:
            isSelected = radioButton.is_selected()
            if not isSelected:
                radioButton.click()

radio1 = RadioButtonsLists()
radio1.test()