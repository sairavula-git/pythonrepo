#This program finds all amicable numbers below 10000 and gives their sum
#This is solution to Problem 21 of ProjectEuler

import math

def is_factor(num,factor):
    if not (num % factor):
        return True
    else:
        return False

fact_sum_dict = {}
amicable_nums = set({})

for num in range (2,10000):
    sum_fact = 1
    for factor in range (2,int(math.sqrt(num))+1):
        if is_factor(num,factor):
            factor2 = int(num/factor)
            if factor == factor2:
                sum_fact = sum_fact + factor
            else:
                sum_fact = sum_fact + factor + factor2
    fact_sum_dict.update({num:sum_fact})


for item,value in fact_sum_dict.items():
    if item != value:
        if fact_sum_dict.get(value) == item:
            amicable_nums.add(item)
            amicable_nums.add(value)

print(sum(amicable_nums))


