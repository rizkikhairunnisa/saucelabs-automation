from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
