# Описать значок корзины, гет кол-ва товара, кнопки remove, checkout, continue shopping
from selenium.webdriver.common.by import By
from forms.login_form import BasePage
from selenium.common.exceptions import NoSuchElementException


class BasketFormElements:
    SHOPPING_CONT = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_COUNT = (By.CLASS_NAME, "cart_quantity")
    ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.ID, "item_4_title_link")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_BTN = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")


class BasketForm(BasePage):
    element = BasketFormElements

    def check_exists_basket(self):
        try:
            self.driver.find_element(*self.element.SHOPPING_CONT)
        except NoSuchElementException:
            return False
        return True

    def check_exists_item(self):
        try:
            self.driver.find_element(*self.element.ITEM)
        except NoSuchElementException:
            return False
        return True

    def click_basket(self):
        self.driver.find_element(*self.element.SHOPPING_CONT).click()

    def click_checkout(self):
        self.driver.find_element(*self.element.CHECKOUT).click()

    def click_remove_btn(self):
        self.driver.find_element(*self.element.REMOVE_BTN).click()

    def click_continue_btn(self):
        self.driver.find_element(*self.element.CONTINUE_BTN).click()

    def check_price(self):
        text = self.driver.find_element(*self.element.ITEM_PRICE).text.replace(" ", "")
        ord_c = list(i for i in text)
        return str(ord_c[-1])

    def go_card_item(self):
        self.driver.find_element(*self.element.ITEM_NAME).click()
