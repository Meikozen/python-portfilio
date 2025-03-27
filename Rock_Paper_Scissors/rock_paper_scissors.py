import random

rock = 1
paper = 2
scissors = 3

#ask for user input and save to a value, user
user = input("Rock, Paper, or Scissors? ")

#add three if statements to save value to 1, 2, or 3 depending on if input is rock, paper, or scissors
if user == "rock":
    user = 1
elif user == "paper":
    user = 2
elif user == "scissors":
    user = 3

#use a random libary to generate a new value, save that value to a different variable, maybe 'CPU'?

CPU = random.randint(1, 3)
print(CPU)

if user == rock:
    if CPU == rock:
        print("Tie!")
    elif CPU == paper:
        print("You lose!")
    elif CPU == scissors:
        print("You win!")
if user == paper:
    if CPU == paper:
        print("Tie!")
    elif CPU == rock:
        print("You lose!")
    elif CPU == scissors:
        print("You win!")
if user == scissors:
    if CPU == scissors:
        print("Tie!")
    elif CPU == rock:
        print("You lose!")
    elif CPU == paper:
        print("You win!")
