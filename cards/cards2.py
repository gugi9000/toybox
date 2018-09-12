import random


deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]*4
r_deck = [] 

for i in range(0, len(deck)):
    card = random.randint(0,len(deck)-1)
    chosen = deck.pop(card)
    r_deck.append(chosen)

print(f'r_Deck: {r_deck}')
print(f'Deck: {deck}')
