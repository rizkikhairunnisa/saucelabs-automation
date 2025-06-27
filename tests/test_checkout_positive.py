import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_success_checkout(driver):
    print("Step 1: Login")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)
    # ✅ Assert sudah masuk ke halaman product
    assert "inventory" in driver.current_url, "Login failed: Not redirected to inventory page"

    print("Step 2: Add to cart")
    product_page = ProductsPage(driver)
    product_page.add_item_to_cart()
    time.sleep(3)
    # ✅ Assert ikon cart berubah jadi '1'
    assert product_page.get_cart_badge_count() == "1", "Cart count should be 1 after adding product"

    print("Step 3: Go to cart")
    product_page.go_to_cart()
    time.sleep(3)
    # ✅ Assert halaman cart
    assert "cart" in driver.current_url, "Not on the cart page"

    print("Step 4: Proceed to checkout")
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()
    time.sleep(3)
    # ✅ Assert halaman checkout step one
    assert "checkout-step-one" in driver.current_url, "Not on the checkout step one page"

    print("Step 5: Fill checkout info")
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("Kiki", "QA", "12345")
    time.sleep(3)
    # ✅ Assert lanjut ke step two
    assert "checkout-step-two" in driver.current_url, "Checkout step one failed"

    print("Step 6: Finish checkout")
    checkout.finish_checkout()
    time.sleep(3)
    # ✅ Assert ke halaman selesai
    assert "checkout-complete" in driver.current_url, "Did not reach checkout complete page"

    print("Step 7: Validate success message")
    assert checkout.get_success_message() == "Thank you for your order!", "Success message not found"
