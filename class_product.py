from abc import ABC, abstractmethod
from mixin import MixinShow


class BaseProduct(ABC):
    """
    Абстрактный класс для продуктов
    """
    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls):
        pass


class Product(BaseProduct, MixinShow):
    """
     Класс товаров
    """

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self._price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            result = (self._price * self.quantity) + (other._price * other.quantity)
            return result
        else:
            raise TypeError('Можно складывать только экземпляры одного и того же класса!')

    @classmethod
    def new_product(cls, name, description, price, quantity, products):
        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен!')
        for i in products:
            if name == i.name:
                i.quantity += quantity
                if price < i._price:
                    i._price = price
            else:
                return cls(name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0 or new_price == self._price:
            print('Введена некорректная цена!')
        elif new_price < self._price:
            user_answer = input('Если вы хотите поменять цену введите: y, иначе n')
            if user_answer == 'y':
                self._price = new_price
            else:
                print("Введите корректный ответ, пожалуйста!")
        else:
            self._price = new_price


class SmartPhone(Product, MixinShow):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product, MixinShow):
    def __init__(self, name, description, price, quantity, manufacturer, germination, color):
        self.manufacturer = manufacturer
        self.germination = germination
        self.color = color
        super().__init__(name, description, price, quantity)
