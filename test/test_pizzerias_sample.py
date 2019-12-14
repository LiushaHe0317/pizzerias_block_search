import unittest
from pizzerias import PizzeriasSample


class PizzeriasSampleTest(unittest.TestCase):
    def test_sample(self):
        n_of_block = 1000
        n_of_shop = 10
        seed = 42

        sampler = PizzeriasSample(n_of_block, n_of_shops=n_of_shop, seed=seed)
        res = [[(655, 693), 28], [(115, 759), 30], [(26, 914), 65], [(760, 559), 78], [(282, 90), 4], [(251, 605), 72],
               [(229, 433), 26], [(143, 33), 92], [(755, 31), 84], [(105, 96), 90]]
        self.assertEqual(res, sampler.sample(), "results of sample() method incorrect")