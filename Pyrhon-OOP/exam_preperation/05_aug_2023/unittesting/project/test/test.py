from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar('Stinger', 'Sport car', 10_000, 80_000)
        self.car2 = SecondHandCar('Punto', 'Family car', 200_000, 5000)
        self.car3 = SecondHandCar('320', 'Sport car', 200_000, 60_000)

    def test_price_equal_one_point_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_value_equal_one_hundred_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_correct_init(self):
        self.assertEqual('Stinger', self.car.model)
        self.assertEqual('Sport car', self.car.car_type)
        self.assertEqual(10_000, self.car.mileage)
        self.assertEqual(80_000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_set_promotion_with_equal_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(80_000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotion_with_higher_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(100_000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotion_with_lower_price_sets_the_price_returns_correct_string(self):
        result = self.car.set_promotional_price(50_000)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_need_repair_too_expensive_returns_string(self):
        result = self.car.need_repair(50_000, 'description')
        self.assertEqual('Repair is impossible!', result)

    def test_repair_appropriate_price_increase_price_adds_description_to_repairs(self):
        self.car.repairs = ['new window']
        result = self.car.need_repair(2000, 'steer wheel changed')
        self.assertEqual(82_000, self.car.price)
        self.assertEqual(['new window', 'steer wheel changed'], self.car.repairs)
        self.assertEqual('Price has been increased due to repair charges.', result)

    def test__gt__with_different_car_types(self):
        result = self.car.__gt__(self.car2)
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test__gt__from_same_type_expect_correct_bool(self):
        self.assertTrue(self.car.__gt__(self.car3))

    def test__str__expect_correct_string(self):
        expected_result = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""
        self.assertEqual(expected_result, str(self.car))


if __name__ == '__main__':
    main()
