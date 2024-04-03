from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart('Lidl', 100)
        self.cart2 = ShoppingCart('Sinsay', 500)

    def test_correct_init(self):
        self.assertEqual('Lidl', self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_starts_with_lowercase_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'lidl'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_with_digits_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'Lid45'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_product_price_equal_100_raisesValue_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('mop', 100.0)
        self.assertEqual("Product mop cost too much!", str(ve.exception))

    def test_add_to_cart_product_price_over_100_raisesValue_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('mop', 100.1)
        self.assertEqual("Product mop cost too much!", str(ve.exception))

    def test_add_to_cart_valid_product_price_expect_success(self):
        result = self.cart.add_to_cart('pants', 12.0)
        self.assertEqual({'pants': 12.0}, self.cart.products)
        self.assertEqual("pants product was successfully added to the cart!", result)

    def test_remove_from_cart_with_existing_product_expect_success(self):
        self.cart.add_to_cart('pants', 12.0)
        self.cart.add_to_cart('cheese', 5.0)
        result = self.cart.remove_from_cart('cheese')
        self.assertEqual({'pants': 12.0}, self.cart.products)
        self.assertEqual("Product cheese was successfully removed from the cart!", result)

    def test_remove_with_non_existing_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('cheese')
        self.assertEqual("No product with name cheese in the cart!", str(ve.exception))

    def test__add__expect_success(self):
        self.cart.products = {'banitsa': 2.0}
        self.cart2.products = {'kozunac': 6.0, 'milk': 1.90}
        new_cart = self.cart.__add__(self.cart2)
        self.assertEqual('LidlSinsay', new_cart.shop_name)
        self.assertEqual(600, new_cart.budget)
        self.assertEqual({'banitsa': 2.0, 'kozunac': 6.0, 'milk': 1.90}, new_cart.products)

    def test_buy_products_without_money_raises_value_error(self):
        self.cart.products = {'milk': 2.0}
        self.cart.budget = 0.50
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 1.50lv!", str(ve.exception))

    def test_buy_products_with_enough_money_returns_correct_string(self):
        self.cart.products = {'milk': 2.0}
        expected_result = 'Products were successfully bought! Total cost: 2.00lv.'
        self.assertEqual(expected_result, self.cart.buy_products())


if __name__ == '__main__':
    main()