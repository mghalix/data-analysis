import pandas as pd

# Import the cars.csv data: cars
df = pd.read_csv("./cars.csv", index_col=0) # index_col to set the index as first column in the excel file instead of generating 0-n indexes

# Print out cars
print(df)
