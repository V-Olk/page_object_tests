from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_title()

    def should_be_basket_url(self):
        assert "basket" in self.url, "Basket link is not presented"
        assert True

    def should_be_basket_title(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TITLE), "Basket title is not presented"
        assert True

    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MSG), "Basket is not empty"

    def should_be_empty_message(self):
        assert "empty" in self.browser.find_element(*BasketPageLocators.EMPTY_MSG).text, "Basket is not empty"
