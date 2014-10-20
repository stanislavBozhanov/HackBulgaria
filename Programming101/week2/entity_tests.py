from entity import Entity
import unittest


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.en = Entity("Dude", "123")

    def test_init(self):
        self.assertEqual(self.en.name, "Dude")
        self.assertEqual(self.en.health, "123")

if __name__ == '__main__':
    unittest.main()
