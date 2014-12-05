import unittest
from program_generator import construct_class_name


class ProgramGeneratorTests(unittest.TestCase):
    def test_construct_class_name(self):
        self.words = ['some', 'good', 'stuff']
        self.assertEqual(construct_class_name(self.words), 'SomeGoodStuffTests')

if __name__ == '__main__':
    unittest.main()
