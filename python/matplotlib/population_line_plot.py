import matplotlib.pyplot as plt

year = [1950, 1951, 1952, 2100]
pop = [2.538, 2.57, 2.62, 10.85]

plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')

plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])
# the second argument is for yticks names, they should be the same size as the first arg and B here stands for Billion.
plt.show()
