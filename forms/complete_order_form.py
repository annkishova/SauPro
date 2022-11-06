from forms.login_form import BasePage
from playwright.sync_api import Page, expect


class CompleteOrderForm(BasePage):
    def add_basket(self):
        back_home_btn = self.page.locator('[id="back-to-products"]')
        back_home_btn.click()

    def check_image_pony(self, page: Page):
        locator = page.locator(".pony_express")
        expect(locator).to_be_visible()

    def check_title_form(self, page: Page):
        locator = page.get_by_title("class='title'")
        expect(locator).to_contain_text("Checkout: Complete!")

    def exist_basket_icon(self, page: Page):
        locator = page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self, page: Page):
        locator = page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()
