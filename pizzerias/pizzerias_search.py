from typing import Sequence
import numpy
import matplotlib.pyplot as plt


class PizzeriasSearcher:
    def __init__(self, n_of_block: int, shop_locations: Sequence):
        self.n_of_block = n_of_block
        self.city_matrix = numpy.zeros([self.n_of_block, self.n_of_block])
        self.shop_locations = shop_locations

    def each_shop_map(self, shop_loc: Sequence, n_of_block: int):
        """
        This method takes the location of a shop and dimensionality of the city, converts to a 2D ``numpy.ndarray``
            which indicates the whole area a pizzerias shop delivery service can cover.

        :param shop_loc: A sequence containing a tuple of two integers which indicate the coordinates on x- and y- axis and
            an integer which indicates the farthest distance a delivery guy can go.
        :param n_of_block: An integer which indicates the dimensionality of the city.
        :return: A 2D ``numpy.ndarray``.
        """
        ...

    @property
    def no_of_shops(self):
        return len(self.shop_locations)

    @property
    def pizzerias_matrix(self):
        """
        This property returns a matrix indicating the whole picture of pizzerias delivery services.
        """
        p_matrix = self.city_matrix
        for shop_loc in self.shop_locations:
            p_matrix += self.each_shop_map(shop_loc, self.n_of_block)
        return p_matrix

    @property
    def max_num(self):
        """
        This property returns the maximum a city block could have.
        """
        ...

    @property
    def best_homw_locations(self):
        """


        """
        ...

    def current_location(self, home_loc: Sequence[int, int]):
        """
        This method takes a tuple of two integers which indicate the coordinate of a given home location.

        :param home_loc: A tuple of integers.
        """
        ...

    def plot_pizzerias_matrix(self, pizzerias_matrix: numpy.ndarray):
        """
        This method plots a 2D ``numpy.ndarray`` of the matrix that pizzzerias delivery services cover..

        :param pizzerias_matrix: A 2D ``numpy.ndarray``.
        """
        ...

    def load(self):
        ...

    def save(self):
        ...