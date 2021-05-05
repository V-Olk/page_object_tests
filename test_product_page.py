from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
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