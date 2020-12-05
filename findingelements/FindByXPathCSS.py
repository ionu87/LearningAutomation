from selenium import webdriver

class FindByXPathCSS():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        elementByXPATH = driver.find_element_by_xpath("//input[@id='name']")
        if elementByXPATH is not None:
            print('Element by Xpath found.')

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")
        if elementByCSS is not None:
            print('Element by CSS selecter found.')

obj1 = FindByXPathCSS()
obj1.test()