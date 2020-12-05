from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpath():
    def test(self):
        URL = 'https://letskodeit.teachable.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        #Login
        driver.find_element(By.LINK_TEXT, 'Login').click()
        driver.find_element(By.ID, 'user_email').send_keys('test@email.com')
        driver.find_element(By.ID, 'user_password').send_keys('abcabc')
        driver.find_element(By.NAME, 'commit').click()

        time.sleep(5)

        # Search for courses
        searchCourse = driver.find_element(By.ID, 'search-courses')
        searchCourse.send_keys('JavaScript')

        #Select course
        _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
        _courseLocator = _course.format('JavaScript for beginners')

        courseName = driver.find_element(By.XPATH, _courseLocator)
        courseName.click()

text = DynamicXpath()
text.test()