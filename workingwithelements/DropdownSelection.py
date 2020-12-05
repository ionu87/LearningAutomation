from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropdownSelection():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        element1 = driver.find_element(By.ID, 'carselect')
        sel = Select(element1)
        sel.select_by_value('benz')
        print('Select Benz by value')
        time.sleep(2)

        sel.select_by_index(2)
        print('Select Honda by index')
        time.sleep(2)

        sel.select_by_visible_text('BMW')
        print('Select BMW by visible text')
        time.sleep(2)

        sel.select_by_index(2)
        print('Select Honda by index')

dropdown = DropdownSelection()
dropdown.test()