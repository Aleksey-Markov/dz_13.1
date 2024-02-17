import pytest
from class_product import Product, apple, grusha
from class_category import Category


@pytest.fixture()
def product_apple():
    return Product('яблоко', 'вкусное', 200, 3)


@pytest.fixture()
def category():
    return Category('фрукты', 'полезные', apple)


def test_init(product_apple):
    assert product_apple.name == 'яблоко'
    assert product_apple.description == 'вкусное'
    assert product_apple.price == 200
    assert product_apple.quantity == 3


def test_init_category(category):
    assert category.name == 'фрукты'
    assert category.description == 'полезные'
    assert category.products == category.products


def test_count():
    assert Category.category_count == 1
    assert Category.products_count == 1
