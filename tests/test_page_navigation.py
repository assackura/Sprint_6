from data import Urls
import allure
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestPageNavigation:

    @allure.title('Проверяем переход на страницу заказа')
    @allure.description('Проверяем переход на страницу заказа по кнопке в шапке страницы')
    def test_input_order_page_click_to_up_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        button_next = main_page.click_order_button(BasePageLocators.UP_ORDER_BUTTON_MAIN_PAGE)

        assert button_next.text == 'Далее', 'Ожидаемый локатор не найден'

    @allure.title('Проверяем переход на страницу заказа')
    @allure.description('Проверяем переход на страницу заказа по кнопке внизу страницы')
    def test_input_order_page_click_to_down_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        button_next = main_page.click_order_button(MainPageLocators.DOWN_ORDER_BUTTON_MAIN_PAGE)

        assert button_next.text == 'Далее', 'Ожидаемый локатор не найден'

    @allure.title('Проверяем переход на главную страницу')
    @allure.description('Проверяем переход на главную страницу по клику на логотип самоката')
    def test_click_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE)

        assert order_page.click_logo_scooter().text == 'Заказать', 'Ожидаемый локатор не найден'

    @allure.title('Проверяем переход на страницу "Дзена"')
    @allure.description('Проверяем переход на страницу "Дзена" по клику на логотип Яндекс')
    def test_click_logo_yandex(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE)
        order_page.click_logo_yandex()

        current_url = order_page.wait_load_dzen_page()

        assert current_url == Urls.DZEN_PAGE, 'Ожидаемый локатор не найден'





