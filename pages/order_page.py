import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        self.wait_and_find_element(OrderPageLocators.NAME_INPUT).send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_second_name(self, lastname):
        self.wait_and_find_element(OrderPageLocators.LASTNAME_INPUT).send_keys(lastname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        self.wait_and_find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Заполняем поле Станция метро')
    def set_metro_station(self, metro_station):
        self.wait_and_find_element(OrderPageLocators.METRO_FIELD).click()
        self.wait_and_find_element(OrderPageLocators.station_locator(metro_station)).click()

    @allure.step('Заполняем поле Номер телефона')
    def set_phone_number(self, phone):
        self.wait_and_find_element(OrderPageLocators.PHONE_FIELD).send_keys(phone)

    @allure.step('Кликаем кнопку далее')
    def click_continue_button(self):
        self.wait_and_find_element(OrderPageLocators.NEXT_BTN).click()

    @allure.step('Выбираем дату доставки')
    def set_delivery_date(self, delivery_day):
        self.wait_and_find_element(OrderPageLocators.DATE_INPUT).click()
        self.wait_and_find_element(OrderPageLocators.date_locator(delivery_day)).click()

    @allure.step('Заполняем поле Срок Аренды')
    def set_rental_period(self, rental_period):
        self.wait_and_find_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        self.wait_and_find_element(OrderPageLocators.period_locator(rental_period)).click()

    @allure.step('Кликаем кнопку заказать')
    def click_order_button(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_BTN).click()

    @allure.step('Подтверждаем заказ')
    def click_confirm_button(self):
        self.wait_and_find_element(OrderPageLocators.CONFIRM_BTN).click()

    @allure.step('Находим кнопку Статус Заказа')
    def find_status_button(self):
        return self.wait_and_find_element(OrderPageLocators.STATUS_BTN).is_displayed()

    @allure.step('Заказываем самокат')
    def order_scooter(self, name, second_name, address, metro_station, phone_number, day_number, period):
        self.set_name(name)
        self.set_second_name(second_name)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone_number(phone_number)
        self.click_continue_button()
        self.set_delivery_date(day_number)
        self.set_rental_period(period)
        self.click_order_button()
        self.click_confirm_button()
        