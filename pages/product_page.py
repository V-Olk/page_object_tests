from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "'Add to basket' button is not presented"

    def should_be_the_same_name_of_product(self, name):
        assert self.is_element_present(By.CSS_SELECTOR, "#messages strong"), "Messages are not presented"
        elements = self.browser.find_elements(By.CSS_SELECTOR, "#messages strong")
        assert elements[0].text == name, "Different name of product"

    def should_be_the_same_price_of_product(self, price):
        assert self.is_element_present(By.CSS_SELECTOR, "#messages strong"), "Messages are not presented"
        elements = self.browser.find_elements(By.CSS_SELECTOR, "#messages strong")
        assert elements[2].text == price, "Different price of product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should be"


