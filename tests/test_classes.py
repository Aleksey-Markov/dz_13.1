import pytest
from class_product import Product
from class_category import Category


@pytest.fixture()
def product_apple():
    return Product('яблоко', 'вкусное', 200, 3)


@pytest.fixture()
def category():
    return Category('фрукты', 'полезные', [])


def test_init(product_apple):
    assert product_apple.name == 'яблоко'
    assert product_apple.description == 'вкусное'
    assert product_apple.price == 200
    assert product_apple.quantity == 3


def test_init_category(category):
    assert category.name == 'фрукты'
    assert category.description == 'полезные'
    assert category.products_list == []


def test_count(category):
    assert Category.category_count == 1
    assert Category.products_count == 0


def test_products_setter(category, product_apple):
    assert category.products == []
    category.products = [1, 2, 3]
    assert category.products == []
    category.products = product_apple
    assert category.products == ['яблоко, 200 руб. Остаток:3 шт.']


def test_new_product_quantity():
    with pytest.raises(ValueError):
        Product.new_product('apple', 'tasty', 100, 0, [])