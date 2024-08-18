from selenium.webdriver.common.by import By


class MainPageLocators:

    DOWN_ORDER_BUTTON_MAIN_PAGE = (By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[contains(text(), "Заказать")]')
    HEADLINE_TEXT = (By.XPATH, './/div[contains(@class, "Home_Header")]')

    @staticmethod
    def question_button_locator(question):
        return By.XPATH, f'.//div[contains(@id,"accordion__heading") and text()="{question}"]'

    @staticmethod
    def answer_panel_locator(answer):
        return By.XPATH, f'.//div[contains(@id,"accordion__panel")]/p[text()="{answer}"]/parent::div'

    @staticmethod
    def answer_text_locator(answer):
        return By.XPATH, f'.//div[contains(@id,"accordion__panel")]/p[text()="{answer}"]'