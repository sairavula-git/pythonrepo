#This code gives the sum of all even fibonacci numbers less than 4 million
#This is the second problem in projectEuler
first=0
second=1
fibonacci_list = [0,1] #initializing fibonacci list
temp=second
#third=first+second 
sum=0
while(second<=4000000): #making sure that the number doesn't exceed 4 million
    temp=second
    second=first+second
    first=temp
    fibonacci_list.append(second)
    #third=first+second #optimised the code by removing redundant parts
for x in fibonacci_list:
    if(x%2==0):
        sum=sum+x
print(sum)
