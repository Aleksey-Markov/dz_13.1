from class_product import Product


class Category:
    name: str
    description: str
    products = list
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.products_count += 1
        for product in products:
            if product in products:
                self.products_count -= 1
