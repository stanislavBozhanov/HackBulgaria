import os.path
from dungeon import Dungeon
import unittest


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.filepath = "basic_dungeon.txt"
        self.dun = Dungeon(self.filepath)

    def test_if_path_exists(self):
        self.assertTrue(os.path.isfile(self.filepath))

    def test_init(self):
        self.assertEqual(self.dun.filepath, self.filepath)

    def test_if_starting_point_exists(self):
        my_file = open(self.filepath, 'r')
        content = my_file.read()
        self.assertIn('S', content)
        my_file.close()

    

if __name__ == '__main__':
    unittest.main()
