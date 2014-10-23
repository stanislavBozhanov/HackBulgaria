import unittest
from hero import Hero
from orc import Orc
from weapon import Weapon
from fight import Fight


class TestFight(unittest.TestCase):

        def setUp(self):
            self.sten = Hero("Bron", 100, "DragonSlayer")
            self.sho = Orc("Vilasteros", 100, 1.34)
            self.bow = Weapon("Mighty Bow", 13, 0.17)
            self.axe = Weapon("Thunder Axe", 19, 0.25)
            self.sho.equip_weapon(self.bow)
            self.sten.equip_weapon(self.axe)
            self.battle = Fight(self.sten, self.sho)

        def test_init(self):
            self.assertEqual(self.battle.hero, self.sten)
            self.assertEqual(self.battle.orc, self.sho)

        def test_player_order(self):
            pass

        def test_simulate_fight(self):
            self.battle.simulate_fight()
            self.assertTrue(self.sten.is_alive() ^ self.sho.is_alive())

        def test_fight_with_no_weapons_orc(self):
            self.sho.equipped_weapon = None
            self.battle.simulate_fight()
            self.assertTrue(self.sten.is_alive())

        def test_fight_with_no_weapons_hero(self):
            self.sten.equipped_weapon = None
            self.battle.simulate_fight()
            self.assertTrue(self.sho.is_alive())


if __name__ == '__main__':
    unittest.main()
