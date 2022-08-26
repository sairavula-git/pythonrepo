#This is a fun game for addition of 3 digit numbers
#It gives the number of trials taken and time for arriving at the correct sum of two random numbers

from numpy import random
import time
user_Option = input("This game gives you two number to add.\nTo start playing press any key or to exit press X or x\n")

def addition_code():
    print("Give the sum of below numbers")
    num1 = random.randint(100,999)
    print(num1)
    num2 = random.randint(100,999)
    print(num2)
    init_Time = time.time() #initializing time after printing numbers and just before taking input
    print("Solution: ")
    user_Input = int(input())
    user_Try = 1
    while user_Input != num1 + num2:
        print("Wrong Answer, Please try again: ") 
        user_Input = int(input())
        user_Try = user_Try + 1 
        
    if user_Input == num1 + num2:
        fin_Time = time.time() #finalizing time just after obtaining correct answer
        time_Taken = fin_Time - init_Time
        print("Great! You got the right answer.")
        print("You have taken {} trials and {} seconds to arrive at the sum.".format(user_Try, time_Taken))

while user_Option != 'x' and user_Option != 'X':
    addition_code()
    user_Option = input("To continue playing press any key or to exit press X or x\n")