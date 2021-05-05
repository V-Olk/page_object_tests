from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BTN_BASKET = (By.CSS_SELECTOR, "a[href='/en-gb/basket/']")

class BasketPageLocators():
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
    ALERT_EMPTY = (By.CSS_SELECTOR, ".alert-info p")
    EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner")