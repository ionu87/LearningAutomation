from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WindowSize():
    def test(self):
        URL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print(f'Height is {height}')
        print(f'Width is {width}')



chromeBrowser = WindowSize()
chromeBrowser.test()