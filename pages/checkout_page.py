from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.confirmation_header = (By.CLASS_NAME, "complete-header")

    def fill_information(self, first, last, postal):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_button).click()

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()

    def is_order_complete(self):
        return "Thank you" in self.driver.find_element(*self.confirmation_header).text
