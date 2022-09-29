#This program gives the number that has largest Collatz Sequence under 1 million
#This is a solution to Problem-14 of ProjectEuler

max_chain = [0,0]
for x in range(1000000):
    chain_size = 0
    num = x
    while num > 1:
        if num%2 == 0:
            num = num/2
        else:
            num = 3*num+1 
        chain_size+=1
    if max_chain[0] < chain_size:
        max_chain[0] = chain_size
        max_chain[1] = x

print(max_chain)