from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    textbox_username_xpath = "//input[@id='email']"
    textbox_password_xpath = "//input[@id='password']"
    button_signin_xpath = "//button[@type='submit']"
    link_logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def textbox_username(self):
        return By.XPATH, self.textbox_username_xpath

    @property
    def textbox_password(self):
        return By.XPATH, self.textbox_password_xpath

    @property
    def button_signin(self):
        return By.XPATH, self.button_signin_xpath

    def setUserName(self, username):
        self.type(self.textbox_username, username)

    def setPassword(self, password):
        self.type(self.textbox_password, password)

    def clickSignInWithEmail(self):
        self.click(self.button_signin)

    def clickLogin(self):
        self.clickSignInWithEmail()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

