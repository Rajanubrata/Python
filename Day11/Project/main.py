import art
import random 
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def total_score(my_cards):
  total = 0
  for card in my_cards:
    total += card
  return total

#create my hand and computers hand
my_card=[]
comp_card=[]


#i take two card & computer take 2 card
print(".♣️♦️♠️♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠")
my_card.append(random.choice(cards))
my_card.append(random.choice(cards))
print(f"Your cards are: {my_card}, Current Score = {total_score(my_card)}\n")

comp_card.append(random.choice(cards))
comp_card.append(random.choice(cards))
print(f"Computer's 1st card': {comp_card[0]}\n")
print(".♣️♦️♠️♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠")

should_continue= True 
while should_continue:
  #ask user if he want to take card
  if input("Type 'Y' to get another card || Type 'N' to pass : ").lower()=='y':
    print("\n")
    my_card.append(random.choice(cards))
    comp_card.append(random.choice(cards))
    print(".♣️♦️♠️♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠")
    print(f"Your cards are: {my_card}, Current Score = {total_score(my_card)}\n")
    print(f"Computer's 1st card: {comp_card[0]}\n")
    print(".♣️♦️♠️♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠")
    
    if total_score(my_card) > 21:
      should_continue=False
  else:
    should_continue= False

print(f"Your final hand  : {my_card}, Current Score = {total_score(my_card)}\n")
print(f"Computer's final hand: {comp_card}, Current Score = {total_score(comp_card)} \n")

#check who wins
print(".♣️♦️♠️♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠")

if total_score(my_card) <= 21:
  if total_score(comp_card) > 21 :
    print(art.win)
  elif total_score(my_card)>total_score(comp_card):
    print(art.win)
  elif total_score(my_card)==total_score(comp_card):
    print(art.draw)
  else:
    print(art.loose)
else:
  print(art.loose)
# print(".♣️♦️♠️♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠♣️♦️♠")
  
