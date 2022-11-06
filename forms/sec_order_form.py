from forms.login_form import BasePage
from playwright.sync_api import Page, expect


class SecOrderForm(BasePage):
    def check_exists_price_of_item(self, page: Page):
        locator = page.locator(".inventory_item_price")
        expect(locator).to_be_visible()

    def check_exists_name_of_item(self, page: Page):
        locator = page.locator(".inventory_item_name")
        expect(locator).to_be_visible()

    def check_exists_details_of_item(self, page: Page):
        locator = page.locator(".inventory_item_desc")
        expect(locator).to_be_visible()

    def finish_btn(self, page: Page):
        finish_btn = page.locator('[id="finish"]')
        finish_btn.click()

    def check_title_form(self, page: Page):
        locator = page.get_by_title("class='title'")
        expect(locator).to_contain_text("Checkout: Overview")

    def cancel_button(self, page: Page):
        cancel_button = page.locator('[name="cancel"]')
        cancel_button.click()

    def exist_basket_icon(self, page: Page):
        locator = page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self, page: Page):
        locator = page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()
