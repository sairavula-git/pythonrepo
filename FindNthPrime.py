# This program finds 10001th prime number and can be used to find any nth prime number
# This is solution to problem 7 of ProjectEuler
# I used my previous program logic to arrive at the solution

def list_of_prime(n):
    listofprime = [2]
    check = 3
    while len(listofprime) <= n:
        factors = 0
        for y in range(2, check):
            if check % y == 0:
                factors = factors + 1
                break
            if y * y > check:
                break
        if factors == 0:
            listofprime.append(check)
        check = check + 2
    return listofprime[n-1]


print(list_of_prime(10001))
