from class_product import Product, apple, grusha


class Category:
    '''
    Класс категорий товаров
    '''
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.products_count += len(set(products))

    @property
    def products(self):
        for item in self.__products:
            result = print(f'{item.name}, {item.price} руб. Остаток:{item.quantity}')
        return result

    @products.setter
    def products(self, product):
        self.__products.append(product)

    @property
    def products_list(self):
        return self.__products


fruits = Category('фрукты', 'полезные', [])
fruits.products = apple
fruits.products = grusha
fruits.products
