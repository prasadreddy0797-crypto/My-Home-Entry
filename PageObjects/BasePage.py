import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)

        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(lambda driver: self._is_editable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].focus();", element)

        try:
            element.clear()
            element.send_keys(value)
        except ElementNotInteractableException:
            self.driver.execute_script("arguments[0].value = '';", element)
            self.driver.execute_script(
                "arguments[0].value = arguments[1];"
                "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));"
                "arguments[0].dispatchEvent(new Event('change', { bubbles: true }));",
                element,
                value,
            )

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def _is_editable(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed() and element.is_enabled() and not element.get_attribute("readonly")

    def select_dropdown(self, locator, visible_text):
        # Open dropdown
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        current_value = (element.text or element.get_attribute("value") or "").strip()
        if current_value == visible_text:
            return

        self.click(locator)
        option = self._find_dropdown_option(visible_text)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)

        try:
            option.click()
        except ElementNotInteractableException:
            self.driver.execute_script("arguments[0].click();", option)

        self._close_open_listbox()

    def _close_open_listbox(self):
        try:
            self.wait.until_not(
                EC.presence_of_element_located((By.XPATH, "//*[@role='listbox']"))
            )
        except TimeoutException:
            active = self.driver.switch_to.active_element
            active.send_keys(Keys.ESCAPE)
            self.wait.until_not(
                EC.presence_of_element_located((By.XPATH, "//*[@role='listbox']"))
            )

    def _find_dropdown_option(self, visible_text):
        exact_option = (
            By.XPATH,
            "//div[contains(@class,'MuiPopover-root') or contains(@class,'MuiMenu-paper') or @role='presentation']"
            "//*[(@role='option' or @role='menuitem' or self::li) and normalize-space()=\"%s\"]"
            % visible_text,
        )
        partial_option = (
            By.XPATH,
            "//div[contains(@class,'MuiPopover-root') or contains(@class,'MuiMenu-paper') or @role='presentation']"
            "//*[(@role='option' or @role='menuitem' or self::li) and contains(normalize-space(), \"%s\")]"
            % visible_text,
        )

        try:
            return self.wait.until(EC.visibility_of_element_located(exact_option))
        except TimeoutException:
            return self.wait.until(EC.visibility_of_element_located(partial_option))
