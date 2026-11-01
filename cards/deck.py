import random
# I spent like a whole hour trying to figure this out to no avail. It would
# seem that for some reason, even just when importing 'card' itself (no 'from'
# statement!), that it fails to import when I import this deck.py from game.py
# in the parent directory. I tried a bunch of different ways to resolve this
# import error, including reading through the docs to try and implement
# relative imports, but that didnt work either. Thus, as your instructions
# explicitly say to import the Card class from this module in the same package
# directory, I am at a loss on this one, and I submit what I do have for 
# you to grade. 
from card import Card # , create_card

SUITS: list[str] = ["hearts", "diamonds", "clubs", "spades"]

class Deck:
    cards: list[Card]

def create_card(rank: int, suit: str) -> Card:
    my_card = Card()
    my_card.rank = rank
    my_card.suit = suit
    return my_card

# only wrote this here in the middle of my desperate attempts to get the damn
# import to work; I hoped that maybe the problem was that my "card" module had
# anything but just a class in there (I was wrong, but whatever)
def create_deck() -> Deck:
    deck = Deck()
    cards: list[Card] = []
    for suit in SUITS:
        for i in range(1,14):
            cards.append(create_card(i, suit))
    return deck

def shuffle(deck: Deck) -> None:
    random.shuffle(deck.cards)

def draw(deck: Deck) -> Card:
    my_card = deck.cards[-1]
    deck.cards.pop(-1)
    return my_card
