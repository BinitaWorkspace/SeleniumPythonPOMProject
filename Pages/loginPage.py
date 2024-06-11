from selenium.webdriver.common.by import By
from POMProjectDemo.Locators.locators import Locators

class LoginPage():

    # creating a constructor and taking driver as an argument there after adding the objects with their element finder
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.loginbutton_xpath = Locators.loginbutton_xpath
        self.invalidUsername_tagname =Locators.invalidUsername_tagname
    # Creating a function for entering the Username in textbox(Actions/events)
    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys("Admin")

    # Creating a function for entering the Password in textbox(Actions/events)
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys("admin123")

    # Creating a function for clicking on the Login Button(Actions/events)
    def click_login(self):
        self.driver.find_element(By.XPATH, self.loginbutton_xpath).click()
    #Invalid username check
    def check_invalidUserNameMessage(self):
        msg= self.driver.find_element(By.TAG_NAME, self.invalidUsername_tagname).text()
        return msg