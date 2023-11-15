import random

print("Hello! Welcome to Rock, Paper, Scissors!")
player = input("Pick either 0, 1, or 2 for Rock, Paper, or Scissors, respectively. ")

player = int(player)

while (player != 0 and player != 1 and player != 2):
	player = int(input("Sorry, you must choose either 0, 1, or 2. "))

if (player == 0):
	print("You chose Rock!")
elif (player == 1):
	print("You chose Paper!")
else:
	print("You chose Scissors!")

computer = random.randint(0, 2)

if (computer == 0):
	print("The computer chose Rock!")
elif (computer == 1):
	print("The computer chose Paper!")
else:
	print("The computer chose Scissors!")

if (player == 0 and computer == 0):
	print("It's a tie!")
elif (player == 0 and computer == 1):
	print("Computer won! Better luck next time!")
elif (player == 0 and computer == 2):
	print("You won! Congratulations!")
elif (player == 1 and computer == 0):
	print("You won! Congratulations!")
elif (player == 1 and computer == 1):
	print("It's a tie!")
elif (player == 1 and computer == 2):
	print("Computer won! Better luck next time!")
elif (player == 2 and computer == 0):
	print("Computer won! Better luck next time!")
elif (player == 2 and computer == 1):
	print("You won! Congratulations")
else:
	print("It's a tie!")
