class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def product(self):
        return [self.name, self.description, self.price, self.quantity]

    def add_to_unique(self):
        if self.name != Product.product(apple)[0]:
            return True


class Category(Product):
    name: str
    description: str
    products: list
    quantity_of_categories = 0

    def __init__(self, name, description, products, quantity_of_categories=0, quantity_unique_products=0):
        self.name = name
        self.description = description
        self.products = products
        self.quantity_of_categories = 0
        Category.quantity_of_categories += 1
        if Product.add_to_unique(self):
            self.quantity_of_categories += 1


apple = Product('яблоко','вкусное', 200, 3)
fruits = Category('фрукты', 'полезные', Category.product(apple))
