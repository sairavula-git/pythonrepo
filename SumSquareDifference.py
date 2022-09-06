#This program finds the difference between sum of sqaures and square of sum of first 100 natural numbers
#This is solution to the 6th problem in ProjectEuler

def sumSquareDiff(n):
    sum = n * (n + 1) / 2
    sum_Square = sum * sum
    square_Sum = n * (n + 1) * (2 * n + 1) / 6
    diff = abs(sum_Square - square_Sum)
    return diff
    
print(sumSquareDiff(100))