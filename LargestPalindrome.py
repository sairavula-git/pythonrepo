#This code gives the largest palindrome formed as a product of two three digit numbers
#This is solution to the Fourth problem in ProjectEuler series
palin_List = [0]
for x in range(100,999):
	for y in range(100,999):
		prod = x * y
		prod_Str = str(prod)
		len_Prod = len(prod_Str)
		rev_Prod = ''
		k = -1
		for z in range(0, len_Prod):
			rev_Prod += prod_Str[k]
			k = k - 1
		if prod_Str == rev_Prod:
			palin_List.append(prod)
palin_List.sort()
print(palin_List[-1])