#This is a random program for fun. 
#The user need to guess a random integer based on given clues.

from numpy import random
randomNumber = random.randint(1,100)
print("Guess the random integer from 1 to 100:")
userGuess = int(input())
guessSet = { userGuess }
while userGuess != randomNumber:
	if userGuess < randomNumber:
		print("It's higher than {}. Provide a higher number: ".format(userGuess))
	elif userGuess > randomNumber:
		print("The number is lower than {}. Provide lesser number: ".format(userGuess))		
	userGuess = int(input())
	guessSet.add(userGuess)
if userGuess == randomNumber:
	print("Congratulations! {} is the correct guess".format(randomNumber))
	print("You have taken {} chances".format(len(guessSet)))


	