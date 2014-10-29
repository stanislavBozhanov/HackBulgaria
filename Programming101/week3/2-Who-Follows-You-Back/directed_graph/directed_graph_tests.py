import unittest
from directed_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.fr = DirectedGraph()
        self.fr.add_edge('sten', 'sho')
        self.fr.add_edge('sten', 'agito')
        self.fr.add_edge('sho', 'zina')
        self.fr.add_edge('sho', 'tom')
        self.fr.add_edge('tom', 'jerry')
        self.fr.add_edge('zina', 'agito')
        self.fr.add_edge('zina', 'sho')

    def test_add_edge(self):
        self.assertIn('sho', self.fr.graph['sten'])
        self.assertIn('agito', self.fr.graph['sten'])

    def test_get_neighbors(self):
        self.assertEqual(self.fr.get_neighbors_for('sten'), ['sho', 'agito'])

    def test_path_between_direct(self):
        self.assertTrue(self.fr.path_between('sten', 'sho'))

    def test_path_between_indirect(self):
        self.assertTrue(self.fr.path_between('sten', 'zina'))
        self.assertTrue(self.fr.path_between('sten', 'jerry'))

    def test_path_between_no_path(self):
        self.assertFalse(self.fr.path_between('agito', 'zina'))

    def test_path_between_with_loops(self):
        self.assertFalse(self.fr.path_between('agito', 'zina'))


if __name__ == '__main__':
    unittest.main()
