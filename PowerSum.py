#This problem find the sum of digits in 2^1000.
#This is solution to Problem 16 of ProjectEuler


def large_power_sum(num,exp):
    num_string = str(num**exp)
    digits = []
    for chars in num_string:
        digits.append(int(chars))
    return sum(digits)

print(large_power_sum(2,1000))
