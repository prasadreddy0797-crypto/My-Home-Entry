from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PageObjects.BasePage import BasePage
import time


class AddBuildingPage(BasePage):

    # ================= LOCATORS =================

    BTN_BUILDING = (By.XPATH, "//span[normalize-space()='Buildings']")
    BTN_ADD_BUILDING = (By.XPATH, "//button[contains(.,'Add')]")

    # Basic Info
    TXT_BUILDING_NAME = (By.XPATH, "//label[contains(.,'Building Name')]/following::input[1]")
    TXT_ADDRESS = (By.XPATH, "//label[contains(.,'Address')]/following::input[1]")
    TXT_TOTAL_FLOORS = (By.XPATH, "//label[contains(.,'Total Floors')]/following::input[1]")
    TXT_TOTAL_UNITS = (By.XPATH, "//label[contains(.,'Total Units')]/following::input[1]")
    BTN_NEXT = (By.XPATH, "//button[normalize-space()='Next']")

    # Block
    BTN_ADD_BLOCK = (By.XPATH, "//button[contains(.,'Add Block')]")
    TXT_BLOCK_NAME = (By.XPATH, "//label[contains(.,'Block Name')]/following::input[1]")
    TXT_BLOCK_FLOORS = (By.XPATH, "//label[contains(.,'Floors')]/following::input[1]")

    # Facility
    BTN_ADD_FACILITY = (By.XPATH, "//button[normalize-space()='Add Facility']")
    DRP_TYPE = (By.XPATH,"//label[normalize-space()='Type']/following::*[@role='combobox'][1]" )
    TXT_NAME = (By.XPATH,"//label[normalize-space()='Name']/following::input[1]")
    DRP_STATUS = ( By.XPATH,"//label[normalize-space()='Status']/following::*[@role='combobox'][1]")
    TXT_CHARGE = (
        By.XPATH,"//div[@role='dialog']//label[normalize-space()='Charge']/following::input[not(@type='hidden')][1]")
    DRP_CHARGE_UNIT = (By.XPATH, "//label[contains(normalize-space(),'Charge Unit')]/following::*[@role='combobox'][1]")
    TXT_DESCRIPTION = (
        By.XPATH,
        "//label[contains(normalize-space(),'Description')]"
        "/following::input[not(@type='hidden')][1]"
        " | //label[contains(normalize-space(),'Description')]/following::textarea[1]")
    DRP_BOOKING_REQUIRED = (By.XPATH,"//label[contains(normalize-space(),'Booking')]/following::*[@role='combobox'][1]")
    TXT_SLOTS = (
        By.XPATH,"//div[@role='dialog']//label[contains(.,'Number of Slots')]/following::input[not(@type='hidden')][1]")
    BTN_NEXT = (By.XPATH, "//button[normalize-space()='Next']")
    BTN_ADD_SLOT = (
        By.XPATH,
        "//div[@role='dialog']//*[self::button or @role='button'][contains(normalize-space(.), 'ADD SLOT') or contains(normalize-space(.), 'Add Slot')]",
    )
    BTN_ADD_SLOT_ALT = (
        By.XPATH,
        "//div[@role='dialog']//*[contains(@class,'MuiButtonBase-root') and (contains(normalize-space(.), 'ADD SLOT') or contains(normalize-space(.), 'Add Slot'))]",
    )

    # Review
    BTN_FINAL_ADD = (By.XPATH, "//button[normalize-space()='Add']")

    # ================= PAGE ACTIONS =================

    def open_add_building(self):
        self.click(self.BTN_BUILDING)
        self.click(self.BTN_ADD_BUILDING)
        self.wait_visible(self.TXT_BUILDING_NAME)

    # ---------- BASIC INFO ----------
    def fill_basic_info(self, name, address, floors, units):
        self.type(self.TXT_BUILDING_NAME, name)
        self.type(self.TXT_ADDRESS, address)
        self.type(self.TXT_TOTAL_FLOORS, floors)
        self.type(self.TXT_TOTAL_UNITS, units)
        self.click(self.BTN_NEXT)

    # ---------- BLOCK ----------
    def add_block(self, block_name, floors):
        self.click(self.BTN_ADD_BLOCK)
        self.type(self.TXT_BLOCK_NAME, block_name)
        self.type(self.TXT_BLOCK_FLOORS, floors)

        self.wait_clickable(self.BTN_NEXT)
        self.click(self.BTN_NEXT)

        self.wait_clickable(self.BTN_ADD_FACILITY)

    # ---------- FACILITY ----------
    def add_facility(self, type_name, name, status, charge,
                     unit, description, booking_required, slots):

        self.wait_clickable(self.BTN_ADD_FACILITY)
        self.click(self.BTN_ADD_FACILITY)

        # TYPE
        self.wait_visible(self.DRP_TYPE)
        self.select_dropdown(self.DRP_TYPE, type_name)

        # NAME
        self.wait_visible(self.TXT_NAME)
        self.type(self.TXT_NAME, name)

        # STATUS
        try:
            self.select_dropdown(self.DRP_STATUS, status)
        except:
            print("Status already selected or not clickable, skipping...")

        # CHARGE
        self.wait_visible(self.TXT_CHARGE)
        self.type(self.TXT_CHARGE, charge)
        time.sleep(2)

        # CHARGE UNIT
        self.wait_clickable(self.DRP_CHARGE_UNIT)
        self.select_dropdown(self.DRP_CHARGE_UNIT, unit)

        # DESCRIPTION
        self.type(self.TXT_DESCRIPTION, description)

        # BOOKING REQUIRED
        try:
            self.select_dropdown(self.DRP_BOOKING_REQUIRED, booking_required)
        except:
            print("Booking already selected or not clickable, skipping...")

        # SLOTS
        self.type(self.TXT_SLOTS, slots)

        self.click_add_slot()

        self.wait_clickable(self.BTN_NEXT)
        self.click(self.BTN_NEXT)

    def submit_building(self):
        self.wait_clickable(self.BTN_FINAL_ADD)
        self.click(self.BTN_FINAL_ADD)

    def click_add_slot(self):
        for locator in (self.BTN_ADD_SLOT, self.BTN_ADD_SLOT_ALT):
            try:
                element = self.wait.until(EC.visibility_of_element_located(locator))
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", element
                )
                self.driver.execute_script("arguments[0].click();", element)
                return
            except TimeoutException:
                continue

        raise TimeoutException("Add Slot control was not found in the facility dialog.")
