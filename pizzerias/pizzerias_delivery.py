import random


class PizzeriasSample:
    def __init__(self, n_of_blocks: int, n_of_shops=1000, dist_range=100, seed=None):
        self.n_of_blocks = n_of_blocks
        self.n_of_shops = n_of_shops
        self.dist_range = dist_range
        self.random_gen = random
        if seed:
            self.random_gen.seed(seed)

    def sample(self):
        cell_range = list(range(1, self.n_of_blocks+1))

        x_list = self.random_gen.sample(cell_range, self.n_of_shops)
        y_list = self.random_gen.sample(cell_range, self.n_of_shops)
        dist_list = self.random_gen.sample(list(range(1, self.dist_range+1)), self.n_of_shops)

        return [[(x_list[i], y_list[i]), dist_list[i]] for i in range(self.n_of_shops)]
