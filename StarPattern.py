def star_pattern(n):
    for x in range(1,n+1):
        for y in range(1,x+1):
            print("*", end = " ")
        print()
def rev_star(n):
    for x in range(n,0,-1):
        for y in range(x,0,-1):
            print("*", end = " ")
        print()
def square_pattern(n):
    for x in range(n):
        for y in range(n):
            print("*", end = " ")
        print()
def triangle_pattern(n):
    start = n
    end = n+1
    if n%2 != 0:
        end = start
    for rows in range(n):
        for x in range (1,start+1):
            print(" ", end=" ")
        for x in range (start, end+1):
            print("*", end=" ")
        for x in range (1,start+1):
            print(" ", end=" ")
        start = start -1
        end = end + 1
        print()

user_Input = input("Enter the number of rows in the pattern: ")
star_pattern(int(user_Input))
rev_star(int(user_Input))
square_pattern(int(user_Input))
triangle_pattern(int(user_Input))