from selenium.webdriver.support.wait import WebDriverWait
from model.product import Product


class MainPage:

    def __init__(self, wd):
        self.wd = wd
        self.wait = WebDriverWait(wd, 5)

    def open(self):
        self.wd.get("http://localhost/litecart/en/")
        return self

    @property
    def products(self):
        return self.wd.find_elements_by_css_selector(".product")

    def get_products(self):
        products_list = []
        for pr in self.products:
            name = pr.find_element_by_class_name("name").text
            link = pr.find_element_by_class_name("link").get_attribute("href")
            products_list.append(Product(name=name, link=link))
        return products_list
