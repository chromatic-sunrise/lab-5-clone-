# mypy: ignore-errors


from inspect import get_annotations


def test_deck_pod_type_1_pt() -> None:
    from cards.card import Card
    from cards.deck import Deck
    """(1 pt) for having a Deck POD type with cards attribute """

    deck_attributes = get_annotations(Deck)

    assert 'cards' in deck_attributes, 'Missing cards attribute in the Deck class.'
    assert deck_attributes['cards'] == list[Card], 'cards attribute should be annotated as a list[Card] in the Deck class, but it isn\'t.'


def test_create_deck_1_pt() -> None:
    from cards.card import Card
    from cards.deck import create_deck
    """ (1 pt) for the create_deck() function being implemented correctly """
    deck = create_deck()

    assert len(deck.cards) == 52, f'The create_deck() function should initialize the deck\'s cards attribute to contain 52 cards, but instead got a length of {len(deck.cards)}'

    def create_card(rank: int, suit: str) -> Card:
        res = Card()
        res.rank = rank
        res.suit = suit
        return res
    answer = [
        create_card(rank, suit)\
            for suit in ['hearts', 'diamonds', 'clubs', 'spades']\
                for rank in range(1, 14)
    ]

    for card1, card2 in zip(deck.cards, answer):
        print(card2.rank, card2.suit)
        assert card1.rank == card2.rank, ('cards in the deck created by create_deck() are not in the '
            'right order')
        assert card1.suit == card2.suit, ('cards in the deck created by create_deck() are not in the '
            'right order')


def test_draw_1_pt() -> None:
    """ (1 pt) for the draw() function being implemented correctly """
    from cards.card import Card
    from cards.deck import Deck, draw
    deck = Deck()
    def create_card(rank: int, suit: str) -> Card:
        res = Card()
        res.rank = rank
        res.suit = suit
        return res
    deck.cards = [
        create_card(rank, suit)\
            for suit in ['hearts', 'diamonds', 'clubs', 'spades']\
                for rank in range(1, 14)
    ]

    card = draw(deck)

    assert isinstance(card, Card), 'draw(deck) should have returned a Card object, but it didn\'t.'
    assert len(deck.cards) == 51, f'After calling draw(deck) on a full deck of 52 cards, the deck should have 51 cards remaining, but instead got a length of {len(deck.cards)}'
