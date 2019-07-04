#used for card shuffle
import random
#boolean used to know if card was in play
playing = False

chip_pool = 100
bet = 1
restart_phrase = "Press 'd' to deal the cards again or 'q' to quit"
#Hearts, Diamonds, Clubs and Spades(SUITS)
suits = ('H','D','C','S')
#possible card ranks
rankings = ('A','2','3','4','5','6','7','8','9','J','Q','K')
#point values dict
card_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'J':10,'Q':10,'K':10}


class Card(object):
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.suit + self.rank
    def grab_suit(self):
        return self.suit
    def grab_rank(self):
        return self.rank
    def draw(self):
        print(self.suit + self.rank)

class Hand(object):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        #return a string of current hand composition
        hand_comp = ' '
        #a better way of doing this can be through list comprehension
        for card in self.cards:
            card_name = card.__str__()
            hand_comp += ' '+ card_name  

        return 'The hand has %s' %(hand_comp)
    def card_add(self,card):
        #add a card to the hand
        self.cards.append(card)

        #check for aces
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]
    def calc_val(self):
        #calculating the value of the hand, makes the ace 11 if they dont bust the hand
        if (self.ace == True and self.value<12):
            return self.value + 10
        else:
            return self.value
    def draw(self,hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
            self.cards[x].draw()

class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in rankings:
                self.deck.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    def __str__(self):
        deck_comp = " "
        for card in self.cards:
            deck_comp += ' '+ deck_comp.__str__()

        return "The desk has " + desk_comp

#first making a bet
def make_bet():
    #ask player for the bet amount
    global bet 
    bet = 0
    print('What amount of chips would you like to bet? Enter whole integer please')

    while(bet == 0):
        bet_comp = int(input())
        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("Invalid bet, you only have " + str(chip_pool) + " remaining")

def deal_cards():
    #This function deals out cards and sets up round 
    global result,playing,deck,player_hand,dealer_hand,chip_pool,bet
    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    #Deal out initial cards
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = 'Hit or stand? Press either h or s: '

    if playing == True:
        print('Fold, sorry')
        chip_pool -= bet

    #set up to know currently playing hand
    playing = True
    game_step()

def hit():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    #if hand is in play, add card
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        print('Player hand is %s'%(player_hand))

        if player_hand.calc_val() > 21:
            result = 'Busted!'+ restart_phrase

            chip_pool -= bet
            playing = False

        else:
            result = 'Sorry cant hit '+ restart_phrase

    game_step()

def stand():
    global playing, chip_pool,deck,player_hand,dealer_hand,result,bet
    
    if playing == False:
        if player_hand.calc_val() > 0:
            result = 'Sorry, you can"t stand!'

    #Now go through all the other possible options
    else:

        #soft 17 rule
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        #dealer busts
        if dealer_hand.calc_val() > 21:
            result = 'Dealer busts! You win!'+ restart_phrase
            chip_pool += bet
            playing = False

        #Player has better hand than dealer
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = 'You beat the dealer, you win!' + restart_phrase
            chip_pool += bet
            playing = False  

        # Push
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = 'Tied up, push!' + restart_phrase
            playing = False

        # Dealer beats player
        else:
            result = 'Dealer Wins!' + restart_phrase
            chip_pool -= bet
            playing = False
    game_step()

        
def game_step():
    'Function to print game steps/status on output'

    #Display Player hand
    print('Player hand is: ')
    player_hand.draw(hidden = False)

    print('Player hand total is: '+str(player_hand.calc_val()))

    #Display dealer hand
    print('Dealer hand is: ')
    dealer_hand.draw(hidden = True)

    #if game round is over
    if playing == False:
        print('--- for a total of '+ str(dealer_hand.calc_val()))
        print('Chip total: '+str(chip_pool))
    else:
        print('with another card hidden upside down')

    #print result of hit or stand
    print(result)

    player_input()

def game_exit():
    print('Thanks for playing yalll')
    exit()

#function to read user input
def player_input():
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print('Invalid input, Enter h,s,d or q')
        player_input()

def intro():
    statement = '''Welcome to BlackJack! Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    Card output goes a letter followed by a number of face notation'''
    print(statement)


#create a deck
deck = Deck()
#shuffle it
deck.shuffle()
#create player and dealer hands
player_hand = Hand()
dealer_hand = Hand()
#print the intro
intro()
#Deal out the cards and start the game
deal_cards()

