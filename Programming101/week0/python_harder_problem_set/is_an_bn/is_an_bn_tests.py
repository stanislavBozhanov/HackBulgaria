import unittest
from is_an_bn import is_an_bn


class IsAnBnWordTests(unittest.TestCase):
    def test_for_correct_output(self):
        self.assertTrue(is_an_bn("aaaaabbbbb"))
        self.assertFalse(is_an_bn("aaabbbbb"))
        self.assertFalse(is_an_bn("a abb"))
        self.assertFalse(is_an_bn("aabbab"))
        self.assertFalse(is_an_bn("AAaaBBbb"))

if __name__ == '__main__':
    unittest.main()
