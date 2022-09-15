#This is just a basic program for implementing recursion

def num_print(x,n):
    if x <= n:
        print(x)
        x = x + 1
        num_print(x,n)

num_print(1,5)