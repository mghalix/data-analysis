# https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-4-numpy?ex=1
# -----------------------------------------------------------------------------
# Got It!
# 1. NumPy
'''
Wow, you've done well and by now, you are aware

2. Lists Recap
that the Python list is pretty powerful. A list can hold any type and can hold different types at the same time. You can also change, add and remove elements. This is wonderful, but one feature is missing, a feature that is super important for aspiring data scientists as yourself. #* When analyzing data, you'll often want to carry out operations over entire collections of values, and you want to do this fast. With lists, this is a problem.'''

# 3. Illustration
# Let's retake the heights of your family and yourself. Suppose you've also asked for everybody's weight. It's not very polite, but everything for science, right? #* You end up with two lists, height, and weight. The first person is 1-point-73 meters tall and weighs 65-point-4 kilograms. If you now want to calculate the Body Mass Index for each family member, you'd hope that this call can work, making the calculations element-wise.
#! Unfortunately, Python throws an error, because it has no idea how to do calculations on lists. You could solve this by going through each list element one after the other, and calculating the BMI for each person separately, but this is terribly inefficient and tiresome to write.
# -----------------------------------------------------------------------------
# -> Problem
# height = [1.73, 1.68, 1.71, 1.89, 1.79]
# weight = [65.4, 59.2, 63.6, 88.4, 68.7]
# bmi = weight / height**2 #! throws an error here
# print(bmi)
# -----------------------------------------------------------------------------
# -> Solution
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
#! notice how you can perform operations on np arrays unlike lists
bmi = np_weight / np_height**2
print(bmi)
print(bmi > 23)  # list of corresponding booleans
print(bmi[bmi > 23])  # subsetting
# -----------------------------------------------------------------------------
print(np.array([True, 1, 2]) + np.array([3, 4, False]))
