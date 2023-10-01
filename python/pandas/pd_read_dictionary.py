# Pre-defined lists
# country names for which data is available.
names = ["United States", "Australia", "Japan", "India", "Russia", "Morocco", "Egypt"]
# a list with booleans that tells whether people drive left or right in the corresponding country.
dr = [True, False, False, False, True, True, True]
# the number of motor vehicles per 1000 people in the corresponding country.
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd


# Create dictionary my_dict with three key:value pairs: my_dict
dict = {
    "country": [
        "United States",
        "Australia",
        "Japan",
        "India",
        "Russia",
        "Morocco",
        "Egypt",
    ],
    "drives_right": [True, False, False, False, True, True, True],
    "cars_per_cap": [809, 731, 588, 18, 200, 70, 45],
}


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(dict)

# Print cars
# print(cars) # indexes comes out as 0 to 7

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)