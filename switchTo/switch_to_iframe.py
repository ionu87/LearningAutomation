from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchWindow():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.execute_script("window.scrollBy(0, 1000);")

        #Switch to frame using Id
        driver.switch_to.frame('courses-iframe')

        #Switch to frame using name
        #driver.switch_to.frame('iframe-name')

        #Switch to frame using numbers
        #driver.switch_to.frame(0)

        time.sleep(5)
        #Search course
        searchBox = driver.find_element(By.ID, 'search-courses')
        searchBox.send_keys('python')
        time.sleep(5)

        #Switch back to the parent handle(main page)
        driver.switch_to.default_content()

        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(5)
        smth = driver.find_element(By.ID, 'name')
        smth.send_keys('python')
        time.sleep(5)




chromeBrowser = SwitchWindow()
chromeBrowser.test()