from selenium.webdriver.common.by import By
from utils.driver_utils import wait_for_element

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = (By.ID, "inventory_container")

    def is_loaded(self):
        return wait_for_element(self.driver, self.inventory_container).is_displayed()

    def add_item_to_cart(self, item_id="add-to-cart-sauce-labs-backpack"):
        self.driver.find_element(By.ID, item_id).click()
