from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHovering():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(7)

        driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(3)
        element = driver.find_element(By.ID, 'mousehover')
        itemToClick = "//div[@class='mouse-hover-content']//a[text()='Top']"
        time.sleep(5)

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print('Mouse hovered on element')
            time.sleep(3)
            topButton = driver.find_element(By.XPATH, itemToClick)
            actions.move_to_element(topButton).click().perform()
            print('Item clicked')
        except:
            print('Mouse hover failed')

obj1 = MouseHovering()
obj1.test()