from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetAttribute():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, 'name')
        result = element.get_attribute('class')

        print(f'The name of the attribute is {result}')
        time.sleep(1)
        driver.quit()


text = GetAttribute()
text.test()