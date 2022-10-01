#This program calculates the sum of digits in 100!
#It is a solution to Problem 20 of ProjectEuler

import math

num = list(map(int,str(math.factorial(100))))
print(sum(num))
