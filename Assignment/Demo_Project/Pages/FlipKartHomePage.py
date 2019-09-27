from Demo_Project.Locators import FlipKartLocators
class FlipKartHomePage:

    def __init__(self, driver):
        self.driver = driver

    def clickByXpath(self,locator):
        self.driver.find_element_by_xpath(locator).click()


