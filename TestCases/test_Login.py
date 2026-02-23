import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # -----------------------------
    # Test Home Page Title
    # -----------------------------
    def test_homepagetitle(self, setup):

        self.logger.info("******* Test_001_Login ******")
        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title
        assert act_title == "My Home Entry System"



    # -----------------------------
    # Test Login
    # -----------------------------
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignInWithEmail()

        act_title = self.driver.title
        assert act_title == "My Home Entry System"

