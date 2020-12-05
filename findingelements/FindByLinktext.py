from selenium import webdriver

class FindByLinkText():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        elementByLinktext = driver.find_element_by_link_text("Practice")
        if elementByLinktext is not None:
            print('Element by Link Text found.')

        elementByPartialLink = driver.find_element_by_partial_link_text("Log")
        if elementByPartialLink is not None:
            print('Element by partial Link Text found.')

obj1 = FindByLinkText()
obj1.test()