from unittest import TestCase, main
# from first_test_worker.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 200, 10)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(200, self.worker.salary)
        self.assertEqual(10, self.worker.energy)

    def test_work_with_energy_expect_money_increase_and_energy_decrease(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_without_energy_expect_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_expect_energy_increase_by_one(self):
        expect_energy = self.worker.energy + 1
        self.worker.rest()

        self.assertEqual(expect_energy, self.worker.energy)

    def test_get_info_returns_correct_string(self):
        self.assertEqual('Ivan has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()

