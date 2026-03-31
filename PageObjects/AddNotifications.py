from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage


class AddNotificationsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ================= LOCATORS =================

    BTN_Notifications = (By.XPATH, "//span[normalize-space()='Notifications']")
    BTN_Add_Notifications = (
        By.XPATH,
        "//button[contains(normalize-space(), 'ADD NOTIFICATION') or contains(normalize-space(), 'Add Notification')]",
    )
    HDR_Add_Notification = (
        By.XPATH,
        "//div[@role='dialog']//h2["
        "contains(normalize-space(), 'Add Notification') or "
        "contains(normalize-space(), 'Add New Notification') or "
        "contains(normalize-space(), 'Notification')]",
    )

    # ---------- Basic Info -------
    TXT_Title = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'Title')]/following::input[1]")
    TXT_Message = (
        By.XPATH,
        "//div[@role='dialog']//label[contains(normalize-space(),'Message')]/following::textarea[1]"
        " | //div[@role='dialog']//label[contains(normalize-space(),'Message')]/following::input[1]",
    )
    DRP_Type = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'Type')]/following::*[@role='combobox'][1]")
    TXT_Type = (By.XPATH, "//div[@role='dialog']//label[contains(normalize-space(),'Type')]/following::input[1]")
    TXT_User_Id = (
        By.XPATH,
        "//div[@role='dialog']//label["
        "contains(normalize-space(),'User Id') or "
        "contains(normalize-space(),'User ID') or "
        "contains(normalize-space(),'UserId') or "
        "contains(normalize-space(),'User')]"
        "/following::input[1]",
    )

    BTN_ADD = (
        By.XPATH,
        "//div[@role='dialog']//button["
        "normalize-space()='CREATE' or normalize-space()='Create' or "
        "normalize-space()='ADD' or normalize-space()='Add']",
    )

    # ================= PAGE ACTIONS =================

    def open_add_notifications(self):
        self.click(self.BTN_Notifications)
        self.wait_visible(self.BTN_Add_Notifications)
        self.click(self.BTN_Add_Notifications)
        self.wait_visible(self.HDR_Add_Notification)
        self.wait_visible(self.TXT_Title)

    # -------------- BASIC INFO -----------

    def fill_basic_info(self, Title, Message, Type, UserId):
        self.type(self.TXT_Title, Title)
        self.type(self.TXT_Message, Message)
        self._set_notification_type(Type)
        self.type(self.TXT_User_Id, UserId)

    def click_create(self):
        self.click(self.BTN_ADD)

    def _set_notification_type(self, value):
        try:
            self.select_dropdown(self.DRP_Type, value)
        except TimeoutException:
            self.type(self.TXT_Type, value)




