from selenium import webdriver
import time

class SafariBrowser():
    def safaritest(self):
        driver = webdriver.Safari()
        driver.get('http://www.google.com')
        time.sleep(20)

safariObject = SafariBrowser()
safariObject.safaritest()