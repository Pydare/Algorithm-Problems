import random
suits = ('H','D','C','S')
rankings = ('A','1','2','3','4','5','6','7','8','9','10','K','Q','J')
card_value = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'K':10,'Q':10,'J':10}
chips = 100
class Card(object):
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def getSuit(self):
        return self.suit
    def getRank(self):
        return self.rank
    def __str__(self):
        return (self.suit + self.rank)
    def draw(self):
        print(self.suit + self.rank)

class Hand(object):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False
    def __str__(self):
        #prints out hand composition
        hand_comp = ' '
        for card in self.cards:
            card_name = card.__str__()
            hand_comp += card_name
        return 'The hand has %s' %(hand_comp)
    def card_add(self,card):
        self.cards.append(card)
        if card.rank = 'A':
            self.ace = True
        self.value += card_value[card.rank]
    def calc_val(self):
        if(self.ace == True and self.value <= 12):
            return self.value + 10
        else:
            return self.value
    def draw(self):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for card in range(starting_card,len(self,cards)):
            self.cards[card].draw()


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
        deck_comp = ' '
        for deck in self.deck:
            x = deck.__str__()
            deck_comp += x
        return 'The deck has %s' %(deck_comp)

def make_bet():
    global bet
    bet = 0
    bet_comp = int(input('Enter the amount of chips you want to use to bet'))
    while bet == 0:
        if bet_comp > 0 and bet_comp <= chips:
            bet = bet_comp
        else:
            print('Invalid amount entered, you have just '+str(chips)+' chips left')
        
def deal_cards():
    global result,playing,deck,player_hand,dealer_hand,chips,bet
    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = 'Hit or stand, pick either h or s'

    if playing == True:
        print('Fold, sorry')
        chips -= bet
    playing = True
    game_step()

def hit():
    global result, chips, bet, player_hand, dealer_hand, deck
    #if hand is in play add card
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        print('Player hand is %s'%(player_hand))

        if player_hand.calc_val() > 21:
            result = 'Busted! you lose your bet. Press d to deal and q to quit'
            chips -= bet
            playing = False
        else:
            print('Sorry cant hit')
    game_step()

def stand():
    global result, chips, bet, player_hand, dealer_hand, deck
    if playing == False:
        if player_hand.calc_val() > 0:
            result = 'Sorry, you can"t stand!'
        else:
            if dealer_hand.calc_val() < 17:
                dealer_hand.card_add(deck.deal())
            elif dealer_hand.calc_val() < player_hand.calc_val():
                result = 'You have a higher value than dealer, you win! d and q applies'
                chips += bet
                playing = False
            elif dealer_hand.calc_val() == player_hand.calc_val():
                result = 'Theres a tie d and q applies'
                playing = False
            else:
                result = 'Dealer wins! d and q applies again'
        game_step()

def game_step():
    print('Player hand is: ')
    player_hand.draw(hidden = False)
    print('Player hand total is: 'str(player_hand.calc_val()))
    print('Dealer hand is: ')
    dealer_hand.draw(hidden = True)

    if playing = False:
        print('For a total of '+str(dealer_hand.calc_val()))
        print('Total chips is '+str(chips))
    else:
        print('With another card hidden upside down')

    print(result)

    player_input()

def game_exit():
    print('Thanks for playing, bye!')
    exit()

def player_input():
    plin = input().lower()

    if plin == 'h':
        Hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal()
    elif plin == 'q':
        game_exit()
    else:
        print('Invalid input, enter h,s,d or q')
        player_input()

def intro():
    statement = '''Welcome to BlackJack 21. Try your possible best to reach 21. 
    Dealer stops hitting when she reaches 17. Aces can  be use as 7 or 11.followed  Card output displays the card type 
    followed by the number'''
    print(statement)

deck = Deck()
deck.shuffle()
player_hand.Hand()
dealer_hand.Hand()

intro()
deal_cards()





