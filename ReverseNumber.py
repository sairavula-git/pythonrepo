user_Input = int(input("Enter the number to be reversed: "))
temp = 0
while user_Input > 0:
    temp = temp * 10
    temp = temp + user_Input % 10
    user_Input = int(user_Input / 10)
    
print(temp)