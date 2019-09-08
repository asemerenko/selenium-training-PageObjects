from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CartPage:

    def __init__(self, wd):
        self.wd = wd
        self.wait = WebDriverWait(wd, 5)

    def open(self):
        self.wd.get("http://localhost/litecart/en/checkout")
        return self

    def cart_forms(self):
        return len(self.wd.find_elements_by_css_selector("[name='cart_form']"))

    @property
    def table(self):
        return self.wd.find_element_by_css_selector(".dataTable")

    @property
    def remove_cart_item(self):
        cart_form = self.wd.find_element_by_css_selector("[name='cart_form']")
        return cart_form.find_element_by_name("remove_cart_item")

    def wait_staleness_of_table(self, table):
        self.wait.until(ec.staleness_of(table))
        return self

    @property
    def cart_wrapper(self):
        return self.wd.find_element_by_css_selector("#checkout-cart-wrapper em")
