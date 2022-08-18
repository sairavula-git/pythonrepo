#This is a normal program to find the Highest Common Factor between two given numbers
#This was written in preparation for a solution to another ProjectEuler problem

print("Enter the First number:")
num1=int(input())
print("Enter the Second number:")
num2=int(input())
temp=1
fact1={num1}
fact2={num2}
while(temp+temp<=num1):
    if(num1%temp==0):
        fact1.add(temp)
    temp=temp+1
temp=1
while(temp+temp<=num2):
    if(num2%temp==0):
        fact2.add(temp)
    temp=temp+1
  
comFactSet=fact1.intersection(fact2)
comFactList=list(comFactSet)
comFactList.sort()
print("The highest common factor is {}".format(comFactList[-1]))