import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from POMProjectDemo.Pages.loginPage import LoginPage
from POMProjectDemo.Pages.homePage import HomePage
from POMProjectDemo.Locators.locators import Locators


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test01_login_valid(self):
        driver = self.driver
        url = driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        # Creating an object for the  home page
        homepage = HomePage(driver)
        homepage.afterlogin_link_click()
        homepage.logout_link_click()
        time.sleep(2)

    def test02_login_invalid_username(self):
        driver = self.driver
        url = driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message= login.invalidUsername_tagname("p").text
        self.assertEqual(message,"Invalid credentials123")

    @classmethod
    def tearDownClass(td):
        td.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='E:/Projects/Selenium/SeleniumPython/SeleniumPythonPOMProject/POMProjectDemo/reports'))
