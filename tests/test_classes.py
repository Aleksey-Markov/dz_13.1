import pytest
from classes import Product, Category


@pytest.fixture()
def product_apple():
    return Product('яблоко', 'вкусное', 200, 3)


@pytest.fixture()
def category():
    return Category('фрукты', 'полезные', ['яблоко', 'вкусное', 200, 3], 0, 0)


def test_init(product_apple):
    assert product_apple.name == 'яблоко'
    assert product_apple.description == 'вкусное'
    assert product_apple.price == 200
    assert product_apple.quantity == 3


def test_init_category():
    assert category().name == 'фрукты'
    assert category().description == 'полезные'
    assert category().products == ['яблоко', 'вкусное', 200, 3]
