from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Demo_Project.Pages import FlipKartHomePage
from Demo_Project.Locators import FlipKartLocators

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        cls.driver.get("https://www.flipkart.com")


    def test_flipkartScenario(self):
        driver=self.driver()
        homepage=FlipKartHomePage(driver)
        homepage.

        driver.find_element_by_xpath("//span[text()='Enter Email/Mobile number']/ancestor::div/button").click()
        menu=driver.find_element_by_xpath("//span[contains(text(),'Electronics')]")
        ActionChains(driver).move_to_element(menu).perform()
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(text(),'Pixel 3a | 3a XL')]/parent::li").click()
        driver.find_element_by_xpath("(//a[@rel='noopener noreferrer'])[1]").click()
        driver.set_page_load_timeout(10)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        driver.find_element_by_xpath("//text()[contains(.,'ADD TO CART')]/ancestor::button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[text()='+']").click()
        price=driver.find_element_by_xpath("//div[contains(text(),'Total Payable')]/following-sibling::span").text
        amount=price.split('₹')
        print(amount[1])


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
