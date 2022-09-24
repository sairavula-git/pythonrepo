#This program finds a pythogorean triplet such that the sum of a,b,c is 1000
#This is solution to Problem 9 in Project Euler

for r in range (1,500):
    for s in range(1,500):
        for t in range(1,500):
            if r*r == 2 * s * t:
                if 3 * r + 2 * s + 2 * t == 1000:
                    x = r + s
                    y = r + t
                    z = r + s + t
                    break


print("{} {} {}".format(x,y,z))
print(x*y*z)