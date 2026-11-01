# mypy: ignore-errors


import os
from inspect import get_annotations

def test_card_pod_type_1_pt() -> None:
    from cards.card import Card
    """(1 pt) for having a Card POD type with rank and suit attributes """

    card_attributes = get_annotations(Card)

    assert 'rank' in card_attributes, 'Missing rank attribute annotation in Card class.'
    assert card_attributes['rank'] == int, 'rank attribute should be annotated as an int in the Card class, but it isn\'t.'

    assert 'suit' in card_attributes, 'Missing suit attribute annotation in Card class.'
    assert card_attributes['suit'] == str, 'suit attribute should be annotated as a str in the Card class, but it isn\'t.'
