from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_correct_init(self):
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected_result, self.store.toy_shelf)

    def test_add_toy_with_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('M', 'bear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_which_already_on_shelf_raises_exception(self):
        self.store.toy_shelf = {
            "A": 'bear',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'bear')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_on_taken_shelf_raises_exception(self):
        self.store.toy_shelf = {
            "A": 'bear',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.store.add_toy('A', 'doll')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_on_empty_shelf_expect_success(self):
        expected_result = {
            "A": 'bear',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        result = self.store.add_toy('A', 'bear')
        self.assertEqual("Toy:bear placed successfully!", result)
        self.assertEqual(expected_result, self.store.toy_shelf)

    def test_remove_toy_with_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('M', 'bear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_which_not_on_shelf_raises_exception(self):
        self.store.toy_shelf = {
            "A": 'bear',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'doll')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_expect_success(self):
        self.store.toy_shelf = {
            "A": 'bear',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        result = self.store.remove_toy('A', 'bear')
        self.assertEqual(f"Remove toy:bear successfully!", result)

        self.assertEqual(expected_result, self.store.toy_shelf)




if __name__ == '__main__':
    main()