from selenium import webdriver

class FindByIdName():
    def test(self):
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        elementById = driver.find_element_by_id('name')
        if elementById is not None:
            print('Element by ID found.')

        elementByName = driver.find_element_by_name('show-hide')
        if elementByName is not None:
            print('Element by name found.')

        driver.get("https://www.facebook.com/")
        #Search for an id that does not exist. This test will fail
        elementById2 = driver.find_element_by_id('passs')
        if elementById2 is not None:
            print('Element by Id found')
        else:
            print('Element by Id not found.')
obj1 = FindByIdName()
obj1.test()