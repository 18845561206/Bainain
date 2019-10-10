from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,feature,timeout=10,poll=1):
        element = WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*feature))
        return element
    def find_elements(self,feature,timeout=10,poll=1):
        element = WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*feature))
        return element
    def click(self,feature):
        self.find_element(feature).click()
    def input(self,feature,text):
        self.find_element(feature).send_keys(text)