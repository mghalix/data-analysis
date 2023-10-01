'''
    Scenario: You bet your friend you are going to reach at least 60 steps of the empire state building
    by rolling a dice 100 times, each time if the dice is 1, 2 you go one step down, if the dice is
    3, 4, 5 you go one step up, if the dice is 6 you roll the dice again and go the new dice amount of steps
    - Ultimately we also want to know what are the chances you meet that bet (can be achieved by
    simulating the bet 1000 times for example then plot the distribution)
'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)


all_walks = []

for _ in range(500):
    random_walk = [0]
    for x in range(100):
        # Set step: last element in random_walk
        step = random_walk[-1]

        # Roll the dice
        dice = np.random.randint(1,7)

        # Determine next step
        if dice <= 2:
            step = step - 1
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # there is 0.5% chance you fall down
        if np.random.rand() <= 0.001:
            step = 0

        # append next_step to random_walk
        random_walk.append(max(0, step)) # cuz you can't go below 0 steps
    all_walks.append(random_walk)

# Print random_walk
# print(random_walk)
np_rw = np.array(random_walk)

# Visualizing the walk
plt.plot(np_rw)
plt.xlabel = "Step"
plt.ylabel = "Dice Roll"

plt.show()
plt.clf()

# Print all_walks
# print(all_walks)

np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw) # to have all the end steps at the last row

# Visualizing every walk to see clear distribution
plt.plot(np_aw_t)
plt.show()
plt.clf()


# the chance of reaching 60 step
ends = np_aw_t[-1,:]
plt.hist(ends)
plt.show()

# calculate odds
odds = ends[ends >= 60]
print(len(odds) / len(ends) * 100)