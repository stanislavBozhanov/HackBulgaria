import unittest
from pizza import *


class TestConsolePizzaOrders(unittest.TestCase):
    def setUp(self):
        self.orders = {}

    def test_get_command(self):
        cmnd = get_command('take Rado 10.0')
        self.assertEqual(cmnd[0], 'take')
        self.assertEqual(cmnd[1], 'Rado')
        self.assertEqual(cmnd[2], '10.0')

    def test_take_command(self):
        cmnd = ['take', 'Rado', '10.0']
        take_command(cmnd, self.orders)
        cmnd = ['take', 'Ivan', '6.43']
        take_command(cmnd, self.orders)
        self.assertEqual(self.orders['Rado'], 10.0)
        self.assertEqual(self.orders['Ivan'], 6.43)

if __name__ == '__main__':
    unittest.main()
