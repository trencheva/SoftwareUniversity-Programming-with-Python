from unittest import TestCase, main
# from third_testing_list.list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3, 'j', 6.3)

    def test_correct_init_ignores_non_integer_values(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_non_int_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.add('s')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_int_add_the_int_to_the_list(self):
        self.int_list.add(4)

        self.assertEqual([1, 2, 3, 4], self.int_list.get_data())

    def test_remove_index_with_invalid_index_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(100)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index_removes_correct_element(self):
        self.int_list.remove_index(0)
        self.assertEqual([2, 3], self.int_list.get_data())

    def test_get_with_invalid_index_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.get(100)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_correct_index_gives_correct_integer(self):
        self.assertEqual(2, self.int_list.get_data()[1])

    def test_insert_with_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(200, 6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_non_integer_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, "hello")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_valid_data_expect_int_added_to_list(self):
        self.int_list.insert(0, 9)

        self.assertEqual([9, 1, 2, 3], self.int_list.get_data())

    def test_het_biggest_number(self):
        self.assertEqual(3, self.int_list.get_biggest())

    def test_get_index_of_element(self):
        self.assertEqual(0, self.int_list.get_index(1))


if __name__ == '__main__':
    main()