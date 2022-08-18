print("Fibonacci series upto: ")
userinput = int(input())
first=0
second=1
fibonacci_list = [0,1]
temp=second
third=first+second
if(userinput>0):
    while(third<=userinput):
        temp=second
        second=first+second
        first=temp
        fibonacci_list.append(second)
        third=first+second
    print("The list of fibonacci numbers upto {}: ".format(userinput))
    print(fibonacci_list)
    print("Total Count: {}".format(len(fibonacci_list)))
else:
    print("Please provide a positive integer value")