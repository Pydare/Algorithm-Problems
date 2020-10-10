"""
52 cards in a deck
4 suits -> Spades, Hearts, Diamonds and Club
13 ranks -> A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K

suit and rank representations should be mapped
{s:3,h:2,d:1,c:0}
"""
#three_of_clubs = Card(0,3)
class Card:

    SUITS = ('Clubs','Diamonds','Hearts','Spades')
    RANKS = ('narf','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

    def __init__(self,suit=0,rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """
        >>> print(Card(2,11))
        Queen of Hearts
        """
        return f"{Card.RANKS[self.rank]} of {Card.SUITS[self.suit]}"

    #By convention, __cmp__ takes two parameters, self and other, and returns 1 if the first object is greater, -1 if the second object is greater, and 0 if they are equal to each other.
    #we are assuming suits to be more important
    def __cmp__(self,other):
        #check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        #suits are the same, check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        #ranks are the same, its a tie
        return 0

three_of_clubs = Card(0,3)
three_of_diamonds = Card(1,3)

print(three_of_clubs.__cmp__(three_of_diamonds))

#each Deck object will contain a list of cards as an attribute.
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += str(self.cards[i]) + "\n"
        return s

    #randrange chooses a random integer in the range a <= x < b
    #traversing the cards and swapping each card with a randomly chosen one
    def shuffle(self):
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i,num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    #takes a card as a parameter, removes it, and returns True if the card was in the deck and False otherwise
    def remove(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    #to deal cards, we want to remove and return the top card
    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return (len(self.cards) == 0)

    


            