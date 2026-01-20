import allure
import pytest

from data import FAQData
from pages.main_page import MainPage
from urls import Urls

@allure.feature('FAQ')
class TestFAQ:

    @allure.title('Проверка ответа на вопрос #{number}')
    @allure.description('Проверяем соответствие ответа на выбранный вопрос')
    @pytest.mark.parametrize(FAQData.param, FAQData.value)
    def test_question_and_answer(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        question_text, answer_text = main_page.get_question_and_answer(number, number)
        assert answer_text == expected_answer, (
            f"Неверный ответ для вопроса #{number}\n"
            f"Вопрос: {question_text}\n"
            f"Ожидаемый ответ: {expected_answer}\n"
            f"Фактический ответ: {answer_text}"
        )
        