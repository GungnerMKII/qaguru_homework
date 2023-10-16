"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from homework.models import Product

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        test_product = product
        assert test_product.check_quantity(0)
        assert test_product.check_quantity(test_product.quantity)
        assert test_product.check_quantity(test_product.quantity - 1)
        assert test_product.check_quantity(test_product.quantity + 1) == False
        

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        test_product = product
        items_quantity = test_product.quantity
        test_product.buy(1)
        assert test_product.quantity == items_quantity - 1

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        test_product = product
        items_quantity = test_product.quantity
        with pytest.raises(ValueError, match="Not enough products available."):
            test_product.buy(test_product.quantity + 1)
        assert test_product.quantity == items_quantity

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        test_cart = cart
        test_product = product

        # Проверяем добавление продукта в корзину
        cart.add_product(test_product, buy_count=2)
        assert test_product in test_cart.products
        assert test_cart.products[test_product] == 2

        # Проверяем увеличение количества, если продукт уже есть в корзине
        test_cart.add_product(test_product, buy_count=3)
        assert test_cart.products[test_product] == 5

    def test_remove_product(self, cart, product):
        test_cart = cart
        test_product = product

        # Проверяем удаление продукта из корзины
        test_cart.add_product(test_product, buy_count=5)
        test_cart.remove_product(test_product)
        assert test_product not in test_cart.products

        # Проверяем удаление продукта с указанным количеством
        test_cart.add_product(test_product, buy_count=5)
        test_cart.remove_product(test_product, remove_count=3)
        assert test_cart.products[test_product] == 2

        # Проверяем удаление продукта с указанным количеством, превышающим текущее количество
        test_cart.remove_product(test_product, remove_count=5)
        assert test_product not in cart.products

    def test_clear(self, cart, product):
        test_cart = cart
        test_product = product

        test_cart.add_product(test_product, buy_count=5)
        test_cart.clear()
        assert not test_cart.products

    def test_get_total_price(self, cart, product):
        test_cart = cart
        product1 = product
        product2 = Product(name="Another Book", price=20.0, description="Another Book Description", quantity=3)

        test_cart.add_product(product1, buy_count=2)
        test_cart.add_product(product2, buy_count=1)
        assert test_cart.get_total_price() == 100 * 2 + 20.0 * 1

    def test_buy(self, cart, product):
        test_cart = cart
        test_product = product

        # Проверяем успешную покупку
        test_cart.add_product(test_product, buy_count=5)
        test_cart.buy()
        assert test_product not in test_cart.products  
        
        # Проверяем ошибку при покупке, когда товаров не хватает
        test_cart.add_product(test_product, buy_count=1001)
        with pytest.raises(ValueError, match=f"Not enough products available for '{test_product.name}'."):
            test_cart.buy()