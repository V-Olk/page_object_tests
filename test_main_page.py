from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #Гость открывает главную страницу 
    page = MainPage(browser, link)  
    page.open()
    #Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    
    basket_page = BasketPage(browser, browser.current_url)
    #basket_page.should_be_basket_page()

    #Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty()
    #Ожидаем, что есть текст о том что корзина пуста 
    basket_page.should_be_empty_message()
