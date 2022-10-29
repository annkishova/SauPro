# Описать значок корзины, гет кол-ва товара, кнопки remove, checkout, continue shopping
from selenium.webdriver.common.by import By
from forms.login_form import BasePage
from selenium.common.exceptions import NoSuchElementException


class ShopFormElements:
    ADD_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRICE = (By.CLASS_NAME, "inventory_item_price")
    COUNT_CART = (By.CLASS_NAME, "shopping_cart_badge")


class ShopForm(BasePage):
    element = ShopFormElements

    def add_basket(self):
        self.driver.find_element(*self.element.ADD_CART).click()

    def check_exists_item_busket(self):
        try:
            self.driver.find_element(*self.element.COUNT_CART)
        except NoSuchElementException:
            return False
        return True

    def check_exists_item(self):
        try:
            self.driver.find_element(*self.element.ITEM_NAME)
        except NoSuchElementException:
            return False
        return True
