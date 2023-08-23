from .page import Page
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(Page):
    def find_element(self, xpath):
        return self.driver.find_element(by= AppiumBy.XPATH, value=xpath)
    def click_element(self,obj):
        obj.click()   
    def send_keys(self,obj, keys):
        obj.send_keys(keys)
    def quit(self):
        self.driver.quit()
    