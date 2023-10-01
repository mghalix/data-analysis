import numpy as np

# seed(): sets the random seed, so that your results are reproducible between simulations.
# As an argument, it takes an integer of your choosing. If you call the function, no output will be generated
# hence the name pseudo-random (the computer uses it) because it's not purely random

np.random.seed(123)

# rand(): if you don't specify any arguments, it generates a random float between zero and one

print(np.random.rand())


# rolling some dice
print(np.random.randint(1, 7))
print(np.random.randint(1, 7))
