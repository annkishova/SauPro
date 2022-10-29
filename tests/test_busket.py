from forms.basket_form import BasketForm
from forms.shop_form import ShopForm
from utils.constants import Url


class TestBasket:
    def test_open_basket(self, fill_login_and_enter):
        #Авторизация
        driver = fill_login_and_enter
        basket_form = BasketForm(driver)
        assert basket_form.check_exists_basket(), "Корзина не отображается"
        basket_form.click_basket()
        current_url = driver.current_url
        assert Url.basket_page_url == current_url, "Форма корзины не открылась"

    # Тест на добавление в корзину + проверка описания и цены + переход в карточку товара
    def test_add_to_basket(self, fill_login_and_enter):
        #Авторизация
        driver = fill_login_and_enter
        shop_form = ShopForm(driver)
        shop_form.add_basket()
        assert shop_form.check_exists_item_busket(), "Товар не добавлен в корзину"
        assert shop_form.check_exists_item(), "В корзине пусто"
        basket_form = BasketForm(driver)
        price_card = basket_form.check_price()
        basket_form.click_basket()
        price_basket = basket_form.check_price()
        assert price_card == price_basket, "Цена товара в корзине и осн странице разные"
        basket_form.go_card_item()
        current_url = driver.current_url
        assert Url.basket_page_url != current_url, "Не выполнен переход к карточке товара"

    def test_check_price(self, fill_login_and_enter):
        #Авторизация
        driver = fill_login_and_enter
        shop_form = ShopForm(driver)
        shop_form.add_basket()
        basket_form = BasketForm(driver)
        price_card = basket_form.check_price()
        basket_form.click_basket()
        price_basket = basket_form.check_price()
        assert price_card == price_basket, "Цена товара в корзине и осн странице разные"

    def test_go_to_item_card(self, fill_login_and_enter):
        #Авторизация
        driver = fill_login_and_enter
        shop_form = ShopForm(driver)
        shop_form.add_basket()
        basket_form = BasketForm(driver)
        basket_form.click_basket()
        basket_form.go_card_item()
        current_url = driver.current_url
        assert Url.basket_page_url != current_url, "Не выполнен переход к карточке товара"

    # Тест на удаление из корзины
    def test_delete_item_from_basket(self, fill_login_and_enter):
        #Авторизация
        driver = fill_login_and_enter
        shop_form = ShopForm(driver)
        shop_form.add_basket()
        basket_form = BasketForm(driver)
        basket_form.click_basket()
        assert basket_form.check_exists_item(), "В корзине нет товаров"
        basket_form.click_remove_btn()
        assert not basket_form.check_exists_item(), "В корзине есть товары"

    #Тест на переход из корзины к оформлению заказа
    def test_checkout_from_basket(self, fill_login_and_enter):
        #Авторизация
        driver = fill_login_and_enter
        basket_form = BasketForm(driver)
        basket_form.click_basket()
        current_url = driver.current_url
        basket_form.click_checkout()
        assert Url.checkout != current_url, "Не выполнен переход к оформлению заказа"

    # Продолжение шопинга
    def test_continue_shopping(self, fill_login_and_enter):
        #Авторизация
        driver = fill_login_and_enter
        basket_form = BasketForm(driver)
        basket_form.click_basket()
        current_url = driver.current_url
        basket_form.click_continue_btn()
        assert Url.main_page_url != current_url, "Не работает переход к продолжению покупок"
