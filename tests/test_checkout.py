from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert products_page.is_loaded()

    products_page.add_item_to_cart()

    cart_page.open_cart()
    cart_page.proceed_to_checkout()

    checkout_page.fill_information("Test", "User", "12345")

    checkout_page.finish_checkout()
    assert checkout_page.is_order_complete()
