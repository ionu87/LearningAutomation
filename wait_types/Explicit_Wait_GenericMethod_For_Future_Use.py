from traceback import print_stack
from UsefulMethodsAndProperties.handy_wrapper_to_find_elements import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitType():
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def waitForElement(self, locatorType='id',
                       timeout=10):
        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print(f"Waiting for maximum {timeout} for the element to be clickable.")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "searchButton")))
            print("Element appeared  on the web page.")
        except:
            print("Element not on the web page.")
            print_stack()
        return element


# obj1 = ExplicitWaitType()
# obj1.waitForElement()

