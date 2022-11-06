from forms.login_form import BasePage
from playwright.sync_api import Page, expect


class FirstOrderForm(BasePage):
    def continue_btn(self, page: Page):
        continue_btn = page.locator('[id="continue"]')
        continue_btn.click()

    def check_title_form(self, page: Page):
        locator = page.get_by_title("class='title'")
        expect(locator).to_contain_text("Checkout: Your Information")

    def cancel_button(self, page: Page):
        cancel_button = page.locator('[name="cancel"]')
        cancel_button.click()

    def fill_first_name(self, page: Page, first_name: str):
        fill_first_name = page.locator('[id="first-name"]')
        fill_first_name.fill(first_name)

    def fill_last_name(self, page: Page, last_name: str):
        fill_last_name = page.locator('[id="last-name"]')
        fill_last_name.fill(last_name)

    def fill_postal_code(self, page: Page, postal_code: str):
        fill_postal_code = page.locator('[id="postal-code"]')
        fill_postal_code.fill(postal_code)

    def check_exists_error(self, page: Page):
        locator = page.locator(".error-message-container")
        expect(locator).to_contain_text("Error: First Name is required")

    def exist_basket_icon(self, page: Page):
        locator = page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self, page: Page):
        locator = page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()
