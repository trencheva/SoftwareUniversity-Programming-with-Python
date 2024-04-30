from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer('Ivan', 20, 10)
        self.player2 = TennisPlayer('Pesho', 22, 15)

    def test_correct_init(self):
        self.assertEqual('Ivan', self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(10, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_with_two_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Iv'
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_with_less_than_two_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'I'
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_less_than_eighteen_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_nwe_win_with_valid_tournament_name_expect_success(self):
        self.player.wins = ['asd']
        self.player.add_new_win('abc')
        self.assertEqual(['asd', 'abc'], self.player.wins)

    def test_nwe_win_with_invalid_tournament_name_returns_correct_string(self):
        self.player.wins = ['asd']
        result = self.player.add_new_win('asd')
        self.assertEqual("asd has been already added to the list of wins!", result)

    def test__lt__with_less_points_expect_correct_string(self):
        result = self.player < self.player2
        self.assertEqual('Pesho is a top seeded player and he/she is better than Ivan', result)

    def test__lt__with_more_points_expect_correct_string(self):
        result = self.player2 < self.player
        self.assertEqual(f'Pesho is a better player than Ivan', result)

    def test__str__(self):
        self.player.wins = ['asd', 'abc']
        expected_result = f"Tennis Player: Ivan\n" \
               f"Age: 20\n" \
               f"Points: 10.0\n" \
               f"Tournaments won: {', '.join(['asd', 'abc'])}"
        self.assertEqual(expected_result, self.player.__str__())

if __name__ == '__main__':
    main()