import pytest

import classes
from classes import Product, Category


@pytest.fixture()
def product_apple():
    return Product('яблоко', 'вкусное', 200, 3)


@pytest.fixture()
def category():
    return Category('фрукты', 'полезные', classes.Product('яблоко', 'вкусное', 200, 3))


def test_init(product_apple):
    assert product_apple.name == 'яблоко'
    assert product_apple.description == 'вкусное'
    assert product_apple.price == 200
    assert product_apple.quantity == 3


def test_init_category(category):
    assert category.name == 'фрукты'
    assert category.description == 'полезные'
    assert category.list_of_products == ['яблоко', 'вкусное', 200, 3]
