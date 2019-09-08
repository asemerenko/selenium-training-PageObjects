from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec


class ProductPage:

    def __init__(self, wd):
        self.wd = wd
        self.wait = WebDriverWait(wd, 5)

    def open(self, link):
        self.wd.get(link)
        return self

    @property
    def cart_quantity(self):
        return self.wd.find_element_by_css_selector("#cart .quantity")

    def select_size_if_present(self, size):
        if is_element_present(self.wd, By.NAME, "options[Size]"):
            Select(self.wd.find_element_by_name("options[Size]")).select_by_value(size)

    @property
    def quantity(self):
        return self.wd.find_element_by_name("quantity")

    @property
    def add_cart_product(self):
        return self.wd.find_element_by_name("add_cart_product")

    def wait_quantity(self, new_quantity):
        self.wait.until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart .quantity"), new_quantity))
        return self


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False
