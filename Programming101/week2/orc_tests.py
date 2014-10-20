from orc import Orc
import unittest


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.sho = Orc("Vilasteros", 400, 1.34353)

    def test_init(self):
        self.assertEqual(self.sho.berserk_factor, 1.34353)

    def test_init_incorrect_berserk(self):
        with self.assertRaises(ValueError):
            Orc("Vilasteros2", 400, 2.32434)


if __name__ == '__main__':
    unittest.main()
