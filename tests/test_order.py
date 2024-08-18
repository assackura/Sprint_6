import pytest
import allure

from data import OrderData, Urls
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверяем заказ')
    @allure.description('Проверяем позитивный сценарий заказа с двумя разными наборами данных')
    @pytest.mark.parametrize(OrderData.parametrs, OrderData.value)
    def test_new_order(self, driver, firstname, secondname, address, subway, phone, date, period, color, comment):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE)
        order_page.fill_form_order(firstname, secondname, address, OrderPageLocators.BUTTON_SUBWAY[subway], phone, date, OrderPageLocators.DROP_MENU_PERIOD[period], OrderPageLocators.CHECKBOX_COLOR_SCOOTER[color], comment)

        assert 'Заказ оформлен' in order_page.get_complited_text()