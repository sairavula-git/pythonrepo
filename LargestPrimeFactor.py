#This code gives the largest primefactor of a given number
#This is solution to problem 3 in projectEuler

print("Enter number to find the largest prime factor:")
num1 = int(input())
primeFactList = []
temp = 2
while temp*temp <= num1: 
    if num1 % temp == 0:
        temp2 = int(num1/temp) #temp & temp2 are factors
        fact_Count = 0 #To determine whether temp1 & temp2 are prime
        for x in range(2, int(temp/2)+1):
            fact_Count = 0
            if temp % x == 0:
                fact_Count=1
                break
        if fact_Count == 0:
            primeFactList.append(temp) 
        if temp != temp2:
            for x in range(2, int(temp2/2)+1):
                fact_Count = 0
                if temp2 % x == 0:
                    fact_Count = 1
                    break
            if fact_Count == 0:
                primeFactList.append(temp2)
    temp = temp+1
if len(primeFactList) > 0:
    primeFactList.sort()
    print("All prime factors are {}".format(primeFactList))
    print("Largest prime factor is {}".format(primeFactList[-1]))
else:
    print("The entered number is itself a prime value. Hence no other prime factors other than itself")