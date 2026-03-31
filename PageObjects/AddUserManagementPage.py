from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from PageObjects.BasePage import BasePage


class AddUserManagementPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ================= LOCATORS =================

    # Navigation
    BTN_USERS = (By.XPATH, "//span[normalize-space()='Users']")
    BTN_Add_Users = (By.XPATH, "//button[contains(.,'ADD USER') or contains(.,'Add User')]")

    # Add User Page Title / Header
    BTN_ADD_USER = (By.XPATH, "//div[@role='dialog']//h2[normalize-space()='Add New User']")

    # -------- Basic Info -------
    TXT_First_Name = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'First Name')]/following::input[1]")
    TXT_Last_Name = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'Last Name')]/following::input[1]")
    TXT_Email = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'Email')]/following::input[1]")
    TXT_Phone_Number = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'Phone Number')]/following::input[1]")

    DRP_User_Type = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'User Type')]/following::*[@role='combobox'][1]")
    DRP_Select_Building = (By.XPATH, "//div[@role='dialog']//*[contains(normalize-space(),'Select Building')]/following::*[@role='combobox'][1]")

    BTN_Create = (By.XPATH, "//div[@role='dialog']//button[normalize-space()='CREATE' or normalize-space()='Create']")

    # ================= PAGE ACTIONS =================

    def open_add_User(self):
        self.click(self.BTN_USERS)
        self.click(self.BTN_Add_Users)
        self.wait_visible(self.BTN_ADD_USER)
        self.wait_visible(self.TXT_First_Name)

    # ---------- BASIC INFO ----------
    def fill_basic_info(self, Firstname, Lastname, Email, PhoneNumber, Usertype, selectbuilding):
        self.type(self.TXT_First_Name, Firstname)
        self.type(self.TXT_Last_Name, Lastname)
        self.type(self.TXT_Email, Email)
        self.type(self.TXT_Phone_Number, PhoneNumber)

        self.select_dropdown(self.DRP_User_Type, Usertype)
        self.select_dropdown_or_first(self.DRP_Select_Building, selectbuilding)

    def click_create(self):
        self.click(self.BTN_Create)

    def select_dropdown_or_first(self, locator, visible_text):
        element = self.wait_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

        try:
            option = self._find_dropdown_option(visible_text)
        except TimeoutException:
            option = self._first_dropdown_option()

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
        self.driver.execute_script("arguments[0].click();", option)
        self._close_open_listbox()

    def _first_dropdown_option(self):
        option_locator = (
            By.XPATH,
            "//div[contains(@class,'MuiPopover-root') or contains(@class,'MuiMenu-paper') or @role='presentation']"
            "//*[(@role='option' or @role='menuitem' or self::li)][normalize-space()][1]",
        )
        return self.wait_visible(option_locator)
