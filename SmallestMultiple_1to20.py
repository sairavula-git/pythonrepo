#This is a program to find the smallest integer that is divisible by all numbers from 1 to 20
#This is the solution to 5th problem in ProjectEuler series

answr = 0
x = 20
check = 0
while(check != 19):
    check = 0
    for y in range(20,1,-1):
        if (x%y) != 0:
            break
        else:
            check = check + 1
    x = x + 20
    
print(x-20)
    