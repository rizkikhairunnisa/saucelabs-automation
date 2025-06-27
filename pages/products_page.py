from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    ITEM_ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def add_item_to_cart(self):
        self.click(self.ITEM_ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)
        
