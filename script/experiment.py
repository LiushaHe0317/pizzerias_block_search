import matplotlib.pyplot as plt
from pizzerias import PizzeriasSample, PizzeriasSearcher


# set some default values
n_of_block = 1000
n_of_shop = 100
seed = 42

# mimic shop location and delivery distance sequence
sampler = PizzeriasSample(n_of_block, n_of_shops=n_of_shop, seed=seed)
shop_locs = sampler.sample()

searcher = PizzeriasSearcher(n_of_block, shop_locs)
matrix = searcher.pizzerias_matrix

# now we could plot the matrix, so we could have a gut feeling for pizzerias delivery services
fig = plt.figure(1)
im = plt.imshow(matrix, cmap=plt.cm.get_cmap('jet'), interpolation='bicubic')
cbar = fig.colorbar(im)
plt.ylim(0, n_of_block)
plt.title('Pizzerias Delivery Map')
plt.show()

# if I live at cell (101, 106)
num = searcher.number_in_location((200, 106))
if num == 0:
    print("Unforutnately, there is no delivery service in your are.")
else:
    print(f'Cool, {int(num)} pizzerias could cover your area.')

# if I need to know some where that has the most deliveries
locs = searcher.best_home_locations

print(f"There are {len(locs)} area(s) where {searcher.maximum_in_the_city} Pizzerias can cover, they are: ", locs)
