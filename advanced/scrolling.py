from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScrollinElement():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        #Scroll down (parameter1: 0 is for scvrolling vertically, parameter 3 is the pixel size)
        driver.execute_script("window.scrollBy(0, 1000);")
        print('Scrolled down')
        time.sleep(7)

        #Scroll uo
        driver.execute_script("window.scrollBy(0, -1000);")
        print('Scrolled up')
        time.sleep(7)

        #Scroll element into view
        element = driver.find_element(By.ID, 'mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print('Scrolled into view')
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, -150);")
        print('Scrolled to the button')

        #Native way to sctoll element into view
        driver.execute_script("window.scrollBy(0, -1000);")
        print('Scrolled up')
        location = element.location_once_scrolled_into_view
        print('Scrolled into view again')
        print(location)



chromeBrowser = ScrollinElement()
chromeBrowser.test()