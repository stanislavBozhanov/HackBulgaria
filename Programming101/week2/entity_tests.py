from entity import Entity
import unittest


class Teentity(unittest.TestCase):
    def setUp(self):
        self.en = Entity("Dude", 100)

    def test_init(self):
        self.assertEqual(self.en.name, "Dude")
        self.assertEqual(self.en.health, 100)

    def test_is_alive(self):
        self.assertTrue(self.en.is_alive())

    def test_not_alive(self):
        self.en.health = 0
        self.assertFalse(self.en.is_alive())

    def test_take_damage(self):
        self.en.take_damage(50)
        self.assertEqual(self.en.health, 50)
        self.en.take_damage(60)
        self.assertEqual(self.en.health, 0)

    def test_take_healing(self):
        self.en.health = 50
        self.assertTrue(self.en.take_healing(20))
        self.assertEqual(self.en.health, 70)

    def test_take_healing_above_max(self):
        self.en.health = 20
        self.en.take_healing(120)
        self.assertEqual(self.en.health, 100)

    def test_healing_on_dead(self):
        self.en.health = 0
        self.assertFalse(self.en.take_healing(100))

if __name__ == '__main__':
    unittest.main()
