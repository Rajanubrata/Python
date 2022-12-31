#Number Guessing Game Objectives:
import art 
import random
import sys
# Include an ASCII art logo.
print(art.logo)
#set a random number between 1 and 100
number = random.randint(1,100)
#ask user to choose deficulty
print("Welcome to the number guessing game \nI'm thinking of a number between 1 and 100 \n")
dificulity = input("Choose a dificulty : Type 'easy' or 'hard' : ")

LifeLine=0
  
if dificulity == "easy":
    LifeLine=10
    print(f"You have {LifeLine} lives left") 
elif dificulity == "hard":
    LifeLine=5
    print(f"You have {LifeLine} lives left")
else:
  print("You must choose a dificulty")
  sys.exit()
  
# Allow the player to submit a guess for a number between 1 and 100.
while LifeLine > 0:
  user_guess = int(input("Make a Guess : "))
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  if user_guess < number:
    print("Too low")
    LifeLine = LifeLine - 1
    print(f"You have {LifeLine} lives left")
  elif user_guess > number:
    print("Too high")
    LifeLine = LifeLine - 1
    print(f"You have {LifeLine} lives left")
  else:
    print("Correct Guess !\nYou Win 😀")
    break
if LifeLine == 0:
  print("You Lose 😎")
  print(f"My Guess was {number}")
