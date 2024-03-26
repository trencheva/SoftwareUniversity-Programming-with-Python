from unittest import TestCase, main
# from second_test_cat.cat import Cat


class TestCat(TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Maxi')

    def test_correct_init(self):
        self.assertEqual('Maxi', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_expect_fed_and_sleepy_get_true_and_size_increase_with_one(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_eat_when_already_fed_expect_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_if_fed_expect_not_sleepy_after_that(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_make_hungry_cat_sleep_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()