import allure
import pytest

from data import OrderData
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPage
from urls import Urls 


@allure.feature('Заказы')
class TestOrder:

    @allure.title('Проверка верхней кнопки заказа')
    @allure.description('Находим сверху кнопку Заказа и нажимаем на нее')
    def test_top_order_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_top_order_btn()
        assert page.get_current_url() == Urls.ORDER_PAGE, f"Верняя кнопка заказа ведёт на неправильную страницу"


    @allure.title('Проверка нижней кнопки заказа')
    @allure.description('Находим снизу кнопку Заказа и нажимаем на нее')
    def test_bottom_order_button(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_bottom_order_btn()
        assert page.get_current_url() == Urls.ORDER_PAGE, f"Нижняя кнопка заказа ведёт на неправильную страницу"

    
    @allure.title('Полная процедура заказа самоката через верхнюю кнопку')
    @pytest.mark.parametrize(OrderData.param, OrderData.value)
    def test_order_scooter_via_top_button(self, driver, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_top_order_btn()
        order_page.order_scooter(first_name, last_name, address, metro_station, phone, delivery_date, rental_period)
        assert order_page.find_status_button() == True


    @allure.title('Полная процедура заказа самоката через нижнюю кнопку')
    @pytest.mark.parametrize(OrderData.param, OrderData.value)
    def test_order_scooter_via_bottom_button(self, driver, first_name, last_name, address, metro_station, phone, delivery_date, rental_period):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_bottom_order_btn()
        order_page.order_scooter(first_name, last_name, address, metro_station, phone, delivery_date, rental_period)
        assert order_page.find_status_button() == True
   

    @allure.title('Переходим на главную страницу через лого "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.ORDER_PAGE)
        page.click_to_scooter()
        assert page.get_current_url() == Urls.MAIN_PAGE


    @allure.title('Переходим на яндекс дзен через яндекс лого')
    def test_yandex_logo_redirect(self, driver):
        page = MainPage(driver)
        page.open_page(Urls.ORDER_PAGE)
        page.click_to_yandex_logo()
        page.switch_to_window(1)
        page.wait_and_find_element(MainPageLocators.DZEN_NEWS)
        assert page.get_current_url() == Urls.DZEN_URL
        