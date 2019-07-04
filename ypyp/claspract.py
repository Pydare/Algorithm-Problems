from random import shuffle
from random import randint
SUITE = 'H D S C'.split()
RANK = {2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'A',12:'K',13:'Q',14:'J'}
class Deck(object):
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.suit
        return self.rank

c = Deck(['H','D','S','C'],RANK.keys())
print(c)
