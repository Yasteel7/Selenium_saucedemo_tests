from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")

    def open_cart(self):
        self.driver.find_element(*self.cart_link).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
