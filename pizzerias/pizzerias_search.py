from typing import Sequence
import numpy


class PizzeriasSearcher:
    """
    This object takes the size of the city and number of shops, and construct the matrices each shop delivery can cover
        and number of delivery for each cell in the city. It can also computes number of delivery for a given cell,
        maximum of number of delivery, and a sequence of cell coordinates which have the maximum.

    :param n_of_block: An integer which indicates the size of the city.
    :param shop_covers: A sequence of sequences, each sequence contains a tuple of two integers representing the
        coordinate of a pizzerias shop and an integer representing the distance the shop could cover.
    """
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

    def area_matrix(self, loc: Sequence, radius: int):
        """
        This method takes a tuple of coordinates and a radius, construct a sub-matrix of the city matrix accordingly.

        :param loc: A tuple of integers.
        :param radius: An integer.
        :return: A 2D ``numpy.ndarray``.
        """
        x_initial, y_initial = loc

        if y_initial < 0 or x_initial > self.n_of_block or x_initial < 0 or y_initial > self.n_of_block:
            raise ValueError('The location is out of city range.')
        else:
            y_center = self.n_of_block - y_initial
            x_center = x_initial - 1

            low0 = y_center - radius if y_center - radius >= 0 else 0
            high0 = y_center + radius + 1 if y_center + radius + 1 <= self.n_of_block else self.n_of_block
            left1 = x_center - radius if x_center - radius >= 0 else 0
            right1 = x_center + radius + 1 if x_center + radius + 1 <= self.n_of_block else self.n_of_block

            return self.pizzerias_matrix[low0: high0, left1: right1]

    def maximum_in_matrix(self, matrix=None):
        """
        This method returns the maximum a city block could have.

        :param matrix: A ``numpy.ndarray``.
        :return: An integer.
        """
        if isinstance(matrix, numpy.ndarray):
            return int(numpy.amax(matrix))
        elif matrix is None:
            return int(numpy.amax(self.pizzerias_matrix))
        else:
            raise Exception('Accept numpy.ndarray only!')

    def max_locations(self, matrix=None, d0_start=0, d1_start=0):
        """
        This method returns a set of cells which have maximum.

        :param matrix: A ``numpy.ndarray`.
        :param d0_start: An integer.
        :param d1_start: An integer.
        :return: A set of tuples.
        """
        if matrix is None:
            d0, d1 = numpy.where(self.pizzerias_matrix == numpy.amax(self.pizzerias_matrix))
            return {(x + 1, self.n_of_block - d0[i]) for i, x in enumerate(d1)}
        elif isinstance(matrix, numpy.ndarray):
            d0, d1 = numpy.where(matrix == numpy.amax(matrix))
            return {(x + 1 + d1_start, self.n_of_block - (d0[i] + d0_start)) for i, x in enumerate(d1)}
        else:
            raise Exception('Accept numpy.ndarray only!')

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

    def check_location(self, home_loc: Sequence, report=False):
        """
        This method takes a tuple of two integers which indicate the coordinate of a given home location.

        :param home_loc: A tuple of integers.
        :return: number of delivery in the current location.
        """
        num = self.pizzerias_matrix[self.n_of_block - home_loc[1], home_loc[0] - 1]
        if report:
            if num == 0:
                print("Unfortunately, there is no delivery service in your current location.")
            else:
                print(f'Cool, {int(num)} pizzerias could cover your current location.')
        return num

    def check_area(self, loc: Sequence, radius: int, report=False):
        """
        This method takes a location coordinate and a radius and search the delivery services around this specified area.

        :param loc: A tuple of integers.
        :param radius: An integer.
        :param report: A boolean that indicates whether or not print a report.
        return:
            - A sub-matrix of the pizzerias matrix which is created in terms of specified range.
            - A maximum in this area.
            - A set of cells that have maximum.
        """
        matrix = self.area_matrix(loc, radius)
        x_initial, y_initial = loc

        y_center = self.n_of_block - y_initial
        x_center = x_initial - 1

        low0 = y_center - radius if y_center - radius >= 0 else 0
        left1 = x_center - radius if x_center - radius >= 0 else 0

        maximum = self.maximum_in_matrix(matrix)
        max_set = self.max_locations(matrix=matrix, d0_start=low0, d1_start=left1)

        if report:
            print(f"In the given area, there are {len(max_set)} areas where {maximum} Pizzerias delivery service "
                  f"can cover, they are: ", max_set)

        return matrix, maximum, max_set

    def check_city(self, report=False):
        """
        This method returns the matrix, the maximum and a set of maximum tuple of cells.

        :param report: A boolean indicating whether or not print report.
        :return:
            - The pizzerias matrix.
            - A maximum in this the pizzerias matrix.
            - A set of cells that have maximum.
        """
        if report:
            print(f"There are {len(self.max_locations())} area(s) where {self.maximum_in_matrix()} Pizzerias can cover, "
                  f"they are: ", self.max_locations())

        return self.pizzerias_matrix, self.maximum_in_matrix(), self.max_locations()