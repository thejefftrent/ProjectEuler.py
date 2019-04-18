from enum import Enum

plays = []
with open('ProjectEuler.py/p054_poker.txt','r') as file:
    plays = file.readlines()
plays = [play.strip() for play in plays]
plays = [play.split(' ') for play in plays]

print(plays[0])
class Ranks(Enum):
    HIGHCARD = 0
    ONEPAIR = 1
    TWOPAIR = 2
    THREEOFAKIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULLHOUSE = 6
    FOUROFAKIND = 7
    STARIGHTFLUSH = 8
    ROYALFLUSH = 9



class PokerHand:
    def __init__(self, five_cards:list):
        self.cards = five_cards
    
    def rank(self):
        pass


    


for play in plays:
    pass
