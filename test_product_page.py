from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = MainPage(browser, link)
    page.open()

    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_add_to_basket_btn()

    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()

    button = browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
    button.click()

    product_page.solve_quiz_and_get_code()

    product_page.should_be_the_same_name_of_product(product_name)
    product_page.should_be_the_same_price_of_product(product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = MainPage(browser, link)
    page.open()  
    product_page = ProductPage(browser, browser.current_url)

    #Добавляем товар в корзину 
    browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    page.open()  
    product_page = ProductPage(browser, browser.current_url)

    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = MainPage(browser, link)
    page.open()  
    product_page = ProductPage(browser, browser.current_url)
    
    #Добавляем товар в корзину
    browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_dissapear_success_message()