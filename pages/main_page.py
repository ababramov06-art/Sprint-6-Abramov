from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls
import allure


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @allure.step("Клик по верхней кнопке заказа")
    def click_top_order_btn(self):
        self.wait_and_find_element(MainPageLocators.TOP_ORDER_BTN).click()

    @allure.step("Клик по нижней кнопке заказа")
    def click_bottom_order_btn(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BTN)
        self.wait_and_find_element(MainPageLocators.BOTTOM_ORDER_BTN).click()

    @allure.step("Скролл к разделу FAQ")
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Клик по логотипу Яндекса")
    def click_to_yandex_logo(self):
        self.wait_and_find_element(MainPageLocators.YANDEX_LOGO).click()

    @allure.step("Клик по лого самоката")
    def click_to_scooter(self):
        self.wait_and_find_element(MainPageLocators.SCOOTER_LOGO).click()

    @allure.step("Получаем текст вопроса и ответ по локаторам")
    def get_question_and_answer(self, question_index, answer_index):
        self.scroll_to_faq()
        question_loc = MainPageLocators.question_locator(question_index)
        answer_loc = MainPageLocators.answer_locator(answer_index)
        question_text = self.wait_and_find_element(question_loc).text
        self.wait_and_find_element(question_loc).click()
        answer_text = self.wait_and_find_element(answer_loc).text
        return question_text, answer_text
    
    @allure.step("Проверка редиректа на страницу заказа")
    def check_redirect_to_order_page(self):
        return self.get_current_url() == Urls.ORDER_PAGE
    