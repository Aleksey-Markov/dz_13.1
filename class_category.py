from class_product import Product
from mixin import MixinShow


class Category(MixinShow):
    """
    Класс категорий товаров
    """
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        super().__init__()
        Category.category_count += 1
        Category.products_count += len(set(products))

    def __len__(self):
        result = 0
        for i in self.__products:
            result += i.quantity
        return result

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def average_sum(self):
        try:
            result = 0
            for i in self.__products:
                result += i._price * i.quantity
            return result / len(self)
        except ZeroDivisionError:
            print('0')

    @property
    def products(self):
        products_list = []
        for item in self.__products:
            products_list.append(f'{item.name}, {item.price} руб. Остаток:{item.quantity} шт.')
        return products_list

    @products.setter
    def products(self, product):
        if product.quantity == 0:
            raise ValueError('Невозможно добавить товар с нулевым количеством!')
        if isinstance(product, Product):
            self.__products.append(product)

    @property
    def products_list(self):
        return self.__products
