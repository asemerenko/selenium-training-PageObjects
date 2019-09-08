from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from random import randrange


class Application:
    def __init__(self, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        print(self.wd.capabilities)
        self.wd.implicitly_wait(3)
        self.main_page = MainPage(self.wd)
        self.product_page = ProductPage(self.wd)
        self.cart_page = CartPage(self.wd)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def get_products_list(self):
        self.main_page.open()
        products = self.main_page.get_products()
        return products

    def add_random_product_to_cart(self, product_list, q):
        index = randrange(len(product_list))
        self.product_page.open(product_list[index].link)
        old_quantity = self.product_page.cart_quantity.text
        self.product_page.select_size_if_present('Small')
        self.product_page.quantity.click()
        self.product_page.quantity.clear()
        self.product_page.quantity.send_keys(q)
        self.product_page.add_cart_product.click()
        new_quantity = str(int(old_quantity) + q)
        self.product_page.wait_quantity(new_quantity)

    def del_all_products_from_cart(self):
        self.cart_page.open()
        forms = self.cart_page.cart_forms()
        for item in range(forms):
            table = self.cart_page.table
            self.cart_page.remove_cart_item.click()
            self.cart_page.wait_staleness_of_table(table)
        assert self.cart_page.cart_wrapper.text == "There are no items in your cart."
