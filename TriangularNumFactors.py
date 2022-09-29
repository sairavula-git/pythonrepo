#This program finds the first Triangle number to have 500 factors
#This is solution to Problem 12 of Project Euler
import math
def fact_check(tri_num):
    factors = 2
    for x in range(2,int(math.sqrt(tri_num))):
        if tri_num % x == 0:
            y = tri_num / x
            if x == y:
                factors = factors + 1
            else:
                factors = factors + 2
    return factors

x=2
tri_num =1
factors = 1
while factors < 500:
    tri_num = tri_num + x
    print(tri_num)
    factors = fact_check(tri_num)
    if (factors >= 500):
        print("Triangular Number {}".format(tri_num))
        print("No. of factors are {}".format(factors))
        break
    x = x + 1