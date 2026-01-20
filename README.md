# Sprint-6-Abramov
Финальный проект 6 спринта курса "Автоматизатор тестирования на Python" от Яндекс Практикум на тему "Page Object". Проект автоматизации тестирования сайта заказа самокатов https://qa-scooter.praktikum-services.ru/

allure_results - сожержит отчеты alure 
locators - директория локаторов 
    locators/main_page_locators.py - локаторы для главной страницы 
l   ocators/order_page_locators.py - локаторы для страницы заказа 
pages - директория методов страниц 
    pages/base_page.py - общие методы 
    pages/main_page.py - методы для главной страницы 
    pages/order_page.py - методы для страницы заказа 
tests - директория тестов 
    tests/test_faq.py - тесты для вопросов 
    tests/test_order.py - тесты для страницы заказа 
conftest.py - файл с фикстурами 
data.py - данные для параметризации 
README.md - описание проекта
requirements - файл с внешними зависимостями
urls.py - файл с константами URL

Команда для запуска тестов: pytest tests/ -v