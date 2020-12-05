from selenium import webdriver

class RunnFFTests():
    def testMethod(self):
        #driver = webdriver.Firefox(executable_path="/Users/ip/AutomationWithPython/drivers/geckodriver")
        driver = webdriver.Firefox()
        driver.get("http://google.com")

test1 = RunnFFTests()
test1.testMethod()