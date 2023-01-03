from art import logo , vs
from game_data import data 
import random
from replit import clear
#Display art
print(logo)
Score=0
game_should_continue=True
account_b = random.choice(data)
def format_data(account):
  #Format the acount data into printable format 
  account_name = account["name"]
  account_descr=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_descr} , from {account_country}"

def check_answer(guess , a_follower_count, b_follower_count):
  if a_follower_count > b_follower_count:
    return guess=="a"
  else:
    return guess=="b"

#Generate a random account from the game data
while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b=random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  #Ask user for a guess
  guess=input("Who has more followers ? A or B : ").lower()
  
  #Check user is correct or not 
  ## Get follower count for each account 
  ## use if statement to check if user is correct 
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  clear()
  print(logo)
  #Give user a feedback on their guess
  if is_correct:
    Score+=1
    print(f"You're right! Current Score = {Score}")
    
  else:
    print(f"Sorry ! Thats wrong . Final Score : {Score}")
    game_should_continue=False
  
