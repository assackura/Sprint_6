import allure
from selenium.webdriver import Keys

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Кликаем по логотипу самоката')
    def click_logo_scooter(self):
        self.wait_and_find_element(BasePageLocators.SCOOTER_LOGO).click()
        return self.wait_and_find_element(MainPageLocators.DOWN_ORDER_BUTTON_MAIN_PAGE)

    @allure.step('Кликаем по логотипу Яндекс')
    def click_logo_yandex(self):
        self.wait_and_find_element(BasePageLocators.YANDEX_LOGO).click()

    @allure.step('Заполняем поле Имя')
    def set_firstname(self, firstname):
        self.wait_and_find_element(OrderPageLocators.FIELD_FIRSTNAME).send_keys(firstname)

    @allure.step('Заполняем поле Фамилия')
    def set_secondname(self, secondname):
        self.wait_and_find_element(OrderPageLocators.FIELD_SECONDNAME).send_keys(secondname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        self.wait_and_find_element(OrderPageLocators.FIELD_ADDRESS).send_keys(address)

    @allure.step('Заполняем поле Метро')
    def set_subway(self, subway):
        self.wait_and_find_element(OrderPageLocators.FIELD_SUBWAY).click()
        self.wait_and_find_element(subway).click()

    @allure.step('Заполняем поле Номер телефона')
    def set_phone(self, phone):
        self.wait_and_find_element(OrderPageLocators.FIELD_PHONE).send_keys(phone)

    @allure.step('Кликаем по кнопке Далее')
    def next_button_click(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_NEXT_BUTTON).click()

    @allure.step('Заполняем поле Дата')
    def set_date_order(self, date):
        self.wait_and_find_element(OrderPageLocators.FIELD_DATE).send_keys(date)
        self.wait_and_find_element(OrderPageLocators.FIELD_DATE).send_keys(Keys.ENTER)

    @allure.step('Заполняем поле Срок аренды')
    def set_period_using(self, period):
        self.wait_and_find_element(OrderPageLocators.FIELD_RENTAL_PERIOD).click()
        self.wait_and_find_element(period).click()

    @allure.step('Выбираем цвет самоката')
    def set_color_scooter(self, color):
        self.wait_and_find_element(color).click()

    @allure.step('Заполняем поле Комментарий для курьера')
    def set_comment_for_delivery(self, comment):
        self.wait_and_find_element(OrderPageLocators.FIELD_COMMENT_FOR_DELIVERY).send_keys(comment)

    @allure.step('Кликаем по кнопке Да на выпадающем окне подтверждения заказа')
    def click_yes(self):
        self.wait_and_find_element(OrderPageLocators.YES_BUTTON).click()

    @allure.step('Нажимаем кнопку Заказать')
    def order_click(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_BUTTON).click()

    def fill_form_order(self, firstname, secondname, address, subway, phone, date, period, color, comment):
        self.set_firstname(firstname)
        self.set_secondname(secondname)
        self.set_address(address)
        self.set_subway(subway)
        self.set_phone(phone)
        self.next_button_click()
        self.set_date_order(date)
        self.set_period_using(period)
        self.set_color_scooter(color)
        self.set_comment_for_delivery(comment)
        self.order_click()
        self.click_yes()

    @allure.step('Получаем текст об успешно заказе')
    def get_complited_text(self):
        return self.wait_and_find_element(OrderPageLocators.ORDER_COMPLETED_TEXT).text
