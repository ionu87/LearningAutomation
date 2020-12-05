from selenium import webdriver
import time

class RunChromeTest():
    def chromeTest(self):
        #driver = webdriver.Chrome(executable_path="/Users/ip/AutomationWithPython/drivers/chromedriver")
        driver = webdriver.Chrome()
        driver.get("http://www.google.com")
        time.sleep(20)
test1 = RunChromeTest()
test1.chromeTest()