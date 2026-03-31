import pytest
import random
from PageObjects.LoginPage import LoginPage
from PageObjects.AddUserManagementPage import AddUserManagementPage
from utilities.readProperties import ReadConfig

@pytest.mark.regression
class Test_004_AddUserManagement:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()


    def test_AddUser(self, setup):
        driver = setup
        driver.get(self.baseURL)
        driver.maximize_window()

        email = f"prasad{random.randint(1000,9999)}@example.com"

        login_page = LoginPage(driver)
        login_page.setUserName(self.username)
        login_page.setPassword(self.password)
        login_page.clickSignInWithEmail()

        add_user_page = AddUserManagementPage(driver)
        add_user_page.open_add_User()

        add_user_page.fill_basic_info(
            Firstname="Prasad",
            Lastname="Reddy",
            Email=email,
            PhoneNumber="9876543210",
            Usertype="Admin",
            selectbuilding="Prasad"
        )

        add_user_page.click_create()

        print("Add User test passed successfully")
