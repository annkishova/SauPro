from forms.login_form import LoginForm
from utils.constants import Url
from playwright.sync_api import Page, expect


def test_authorization_succesfull_authorization(page: Page):
    page.goto(Url.login_url)
    login_form = LoginForm(page)
    login_form.fill_login_and_enter()
    #current_url = page.url
    expect(page).to_have_url(Url.main_page_url)
