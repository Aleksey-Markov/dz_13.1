from class_product import Product, apple, grusha, grusha1


class Category:
    '''
    Класс категорий товаров
    '''
    category_count = 0
    products_count = 1

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = [products.__dict__]
        Category.category_count += 1
        if products.name != products.name:
            Category.products_count += 1

    @property
    def products(self):
        return f'{self.__products[0]["name"]}, {self.__products[0]["_price"]} руб. Остаток: {self.__products[0]["quantity"]} шт.'

    @products.setter
    def products(self, product):
        self.__products.append(product.__dict__)


fruits = Category('фрукты', 'полезные', apple)
fruits1 = Category('фрукты', 'полезные', grusha)
print(fruits1.products)


