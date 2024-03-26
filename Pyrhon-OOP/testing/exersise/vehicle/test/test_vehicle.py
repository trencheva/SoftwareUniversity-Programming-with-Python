from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 200)

    def test_correct_default_fuel_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_without_fuel_raises_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_and_fuel_decrease(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_over_the_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(200)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_correct_amount_fuel_increase(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(50)
        self.assertEqual(100, self.vehicle.fuel)

    def test_correct__str__(self):
        expected_result = f"The vehicle has 200 " \
               f"horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == '__main__':
    main()