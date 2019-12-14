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

# if I live at cell (101, 106), I want to check the delivery service in my area
location = (101, 106)
searcher.check_location(location, report=True)

# if I check the area around me with 100 units
radius = 100
area_matrix, area_maximum, area_max_locs = searcher.check_area(location, radius=100, report=True)

# I can also check the whole city
city_matrix, city_maxmum, city_max_locs = searcher.check_city(report=True)

# now we could plot the matrix, so we could have a gut feeling for pizzerias delivery services
fig1 = plt.figure(1)
im1 = plt.imshow(city_matrix, cmap=plt.cm.get_cmap('jet'), interpolation='bicubic')
cbar1 = fig1.colorbar(im1)
plt.ylim(0, n_of_block)
plt.title('Pizzerias Delivery Map')
plt.show()

fig2 = plt.figure(2)
im2 = plt.imshow(area_matrix, cmap=plt.cm.get_cmap('jet'), interpolation='bicubic')
cbar2 = fig2.colorbar(im2)
plt.ylim(0, radius*2+1)
plt.title('Specified area map')
plt.show()
