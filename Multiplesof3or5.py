#This code provides the sum of multiples of 3 & 5 under 1000
#This is projectEuler problem 1.
int sum=0
for x in range(1000) 
if(x%3==0 ||x%5==0):
	sum=sum+x
	
print(sum)