import allure

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликаем по вопросам')
    def click_question_button(self, text):
        btn = self.wait_and_find_element(MainPageLocators.question_button_locator(text))
        self.driver.execute_script("arguments[0].click()", btn)
        return self.wait_and_find_element(MainPageLocators.question_button_locator(text)).text

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer(self, text):
        self.wait_and_find_element(MainPageLocators.answer_panel_locator(text))
        return self.wait_and_find_element(MainPageLocators.answer_text_locator(text))

    @allure.step('Кликаем по кнопке "Заказать" на главной странице')
    def click_order_button(self, locator):
        btn = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].click()", btn)
        return self.wait_and_find_element(OrderPageLocators.ORDER_NEXT_BUTTON)
