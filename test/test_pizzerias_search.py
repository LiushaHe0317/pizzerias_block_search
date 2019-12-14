import unittest
import numpy
from pizzerias import PizzeriasSearcher


class PizzeriasSearchTest(unittest.TestCase):
    def setUp(self):
        self.no_of_block = 5
        self.shop_locations = [[(3, 3), 2], [(1, 1), 2]]
        self.searcher = PizzeriasSearcher(self.no_of_block, self.shop_locations)

    def test_each_shop_matrix(self):
        res = self.searcher.each_shop_matrix(self.shop_locations[0])
        expected = numpy.array([[0,0,1,0,0],[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]])
        self.assertEqual(expected.tolist(), res.tolist(), "returned matrix for shop [(3, 3), 2] is not current")

        res = self.searcher.each_shop_matrix(self.shop_locations[1])
        expected = numpy.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]])
        self.assertEqual(expected.tolist(), res.tolist(), "returned matrix for shop [(3, 3), 2] is not current")

    def test_maximum_in_matrix(self):
        self.assertEqual(2, self.searcher.maximum_in_matrix(), "returned maximum incorrect")
        matrix = numpy.array([[0,0,0],[1,1,1],[0,0,3]])
        self.assertEqual(3, self.searcher.maximum_in_matrix(matrix), "returned maximum incorrect")

    def test_max_locations(self):
        # test if matrix = None
        self.assertEqual({(1,3), (3,1), (2,2)}, self.searcher.max_locations(),
                         "returned best location list incorrect")
        # test if matrix
        matrix = self.searcher.pizzerias_matrix[2:5,2:5]
        self.assertEqual({(3,1)}, self.searcher.max_locations(matrix, d0_start=2, d1_start=2),
                         "the set coordinates incorrect.")

    def test_number_in_location(self):
        self.assertEqual(1, self.searcher.check_location((1,1)), "number for cell (1,1) incorrect")
        self.assertEqual(2, self.searcher.check_location((1,3)), "number for cell (1,3) incorrect")
        self.assertEqual(2, self.searcher.check_location((3,1)), "number for cell (3,1) incorrect")

    def test_area_matrix(self):
        matrix = [[1,1,1],[1,1,1],[2,1,1]]
        self.assertEqual(matrix, self.searcher.area_matrix((3,3), 1).tolist(), "returned area matrix incorrect")
        self.assertEqual((3,3), self.searcher.area_matrix((3,3), 1).shape, "returned matrix shape incorrect")

    def test_properties(self):
        expected = numpy.array([[0,0,1,0,0], [0,1,1,1,0], [2,1,1,1,1], [1,2,1,1,0], [1,1,2,0,0]])

        self.assertEqual(expected.tolist(), self.searcher.pizzerias_matrix.tolist(),
                         "the matrix for all cells the pizzerias could cover is in correct")
        self.assertEqual(len(self.shop_locations), self.searcher.no_of_pizzeriass,
                         "no_of_pizzeriass results incorrect.")

    @unittest.skip('This method calls other methods does not need to duplicate the test.')
    def test_check_are(self):
        pass

    @unittest.skip('This method calls other methods does not need to duplicate the test.')
    def test_check_city(self):
        pass