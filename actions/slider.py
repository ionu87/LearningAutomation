from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Slider():
    def test(self):
        URL = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        slider = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(3)
        try:
            actions =ActionChains(driver)
            actions.drag_and_drop_by_offset(slider, 100, 0).perform()  #100 is horizontal and 0 si vertical
            print('Slide element successful')
            time.sleep(4)
        except:
            print('Slide element failed')


obj1 = Slider()
obj1.test()