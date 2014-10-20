from hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.sten = Hero("Bron", 100, "DragonSlayer")

    def test_init(self):
        self.assertEqual(self.sten.name, "Bron")
        self.assertEqual(self.sten.health, 100)
        self.assertEqual(self.sten.nickname, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.sten.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):
        self.assertEqual(self.sten.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.sten.is_alive())

    def test_not_alive(self):
        self.sten.health = 0
        self.assertFalse(self.sten.is_alive())

    def test_take_damage(self):
        self.sten.take_damage(50)
        self.assertEqual(self.sten.health, 50)
        self.sten.take_damage(60)
        self.assertEqual(self.sten.health, 0)

    def test_take_healing(self):
        self.sten.health = 50
        self.assertTrue(self.sten.take_healing(20))
        self.assertEqual(self.sten.health, 70)

    def test_take_healing_above_max(self):
        self.sten.health = 20
        self.sten.take_healing(120)
        self.assertEqual(self.sten.health, 100)

    def test_healing_on_dead(self):
        self.sten.health = 0
        self.assertFalse(self.sten.take_healing(100))

if __name__ == '__main__':
    unittest.main()
