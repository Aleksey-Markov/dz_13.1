from main import Category, fruits


class Product:
    """
     Класс товаров
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity, products):
        for i in products:
            if name == i.name:
                quantity += i.quantity
                if price < i._price:
                    price = i._price
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


apple = Product('яблоко', 'вкусное', 200, 3)
grusha = Product('груша', 'тоже вкусная', 180, 5)
grusha1 = Product.new_product('груша', 'тоже вкусная', 190, 2, fruits.products_list)
print(grusha1.quantity)
