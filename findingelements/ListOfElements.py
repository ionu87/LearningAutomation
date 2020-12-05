from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class ListOfElements():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)

        elementListByClassName = driver.find_elements(By.CLASS_NAME, 'inputs')
        elements = len(elementListByClassName)
        if elementListByClassName is not None:
            print(f'Size fo the list is: {elements}')

        elementListByTagName = driver.find_elements(By.TAG_NAME, 'input')
        tagElements = len(elementListByTagName)
        if elementListByTagName is not None:
            print(f'Size fo the list is: {tagElements}')

obj1 = ListOfElements()
obj1.test()