from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("https://www.flipkart.com")


    def test_flipkartScenario(self):
        driver=self.driver
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//span[text()='Enter Email/Mobile number']/ancestor::div/button").click()
        menu=driver.find_element_by_xpath("//span[contains(text(),'Electronics')]")
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Pixel 3a | 3a XL')]/parent::li").click()
        driver.find_element_by_xpath("//a[@rel='noopener noreferrer'])[1]").click()
        driver.switch_to.window(1)
        driver.find_element_by_xpath()


        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
