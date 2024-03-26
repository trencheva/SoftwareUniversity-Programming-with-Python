from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Hero', 1, 100, 100)
        self.enemy = Hero('Enemy', 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual('Hero', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_hero_fights_with_himself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_without_hero_health_raises_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_without_enemy_health_raises_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_withdraw_return_draw(self):
        self.hero.health = 50
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_with_enemy_health_zero_return_correct_string_and_stats_increase(self):
        expected_level = self.hero.level + 1
        expected_health = (self.hero.health - self.enemy.damage * self.enemy.level) + 5
        expected_damage = self.hero.damage + 5
        result = self.hero.battle(self.enemy)
        self.assertEqual('You win', result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle_with_player_health_goes_zero_return_correct_string_and_enemy_stats_increase(self):
        self.hero, self.enemy = self.enemy, self.hero
        expected_level = self.enemy.level + 1
        expected_health = (self.enemy.health - self.hero.damage * self.hero.level) + 5
        expected_damage = self.enemy.damage + 5
        result = self.hero.battle(self.enemy)
        self.assertEqual('You lose', result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_correct__str__(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected_result, str(self.hero))





if __name__ == '__main__':
    main()
