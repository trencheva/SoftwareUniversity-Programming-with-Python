from unittest import TestCase, main
# from fourth_test_cat_manager.car_manager import Car


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car('Fiat', '500', 10, 100)

    def test_correct_init(self):
        self.assertEqual('Fiat', self.car.make)
        self.assertEqual('500', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_set_fuel_consumption_with_negative_number_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -100
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_set_fuel_capacity_with_negative_number_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -100
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_set_fuel_amount_with_negative_number_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -100
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_negative_number_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more_than_capacity_expect_fuel_increase_to_capacity(self):
        self.car.refuel(120)
        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_not_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_decrease_fuel_amount(self):
        self.car.fuel_amount += 100
        self.car.drive(50)
        self.assertEqual(95, self.car.fuel_amount)


if __name__ == '__main__':
    main()