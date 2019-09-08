def test_add_products_to_cart(app):
    n = 3
    quantity = 2
    products_list = app.get_products_list()
    for ind in range(n):
        app.add_random_product_to_cart(products_list, quantity)
    app.del_all_products_from_cart()
