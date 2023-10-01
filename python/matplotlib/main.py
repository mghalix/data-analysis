import matplotlib.pyplot as plt

age = [10, 20, 30, 40, 50, 60]
knowledge = [5, 60, 75, 80, 83, 70]

# plot (line)
plt.plot(age, knowledge)

plt.show()
plt.clf()

# scatter (dot)
plt.scatter(age, knowledge)

plt.show()
plt.clf()
