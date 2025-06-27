import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_success_checkout(driver):
    print("Step 1: Login")
    LoginPage(driver).login("standard_user", "secret_sauce")
    time.sleep(3)

    print("Step 2: Add to cart")
    product_page = ProductsPage(driver)
    product_page.add_item_to_cart()
    time.sleep(3)

    print("Step 3: Go to cart")
    product_page.go_to_cart()
    time.sleep(3)

    print("Step 4: Proceed to checkout")
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    time.sleep(3)

    print("Step 5: Fill checkout info")
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("Kiki", "QA", "12345")
    time.sleep(3)

    print("Step 6: Finish checkout")
    assert "checkout-step-two" in driver.current_url
    checkout.finish_checkout()
    time.sleep(3)

    print("Step 7: Validate success message")
    assert checkout.get_success_message() == "Thank you for your order!"
