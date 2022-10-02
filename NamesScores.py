#This is solution to Problem22 of ProjectEuler
#The problem description would describe the functionality better

#Using names.txt, a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score

import csv

f = open("p022_names.txt")
names = next(csv.reader(f)) #reading the names from file and storing them as a list
names.sort()
total_score = 0
for index,name in enumerate(names):
    score = 0
    for char in name:
        score = score + ord(char)-64 #Subtracting 64 from ASCII value of alphabet for alphabetlical value
    score = score * (index+1)
    total_score = total_score + score

print(total_score)