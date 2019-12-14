from typing import Sequence
import numpy
import matplotlib.pyplot as plt


class PizzeriasSearcher:
    def __init__(self, n_of_block: int, shop_covers: Sequence):
        self.n_of_block = n_of_block
        self.shop_covers = shop_covers

    def each_shop_matrix(self, shop_loc: Sequence):
        """
        This method takes the location of a shop and dimensionality of the city, converts to a 2D ``numpy.ndarray``
            which indicates the whole area a pizzerias shop delivery service can cover.

        :param shop_loc: A sequence containing a tuple of two integers which indicate the coordinates on x- and y- axis and
            an integer which indicates the farthest distance a delivery guy can go.
        :return: A 2D ``numpy.ndarray``.
        """
        (x_initial, y_initial), r = shop_loc
        matrix = numpy.zeros([self.n_of_block, self.n_of_block])

        # convert x, y coordinates
        x_center = x_initial - 1                # in numpy, x axis = 1
        y_center = self.n_of_block - y_initial  # in numpy, y axis = 0

        # create a list of x or y coordinate which indicates the cells the shop could cover
        x_list = [x for x in range(x_center-r, x_center+r+1) if x >= 0 and x < self.n_of_block]
        # y_list = [y for y in range(y_center-r, y_center+r+1) if y >= 0 and y <= n_of_block-1]

        for d1 in x_list:
            high_bound = y_center + r - numpy.abs(d1 - x_center) + 1
            low_bound = y_center - r + numpy.abs(d1 - x_center)
            matrix[low_bound:high_bound, d1] = 1

        return matrix

    def number_in_location(self, home_loc: Sequence):
        """
        This method takes a tuple of two integers which indicate the coordinate of a given home location.

        :param home_loc: A tuple of integers.
        :return: number of delivery in the current location.
        """
        return self.pizzerias_matrix[self.n_of_block - home_loc[1], home_loc[0] - 1]

    def plot_pizzerias_matrix(self, pizzerias_matrix: numpy.ndarray):
        """
        This method plots a 2D ``numpy.ndarray`` of the matrix that pizzzerias delivery services cover..

        :param pizzerias_matrix: A 2D ``numpy.ndarray``.
        """
        ...

    @property
    def no_of_pizzeriass(self):
        """
        This method returns the total number of shops in the city.
        """
        return len(self.shop_covers)

    @property
    def pizzerias_matrix(self):
        """
        This method returns a matrix indicating the whole picture of pizzerias delivery services.
        """
        p_matrix = numpy.zeros([self.n_of_block, self.n_of_block])
        for shop_loc in self.shop_covers:
            p_matrix += self.each_shop_matrix(shop_loc)
        return p_matrix

    @property
    def maximum_in_the_city(self):
        """
        This method returns the maximum a city block could have.
        """
        return int(numpy.amax(self.pizzerias_matrix))

    @property
    def best_home_locations(self):
        """
        This method returns a set of all locations with the maximum number of delivery services.
        """
        d0, d1 = numpy.where(self.pizzerias_matrix == numpy.amax(self.pizzerias_matrix))
        return {(x + 1, self.n_of_block - d0[i]) for i, x in enumerate(d1)}
