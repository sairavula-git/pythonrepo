#This is a program to find the smallest integer that is divisible by all numbers from 1 to 20
#This is the solution to 4th problem in ProjectEuler series

answr = 0
for x in range(100000000, 1000000000):
    check = 0
    for y in range(2, 21):
        if x % y == 0:
            check = check + 1
    if check == 19:
        answr = x
        break
print(answr)
    