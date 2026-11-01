class Card:
    rank: int
    suit: str

# Before I had the fun struggle of trying to figure out why the import wasn't
# working, I was going to implement this function below, but ended up trying to
# implement it in the deck module in case that it would fix my import problem
# (it didnt).

# You said we can't have a constructor in the Card() class, 
# so this technically isnt one...
# def create_card(rank: int, suit: str) -> Card:
#     card = Card()
#     card.rank = rank
#     card.suit = suit
#     return card
