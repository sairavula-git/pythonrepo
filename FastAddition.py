#This is a fun game for addition of 3 digit numbers
#It gives the number of trials taken and time for arriving at the correct sum of two random numbers

from numpy import random
import time
import os
import math
os.system('cls')
user_Option = input('''\t\tWelcome to the Math Quiz Game: \n
                    Please read the instructions carefully before you proceed\n
                        1. This game gives you Ten addition questions.
                        2. You need to answer the question correctly within 10 seconds.
                        3. You will get 10 points for correct answer in first attempt within 5 seconds
                        4. After 5 seconds you will loose a point for each second.
                        5. You will have 3 attempts to answer and for each wrong attempt you will loose 2 points.
                        6. If you can't answer within 3 attempts or 10 secs you get No points for the question.
                        7. Aggregate score is displayed at the end.
                        
                    \nTo start playing press 's' or 'S' and Enter or to exit press X or x and Enter\n''')

def addition_code(qnum):
    print(f"{qnum}.Give the sum of below numbers")
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    print(f"{num1} + {num2} = ")
    init_Time = time.time() #initializing time after printing numbers and just before taking input
    user_Input = int(input())
    user_Try = 1
    score = 0
    while user_Input != num1 + num2:
        user_Try = user_Try + 1
        if user_Try > 3:
            print("Sorry maximum number of trials exceeded for this question")
            time.sleep(3)
            break
        print("Wrong Answer, Please try again: ") 
        user_Input = int(input())
        
        
    if user_Input == num1 + num2:
        fin_Time = time.time() #finalizing time just after obtaining correct answer
        time_Taken = fin_Time - init_Time
        if time_Taken <= 5:
            score = 10-2*(user_Try-1)
        elif time_Taken <=10:
            score = 10-(math.ceil(time_Taken)-5)-2*(user_Try-1)
        print("Great! You got the right answer.")
        print(f"You have taken {user_Try} attempts and {time_Taken:.2f} seconds.\n You scored {score} points")
        time.sleep(3)
        return score
    return score

if user_Option == 's' or user_Option == 'S':
    score = 0
    for x in range(10):
        os.system('cls')
        score = score + addition_code(x+1)       
    if score > 90:
        print(f"\t\tCongratulations!! You have scored {score:.2f} & that's outstanding.\n")
    elif score >80:
        print(f"\t\tGood job! You scored {score:.2f} and it's impressive\n")
    elif score >60:
        print(f"\t\tGood job! You scored {score:.2f} and can do better\n")
    elif score >40:
        print(f"\t\tYou scored {score:.2f}. Just stay calm and you could do better\n")
    else:
        print(f"\t\tYou scored {score:.2f} and need to work on your math\n")