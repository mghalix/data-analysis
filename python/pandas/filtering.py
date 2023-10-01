# Countries that has drives_right as True
# Import cars data
import pandas as pd
import numpy as np

cars = pd.read_csv('cars.csv', index_col = 0)

print(cars[cars['drives_right']])

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']

many_cars = cpc > 500

car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]



# Print medium
print(medium)
