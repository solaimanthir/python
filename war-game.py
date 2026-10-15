# war game - link https://en.wikipedia.org/wiki/War_(card_game)

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
    #create an empty list of cards
        self.cards = []
        
        #create card for each suit-rank pair and append to the list
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                
                self.cards.append(new_card)
    
    #shuffle the cards
    def shuffle_cards(self):
        random.shuffle(self.cards)
    
    #grab one card for the play
    def grab_one_card(self):
        return self.cards.pop()
        
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def remove_card(self):
        return self.cards.pop(0)
    
    def add_cards(self, card_obj):
        if type(card_obj) == type([]):
            self.cards.extend(card_obj)
        else:
            self.cards.append(card_obj)
    
    def __str__(self):
        return (f'player {self.name} currently has {len(self.cards)} cards')
    
# setup the game
player_1 = Player('One')
player_2 = Player('Two')

new_deck = Deck()
new_deck.shuffle_cards()

#split the deck in half
for i in range(26):
    player_1.add_cards(new_deck.grab_one_card())
    player_2.add_cards(new_deck.grab_one_card())

game_play = True
num_round = 0

while game_play:
    if(len(player_1.cards) == 0):
        print('player2 has won!')
        break
    
    if(len(player_2.cards) == 0):
        print('player1 has won!')
        break
    
    num_round += 1
    print(f'this is round#{num_round}')
    
    #cards on table
    curr_round_cards_p1 = []
    curr_round_cards_p2 = []
    #grab a card from player1's deck and add to p1's slot in table
    curr_round_cards_p1.append(player_1.remove_card())
    #grab a card from player2's deck and add to p2's slot in table
    curr_round_cards_p2.append(player_2.remove_card())

    in_war = True
    while in_war:
        #compare the latest added card from the players
        if curr_round_cards_p1[-1].value < curr_round_cards_p2[-1].value:
            player_2.add_cards(curr_round_cards_p1)
            player_2.add_cards(curr_round_cards_p2)
            in_war = False

        elif curr_round_cards_p1[-1].value > curr_round_cards_p2[-1].value:
            player_1.add_cards(curr_round_cards_p1)
            player_1.add_cards(curr_round_cards_p2)
            in_war = False

        else:
            print('--War--')
            if(len(player_1.cards) < 5):
               print('Player1 has insufficient cards to engage in war')
               print('Player2 has won!')
               game_play = False
               break
           
            if(len(player_2.cards) < 5):
               print('Player2 has insufficient cards to engage in war')
               print('Player1 has won!')
               game_play = False
               break

            #add cards from deck to the table for war
            for i in range(5):
                curr_round_cards_p1.append(player_1.remove_card())
                curr_round_cards_p2.append(player_2.remove_card())
