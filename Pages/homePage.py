from selenium.webdriver.common.by import By
from POMProjectDemo.Locators.locators import Locators

class HomePage():

    # creating a constructor and taking driver as an argument there after adding the objects with their element finder
    def __init__(self, driver):
        self.driver = driver;
        self.afterLogin_link_xpath = Locators.afterLogin_link_xpath
        self.logout_link_tagname = Locators.logout_link_tagname
    # (Actions/events) for clicking on the afterlogin button
    def afterlogin_link_click(self):
        self.driver.find_element(By.XPATH, self.afterLogin_link_xpath).click()

    # (Actions/events)for clicking on the logout button
    def logout_link_click(self):
        self.driver.find_element(By.TAG_NAME, self.logout_link_tagname).click()
