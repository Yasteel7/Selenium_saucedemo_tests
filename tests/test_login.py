from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_login_correct(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert products_page.is_loaded()

def test_login_incorrect_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user", "secret_sauce")

    assert "Username and password do not match" in login_page.get_error_message()

def test_login_incorrect_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "wrong_pass")

    assert "Username and password do not match" in login_page.get_error_message()

def test_login_both_incorrect(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user", "wrong_pass")

    assert "Username and password do not match" in login_page.get_error_message()
