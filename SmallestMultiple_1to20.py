#This is a program to find the smallest integer that is divisible by all numbers from 1 to 20
#This is the solution to 5th problem in ProjectEuler series

x = 20 #starting from x to obtain efficiency
check = 1
while(check != 20): #We will run until we find a number divisible by all 1 to 20
    check = 1
    for y in range(20,1,-1):
        if (x%y) != 0: #if not divisible at any stage break this loop and run for x+20
            break
        else:
            check = check + 1 
    x = x + 20
    
print(x-20)
    