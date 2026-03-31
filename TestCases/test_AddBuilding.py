import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.LoginPage import LoginPage
from PageObjects.AddBuildingPage import AddBuildingPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddBuilding:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_AddBuilding(self, setup):

        self.logger.info("********** Test_003_AddBuilding Started **********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        try:
            # ================= LOGIN =================
            self.logger.info("Logging into application...")

            login_page = LoginPage(self.driver)
            login_page.setUserName(self.username)
            login_page.setPassword(self.password)
            login_page.clickSignInWithEmail()

            # WAIT FOR DASHBOARD
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[normalize-space()='Buildings']")
                )
            )

            self.logger.info("Login successful")

            # ================= OPEN ADD BUILDING =================
            add = AddBuildingPage(self.driver)

            add.open_add_building()

            add.fill_basic_info("Tower A", "Hyderabad", "10", "100")

            add.add_block("Block A", "5")

            add.add_facility(
                "Gym",
                "Gym Area",
                "Open",
                "100",
                "Hourly",
                "Gym Facility",
                "No",
                "50"
            )

            add.submit_building()
            self.logger.info("Building added successfully")

        except Exception as e:
            self.logger.error("Test Failed")
            self.logger.error(str(e))
            self.driver.save_screenshot(".\\Screenshots\\test_AddBuilding.png")
            assert False

        finally:
            self.driver.quit()