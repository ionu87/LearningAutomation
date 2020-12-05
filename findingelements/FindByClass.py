from selenium import webdriver
import time

class FindByClassTag():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        elementByClass = driver.find_element_by_class_name("displayed-class")
        elementByClass.send_keys('hello')
        time.sleep(10)
        if elementByClass is not None:
            print('Element by class found.')

        elementBytag = driver.find_element_by_tag_name("h1")
        text = elementBytag.text
        if elementBytag is not None:
            print(f'Element by tag found: {text}.')

obj1 = FindByClassTag()
obj1.test()