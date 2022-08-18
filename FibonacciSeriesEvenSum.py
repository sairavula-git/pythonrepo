first=0
second=1
fibonacci_list = [0,1]
temp=second
third=first+second
sum=0
while(third<=4000000):
    temp=second
    second=first+second
    first=temp
    fibonacci_list.append(second)
    third=first+second
for x in fibonacci_list:
    if(x%2==0):
        sum=sum+x
print(sum)
