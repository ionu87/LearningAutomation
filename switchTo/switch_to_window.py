from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchWindow():
    def test(self):
        URL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

        #Find parent of the main window
        parentHandle = driver.current_window_handle
        print(f'Parent handle is: {parentHandle}')

        #Find Oen Window button anc clik it
        driver.find_element(By.ID, 'openwindow').click()
        time.sleep(5)

        #Find all handles, there should be two after clicking on the Open Window button
        handles = driver.window_handles

        #Switch to the second windwo anc search for a course
        for handle in handles:
            print(f'Handle: {handle}')
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print('Switched to the second window.')
                searchBox = driver.find_element(By.ID, 'search-courses')
                searchBox.send_keys('python')
                time.sleep(5)
                driver.close()   #Don;t close this window if you want to switch again to the second window
                break

        #Switch back to the first window
        driver.switch_to.window(parentHandle)
        smth = driver.find_element(By.ID, 'name')
        smth.send_keys('python')
        time.sleep(5)

        # #Switch again to the second window
        # driver.switch_to.window(handle)
        # print('Switched to the second window')
        # time.sleep(5)



chromeBrowser = SwitchWindow()
chromeBrowser.test()