print("Enter number to find the largest prime factor:")
num1 = int(input())
primeFactList = []
temp = 2
while temp*temp <= num1: 
    if num1 % temp == 0:
        temp2 = int(num1/temp) #temp & temp2 are factors
        for x in range(2, int(temp/2)+1):
            count = 0
            if temp % x == 0:
                count=1
                break
        if count == 0:
            primeFactList.append(temp) 
        if temp != temp2:
            for x in range(2, int(temp2/2)+1):
                count = 0
                if temp2 % x == 0:
                    count = 1
                    break
            if count == 0:
                primeFactList.append(temp2)
    temp = temp+1
primeFactList.sort()
print("All prime factors are {}".format(primeFactList))
print("Largest prime factor is {}".format(primeFactList[-1]))