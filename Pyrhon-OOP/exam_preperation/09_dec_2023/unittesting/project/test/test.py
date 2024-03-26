from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation('Zornitsa')

    def test_correct_init(self):
        self.assertEqual('Zornitsa', self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_name_short_value_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'a'
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_adds_train_to_arrival_trains(self):
        expected_result = deque(["train 1", "train 2"])
        self.station.new_arrival_on_board("train 1")
        self.station.new_arrival_on_board("train 2")
        self.assertEqual(expected_result, self.station.arrival_trains)

    def test_train_has_arrived_with_incorrect_train_info_expect_correct_string(self):
        self.station.new_arrival_on_board("train 1")
        self.station.new_arrival_on_board("train 2")
        self.assertEqual("There are other trains to arrive before train 2.", self.station.train_has_arrived("train 2"))

    def test_train_has_arrived_with_correct_train_info_expect_correct_string_move_train_to_departure(self):
        self.station.new_arrival_on_board("train 1")
        self.station.new_arrival_on_board("train 2")
        self.station.departure_trains = deque(["train 0"])

        self.assertEqual(f"train 1 is on the platform and will leave in 5 minutes.", self.station.train_has_arrived('train 1'))
        self.assertEqual(deque(['train 0', 'train 1']), self.station.departure_trains)
        self.assertEqual(deque(["train 2"]), self.station.arrival_trains)

    def test_train_has_left_with_correct_train_expect_true_po_from_departure(self):
        self.station.departure_trains.append("train 1")
        self.assertTrue(self.station.train_has_left("train 1"))
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_train_has_left_with_incorrect_train_expect_false(self):
        self.assertFalse(self.station.train_has_left("train 1"))


if __name__ == '__main__':
    main()