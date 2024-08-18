import pytest
import allure
from data import Urls, QuestionData
from pages.main_page import MainPage


class TestQuestions:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверяем каждый вопрос и ответ на соответвие')
    @pytest.mark.parametrize(QuestionData.parametrs, QuestionData.value)
    def test_click_question_show_answer(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        question_panel_text = main_page.click_question_button(question)

        assert question_panel_text == question, f'Вопрос "{question_panel_text}" не соотвествует ожидаемому "{question}"'

        answer_panel_text = main_page.get_answer(answer).text

        assert answer_panel_text == answer, f'Ответ "{answer_panel_text}" на вопрос не соответствует ожидаемому "{answer}"'



