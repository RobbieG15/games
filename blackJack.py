"""
@Author: Robert Greenslade
@
@Title: Blackjack Terminal Game 
@
@Date: May 20th, 2021
"""

import random

# stores suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# declare boolean to control while loops
playing = True


class Card:
    # class to hold information about cards

    def __init__(self, suit, rank):
        """
        function that classifies suit and rank as attributes of the Card class
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        function that prints out the rank and suit when print(Card) is called
        """
        return f"{self.rank} of {self.suit}"

class Deck:
    #class to hold information about deck

    def __init__(self):
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        """
        function that returns how many cards are in the deck in string format
        """
        for Card in self.deck:
            print(f"{Card.rank} of {Card.suit}")

    def shuffle(self):
        """
        shuffles deck 
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        deals two cards to both player and computer
        """
        single_card = self.deck.pop()
        return single_card
            
class Hand:
    #class to hold information about Player hand
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips():
    #class to hold information about chips
    
    def __init__(self):
        self.total = None
        self.bet = 0
        
    def amount_of_chips(self):
        while True:
            try:
                self.total = int(input("How many chips would you like? (choose more than 50) \n"))
            except ValueError:
                 print("Make sure your bet is an integer value")
                 continue
            else:
                if self.total < 50:
                    print('Choose a value greater than 50.')
                    continue
                else:
                    break

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self):
        while True:
            try:
                self.bet = int(input("How many chips would you like to bet? \n"))
            except ValueError:
                 print("Make sure your bet is an integer value")
                 continue
            else:
                if self.bet > self.total:
                    print('You cannot bet more than what you have.')
                    continue
                else:
                    break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'HIT' or 'STAND' \n")

        if x.lower() == 'hit':
            hit(deck,hand)
        elif x.lower() == 'stand':
            print('Player chooses to stand. Dealer is playing.')
            playing = False
        else:
            print('Sorry, please try again.')
            continue
        break

def show_some(player, dealer):
    print("Dealer's hand: card hidden, {}".format(dealer.cards[1]))
    print("Player's hand: Total of {} and {} aces".format(player.value, player.aces))

def show_all(player, dealer):
    print("Dealer's hand: {}, {}".format(dealer.cards[0], dealer.cards[1]))
    print("Player's hand: Total of {} and {} aces".format(player.value, player.aces))
    
def player_busts(player, dealer, chips):
    print('Player Busts!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer Busts!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer Wins!')
    chips.lose_bet()

def push(player, dealer):
    print('Dealer and Player have tied!')


print('Welecome to BlackJack! In this version, the player tries to get as close as they can get to 21 without going over.\n The Dealer is going to hit until they reach 17. Aces count as 1 or 11')
#assign an amount of chips to player
player_chips = Chips()
player_chips.amount_of_chips()

while True:
    

    #creating deck
    deck = Deck()
    deck.shuffle()

    #creating hands for dealer and player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())



    #make player bet
    player_chips.take_bet()
    
    #show some cards
    show_some(player_hand, dealer_hand)

    #reset playing to true to make sure player gets hand
    playing = True

    #player turn
    while playing:

        #hit or stand?
        hit_or_stand(deck, player_hand)

        #show some cards
        show_some(player_hand, dealer_hand)

        #check for player bust or not
        player_hand.adjust_for_ace()
        if player_hand.value > 21:
            playing = False
            
    #if player did not bust, let dealer play
    if player_hand.value <= 21:

        while dealer_hand.value < 17 or dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
        
        #show all cardas after dealer hand
        show_all(player_hand, dealer_hand)

        #check all the winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

        #inform player how many chips they have left
        print(f'Your winnings are {player_chips.total}!')

        #check if player has any left to bet
        if player_chips.total <= 0:
            print('Better luck next time!')
            break
        
        #ask to play new game
        new_game = input('Would you like to play another game? enter YES or NO \n')

        if new_game.lower() == 'yes':
            continue
        
        else:
            print('Thanks for playing!')
            break
    else:
        show_all(player_hand, dealer_hand)
        player_busts(player_hand, dealer_hand, player_chips)
        if player_chips.total <= 0:
            print('Your all out of chips! Better luck next time!')
            break
        
        #ask to play new game
        new_game = input('Would you like to play another game? enter YES or NO \n')

        if new_game.lower() == 'yes':
            continue
        
        else:
            print('Thanks for playing!')
            break
