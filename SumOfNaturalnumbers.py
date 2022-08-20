#This program prints either sum or product of first n natural numbers
print("Range of natural numbers to be considered upto: ")
userInput = int(input())
sumOfN = userInput * (userInput + 1) / 2
prodOfN = 1
for x in range (1, userInput + 1):
    prodOfN=prodOfN*x
    
print("Sum of first {} natural numbers is ".format(sumOfN))
print("Product of first {} natural numbers is ".format(prodOfN))