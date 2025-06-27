import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_missing_first_name(driver):
    print("Step 1: Login")
    LoginPage(driver).login("standard_user", "secret_sauce")
    time.sleep(1)

    print("Step 2: Add product and go to cart")
    product_page = ProductsPage(driver)
    product_page.add_item_to_cart()
    product_page.go_to_cart()
    time.sleep(1)

    print("Step 3: Checkout with empty first name")
    CartPage(driver).proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("", "QA", "12345")  # First name is missing
    time.sleep(1)

    # ✅ Assert: error message should appear
    assert checkout.get_error_message() == "Error: First Name is required"


def test_checkout_missing_last_name(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    product_page = ProductsPage(driver)
    product_page.add_item_to_cart()
    product_page.go_to_cart()
    CartPage(driver).proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("Kiki", "", "12345")  # Last name is missing
    time.sleep(1)
    assert checkout.get_error_message() == "Error: Last Name is required"


def test_checkout_missing_zip_code(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    product_page = ProductsPage(driver)
    product_page.add_item_to_cart()
    product_page.go_to_cart()
    CartPage(driver).proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("Kiki", "QA", "")  # Zip code is missing
    time.sleep(1)
    assert checkout.get_error_message() == "Error: Postal Code is required"
