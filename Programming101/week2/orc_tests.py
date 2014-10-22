from orc import Orc
from weapon import Weapon
import unittest


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.sho = Orc("Vilasteros", 400, 1.34)
        self.bow = Weapon("Mighty Bow", 13, 0.17)

    def test_init(self):
        self.assertEqual(self.sho.berserk_factor, 1.34)

    def test_init_incorrect_berserk(self):
        with self.assertRaises(ValueError):
            Orc("Vilasteros2", 400, 2.32)

    def test_attack(self):
        self.assertEqual(self.sho.attack(), 0)
        self.sho.equip_weapon(self.bow)
        self.assertEqual(self.sho.attack(), 17.42)

if __name__ == '__main__':
    unittest.main()
