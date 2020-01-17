# functions:
# deal:function to return/give dealer or player their first cards,(two) adding cards into hand
# total: for returning the total scores each for dealer and player
# hit:to return hand of a particular request(just one)
# clear:to clear the terminal
# results:to print the results of each players total
# score:  to print the comments of various situations that may occur  for various scores achieved by the dealer and the player
# playagain:to ask if player wants to restart game
import os
import random
deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11: card = 'J'
        if card == 12: card = 'K'
        if card == 13: card = 'Q'
        if card == 14: card = 'A'
        hand.append(card)
    return hand

def total(hand):
    total = 0
    for card in hand:
        if card == 'J'or card == 'K' or card == 'Q':
            total+=10
        if card == 'A':
            if total >= 11: total +=1
            else: total += 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:
        card = 'J'
	elif card == 12:
        card = 'K'
	elif card == 13:
        card = 'Q'
	elif card == 14:
        card = 'A'
    hand.append(card)
    return hand

def playagain():
    again = input('Do you want to play again? Y or N').lower()
    if again == 'y':
        dealer_hand = []
        player_hand = []
        deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4
        game()
    else:
        print('BYE!')
        exit()

def clear():
    if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(dealer_hand,player_hand):
    clear()
    print('The dealer has a '+ str(dealer_hand)+ ' for a total of '+ str(total(dealer_hand)))
    print('The player has a '+ str(player_hand)+ ' for a total of '+ str(total(player_hand)))

def blackjack(dealer_hand,player_hand):
    if total(player_hand) == 21:
        print_results(deal,player_hand)
        print('Congrats! Youve got a blackjack')
        playagain()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand,player_hand)
        print('Sorry you lose. The dealer got a blackjack')
        playagain()

def score(dealer_hand,player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand,player_hand)
        print('Congrats! Youve got a blackjack')
    elif total(dealer_hand) == 21:
        print_results(dealer_hand,player_hand)
        print('Sorry you lose. The dealer got a blackjack')
    elif total(player_hand) > 21:
        print_results(dealer_hand,player_hand)
        print('You got busted')
    elif total(dealer_hand) > 21:
        print_results(dealer_hand,player_hand)
        print('Dealer got busted, you win!')
    elif total(player_hand) < total(dealer_hand):
        print('Sorry, your score isnt higher than the dealer.You lose')
    elif total(player_hand) > total(dealer_hand):
        print('Congrat you win. Your score is higher than the dealers own!')

def game():
    choice = 0
    print('WELCOME TO BLACKJACK')
    print('HOPE YOU READY TO GAMBLE YOUR LIFE')
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choicie != 'q':
        print('The dealer is showing a '+ str(dealer_hand[0]))
        print('You have a '+ ' for a total of '+str(total(player_hand)))
        blackjack(dealer_hand,player_hand)
        choice = input('Do you want to [H]it,[S]tand, or [Q]uit').lower()
        clear()
        if choice == 'h':
            hit(player_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
			play_again()    
        elif choice == 's':
            while total(dealer_hand)<17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
			play_again() 
        elif choice == 'q':
            print('BYE BITCH!')
            exit()

if __name__ == "__main__":
    game()


