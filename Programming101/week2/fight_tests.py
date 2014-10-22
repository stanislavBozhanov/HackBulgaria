import unittest
from hero import Hero
from orc import Orc
from fight import Fight


class TestFight(unittest.TestCase):

    def setUp(self):
        self.sho = Orc("Vilasteros", 400, 1.34)
        self.sten = Hero("Bron", 100, "DragonSlayer")
        self.battle = Fight(self.sten, self.sho)

    def test_init(self):
        self.assertEqual(self.battle.hero, self.sten)
        self.assertEqual(self.battle.orc, self.sho)

    def test_flip_coin(self):
        self.assertGreaterEqual(self.battle.flip_coin(), 0)
        self.assertLessEqual(self.battle.flip_coin(), 1)

    def test_simulate_fight():
        pass

if __name__ == '__main__':
    unittest.main()
