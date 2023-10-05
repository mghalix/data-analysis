import pandas as pd

cars = pd.read_csv("./cars.csv", index_col=0)

for label, row_data in cars.iterrows():
    print(label)
    print(row_data)

# Adapt for loop
# The output should be in the form "country: cars_per_cap"
for lab, row in cars.iterrows():
    print(f"{lab}: {row['cars_per_cap']}")

#* Adding a column
# for lab, row in cars.iterrows():
#     cars.loc[lab, 'COUNTRY'] = row['country'].upper()

#! better approach than adding column inside of iterrows for loop (cuz every iteration it creates a series object)
# we wrote str before upper alone is a method so we need to get the function instead by using str.upper
cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)
