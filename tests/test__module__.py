# mypy: ignore-errors


import os



def test_cards_package_exists_0_5_pts() -> None:
    """(0.5 pts) for having a cards package"""
    assert os.path.isfile("cards/__init__.py"), "__init__.py is missing in cards package"

def test_deck_module_exists_0_5_pts() -> None:
    """(0.5 pts) for having a deck module in the cards package """
    assert os.path.isfile(
        "cards/deck.py"), "deck.py doesn't exist in cards package"

