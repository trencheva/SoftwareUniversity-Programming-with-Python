from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot('1', 'Military', 100, 1000)

    def test_allowed_categories(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)

    def test_price_increment_value(self):
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_price_with_negative_number_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -200
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_category_with_unacceptable_category_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Cleaner'
        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_correct_init(self):
        self.assertEqual('1', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual([], self.robot.hardware_upgrades)

    def test_upgrade_with_hardware_upgrade_that_already_exist_returns_correct_string(self):
        self.robot.hardware_upgrades.append('better ram')
        result = self.robot.upgrade('better ram', 10)
        self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", result)

    def test_upgrade_with_new_component_expect_success(self):
        self.robot.hardware_upgrades = ['ssd']
        result = self.robot.upgrade('better ram', 10)
        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with {"better ram"}.', result)
        self.assertEqual(1015, self.robot.price)
        self.assertEqual(['ssd', 'better ram'], self.robot.hardware_upgrades)

    def test_update_with_lower_version_returns_correct_string(self):
        self.robot.software_updates = [1, 2, 3]
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", self.robot.update(3, 30))

    def test_update_with_correct_version_without_capacity_returns_correct_string(self):
        self.robot.software_updates = [1, 2, 3]
        self.robot.available_capacity = 0
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", self.robot.update(3, 30))

    def test_update_expect_append_version_lower_capacity(self):
        self.robot.software_updates = [4.1]
        result = self.robot.update(5.0, 10)
        self.assertEqual([4.1, 5.0], self.robot.software_updates)
        self.assertEqual(90, self.robot.available_capacity)
        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version 5.0.', result)

    def test__gt__robot_with_higher_price_returns_correct_string(self):
        self.robot2 = Robot('1', 'Military', 100, 500)
        expected_result = f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.robot2.robot_id}.'
        self.assertEqual(expected_result, self.robot.__gt__(self.robot2))

    def test__gt__on_robots_with_equal_price_returns_correct_string(self):
        self.robot2 = Robot('1', 'Military', 100, 1000)
        expected_result = f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.robot2.robot_id}.'
        self.assertEqual(expected_result, self.robot.__gt__(self.robot2))

    def test__gt__robot_with_lower_price_returns_correct_string(self):
        self.robot2 = Robot('1', 'Military', 100, 5000)
        expected_result = f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.robot2.robot_id}.'
        self.assertEqual(expected_result, self.robot.__gt__(self.robot2))


if __name__ == '__main__':
    main()