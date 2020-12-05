from selenium import webdriver
import time
class BrowserInteractions():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        #Maximize browser window
        driver.maximize_window()
        #Open the URL
        driver.get(baseURL)
        #Get title
        title = driver.title
        print(f'The title of the browser is {title}')
        #Get current URL
        currentURL = driver.current_url
        print(f'The current URL is {currentURL}')
        #Browser refresh
        driver.refresh()
        print('browser refreshed 1 time.')
        #Another browser refresh
        driver.get(driver.current_url)
        print('Browser refreshed 2 time.')
        #Open anpther URl
        driver.get('https://letskodeit.teachable.com/')
        currentURL = driver.current_url
        print(f'The current URL is {currentURL}')
        #Browser back
        driver.back()
        print('Go 1 step back.')
        currentURL = driver.current_url
        print(f'The current URL is {currentURL}')

        #Browser forward
        driver.forward()
        print('Go one step forward.')
        currentURL = driver.current_url
        print(f'The current URL is {currentURL}')
        #Retrieve the page source
        source = driver.page_source
        print(source)
        # Close/quit browser
        #driver.close()
        driver.quit()

interaction1 = BrowserInteractions()
interaction1.test()