from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def fill_checkout_info(self, first, last, postal):
        self.enter_text(self.FIRST_NAME, first)
        self.enter_text(self.LAST_NAME, last)
        self.enter_text(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_element_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
