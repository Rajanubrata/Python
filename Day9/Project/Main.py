from replit import clear
import art

#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print ("Welcome to the secret auction!\n")
bid_register={}

flag = True 
while flag:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))

  #add info to dictonary
  bid_register[name]=bid
  other_bid = input("Are there any other bidders ? (Y/N): ")

  if other_bid == "Y":
    clear()
  else:
    flag = False
    clear()

winner=0
for key in bid_register:
  winner = max(winner,bid_register[key])

for key in bid_register:
  if bid_register[key] == winner:
    print(art.congrats)
    print(f"{key} won the auction with Rs.{bid_register[key]}")
