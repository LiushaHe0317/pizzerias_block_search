import unittest
from pizzerias import PizzeriasSearcher


class PizzeriasSearchTest(unittest.TestCase):
    def setUp(self):
        self.no_of_block = 25
        self.shop_locations = [[(5, 5), 8], [(10, 13), 5],
                               [(7, 19), 6], [(18, 9), 5]]
        self.searcher = PizzeriasSearcher(self.no_of_block, self.shop_locations)

    def test_each_shop_map(self):
        res = self.searcher.each_shop_map(self.shop_locations[0], self.no_of_block)
