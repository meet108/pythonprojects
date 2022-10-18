# 1. Q.1 Using Numpy library, generate the 20 random number starting from zero and ends at 100
#   a) Find out how many numbers are greater than 50
#   b) Check is any number is greater than 95
#   c) Check whether all the numbers are greater than 20
# Help: using sum, any, and all function
from numpy import random

x = random.randint(100, size=20)
print(x)
print(x[x>50])
print(any(x>95))
print(all(x>20))

