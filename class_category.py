from class_product import Product


class Category:
    name: str
    description: str
    products = Product
    quantity_of_categories = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.list_of_products = [products.name, products.description, products.price, products.quantity]
        self.quantity_of_categories = 0
        Category.quantity_of_categories += 1
