# loc  => label-based (which means that you have to specify rows and columns based on their row and column labels. )
# iloc =>  integer index based (so you have to specify rows and columns by their integer index like you did in the previous exercise.)

# Import cars data
import pandas as pd
cars = pd.read_csv('./cars.csv', index_col = 0)


# Print out observation for Japan
print(cars.loc['JAP'])
print(cars.iloc[2])


# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])
print(cars.iloc[5, 2])

# Print sub-DataFrameA (observations for Russia and Morocco and the columns country and drives_right)
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
print(cars.iloc[[4, 5], [1, 2]])

# It's also possible to select only columns with loc and iloc. In both cases,
# you simply put a slice going from beginning to end in front of the comma


# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])
print(cars.iloc[:, [2]])


# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
print(cars.iloc[:, [0, 2]])