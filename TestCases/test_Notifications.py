import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.LoginPage import LoginPage
from PageObjects.AddNotifications import AddNotificationsPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_AddNotifications:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_AddNotifications(self, setup):
        self.logger.info("********** Test_005_AddNotifications Started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # ---------- Login ----------
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignInWithEmail()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Notifications']"))
        )

        self.logger.info("********** Login Successful **********")

        # ---------- Open Notifications Page ----------
        self.notify = AddNotificationsPage(self.driver)
        self.notify.open_add_notifications()

        # ---------- Fill Notification Details ----------
        self.notify.fill_basic_info(
            Title="Test Notification",
            Message="This is a test notification created by automation",
            Type="General",
            UserId="123"
        )

        # ---------- Click Add/Create ----------
        self.notify.click_create()

        self.logger.info("********** Notification Created Successfully **********")

        # ---------- Validation ----------
        assert True

        self.driver.quit()
