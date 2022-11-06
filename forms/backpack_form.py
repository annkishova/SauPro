from forms.login_form import BasePage
from playwright.sync_api import Page, expect


class ItemForm(BasePage):
    def add_basket(self):
        add_backet = self.page.locator('[id="add-to-cart-sauce-labs-backpack"]')
        add_backet.click()

    def check_exists_price_of_item(self, page: Page):
        locator = page.locator(".inventory_details_price")
        expect(locator).to_be_visible()

    def check_exists_name_of_item(self, page: Page):
        locator = page.locator(".inventory_details_name")
        expect(locator).to_be_visible()

    def check_exists_details_of_item(self, page: Page):
        locator = page.locator(".inventory_details_desc")
        expect(locator).to_be_visible()

    def check_exists_image_of_item(self, page: Page):
        locator = page.locator(".inventory_details_img")
        expect(locator).to_be_visible()

    def exist_basket_icon(self, page: Page):
        locator = page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self, page: Page):
        locator = page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()