import unittest
import numpy
from pizzerias import PizzeriasSearcher


class PizzeriasSearchTest(unittest.TestCase):
    def setUp(self):
        self.no_of_block = 5
        self.shop_locations = [[(3, 3), 2], [(1, 1), 2]]
        self.searcher = PizzeriasSearcher(self.no_of_block, self.shop_locations)

    def test_no_of_pizzeriass(self):
        self.assertEqual(len(self.shop_locations), self.searcher.no_of_pizzeriass,
                         "no_of_pizzeriass results incorrect.")

    def test_each_shop_matrix(self):
        res = self.searcher.each_shop_matrix(self.shop_locations[0])
        expected = numpy.array([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]])
        self.assertEqual(expected.tolist(), res.tolist(), "returned matrix for shop [(3, 3), 2] is not current")

        res = self.searcher.each_shop_matrix(self.shop_locations[1])
        expected = numpy.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]])
        self.assertEqual(expected.tolist(), res.tolist(), "returned matrix for shop [(3, 3), 2] is not current")

    def test_properties(self):
        expected = numpy.array([[0,0,1,0,0], [0,1,1,1,0], [2,1,1,1,1], [1,2,1,1,0], [1,1,2,0,0]])

        self.assertEqual(expected.tolist(), self.searcher.pizzerias_matrix.tolist(),
                         "the matrix for all cells the pizzerias could cover is in correct")

        self.assertEqual(2, self.searcher.maximum_in_the_city, "the returned maxinum incorrect")

        self.assertEqual({(1,3), (3,1), (2,2)}, self.searcher.best_home_locations,
                         "returned best location list incorrect")

    def test_number_in_location(self):
        self.assertEqual(1, self.searcher.number_in_location((1,1)), "number for cell (1,1) incorrect")
        self.assertEqual(2, self.searcher.number_in_location((1,3)), "number for cell (1,3) incorrect")
        self.assertEqual(2, self.searcher.number_in_location((3,1)), "number for cell (3,1) incorrect")