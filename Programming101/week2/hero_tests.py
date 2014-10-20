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
        pass

if __name__ == '__main__':
    unittest.main()
