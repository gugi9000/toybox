import random


shuffled_deck = []

def shuffle_deck(shuffled_deck):
#Defining the deck
    deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","Ace"]*4
    decksize = len(deck)
    shuffled_deck = list(range(0,decksize))

    #Shuffling the deck
    for i, card in enumerate(deck):
        deck_pos = random.randint(0,decksize)
        if deck_pos in shuffled_deck:
            print(f'deck pos: {deck_pos} - deck: {deck}')
            shuffled_deck[deck_pos] = deck[i]
            break
        else:
            continue

    print(shuffled_deck)

class Deal():
    '''Class to deal a card'''

    def dealing(self,player,shuffled_deck):
            self.player = player
            self.shuffled_deck = shuffled_deck
            dealt_card = shuffled_deck.pop(0)
            player_list[player].update_hand(dealt_card)
            try:
                player_list[player].attributes['hand_value'].append(int(player_list[player].attributes['hand'][-1]))
            except:
                if player_list[player].attributes['hand'][-1] == "Ace":
                    player_list[player].attributes['hand_value'].append("Ace")
                else:
                    player_list[player].attributes['hand_value'].append(10)

print(f'before deck: {shuffled_deck}')
shuffle_deck(shuffled_deck)
print(f'after deck: {shuffled_deck}')

