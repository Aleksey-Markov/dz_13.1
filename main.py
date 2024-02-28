from class_category import Category
from class_product import Product
from class_product import SmartPhone

pr = Product('яблоко', 'красное', 100, 3)
pr2 = Product('жопа', 'вонючая', 2000, 5)
phone = SmartPhone('iphone', 'smartphone', 100000, 2, 3000, 'apple', 8, 'black')
fruits = Category('фрукты', 'полезные', [])
mylist = ['qwerty', 2]
fruits.products = mylist
fruits.products = pr
fruits.products = phone
fruits.products = mylist
print(fruits.products)

