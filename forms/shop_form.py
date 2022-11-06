from forms.login_form import BasePage
from playwright.sync_api import Page, expect


class ShopForm(BasePage):
    def add_basket(self):
        add_backet = self.page.locator('[id="add-to-cart-sauce-labs-backpack"]')
        add_backet.click()

    def check_exists_item_bucket(self, page: Page):
        locator = page.locator(".shopping_cart_badge")
        expect(locator).to_be_visible()

    def check_exists_item(self, page: Page):
        locator = page.locator(".inventory_item_name")
        expect(locator).to_be_visible()

    def exist_basket_icon(self, page: Page):
        locator = page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self, page: Page):
        locator = page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()