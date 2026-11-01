# mypy: ignore-errors


import re

import pexpect

from conftest import Console


def test_correct_incorrect_feedback_1_pt() -> None:
    """(1 pt) for correctly scoring a round and printing "Correct!" or "Incorrect!" """
    cmd = Console('python game.py', timeout=10)

    # Initial score
    assert "Player 1 score: 0" in cmd, 'Expected program to print "Player 1 score: 0" at beginning of game, but it didn\'t.'

    # Check for first card
    assert "First drawn card:" in cmd, 'Expected program to print "First drawn card:", followed by the card, but it didn\'t.'

    # Make a choice
    cmd.sendline('4')

    # Second card shown
    assert "Second drawn card:" in cmd, 'Expected program to print "Second drawn card:", followed by the card, but it didn\'t.'

    # Feedback given
    assert r"(Correct)|(Incorrect)" in cmd, 'Expected program to print "Correct" or "Incorrect" at the end of the player\'s turn, but it didn\'t.'

    if cmd.match[0] == "Correct":
        assert r"Player 1 score: 1" in cmd, 'Expected player\'s score to be printed as 1 after a correct guess with option 4 on the first turn, but it wasn\'t.'
    if cmd.match[0] == "Incorrect":
        assert "Player 1 score: 0" in cmd, 'Expected player\'s score to be printed as 0 after an incorrect guess on the first turn, but it wasn\'t.'

    cmd.close()

    
def test_score_tracking_both_players_1_pt() -> None:
    """(1 pt) for correctly keeping track of both players' scores throughout the game"""
    cmd = Console('python game.py', timeout=15)

    # Initial scores must be shown
    assert "Player 1 score: 0" in cmd, 'Expected program to print "Player 1 score: 0" at the beginning of the game, but it didn\'t.'
    assert "Player 2 score: 0" in cmd, 'Expected program to print "Player 2 score: 0" at the beginning of the game, but it didn\'t.'

    # Play several rounds
    for _ in range(13):
        cmd.sendline('4')

    # Verify both players get turns
    assert "Player 1's turn" in cmd, 'Expected program to print "Player 1\'s turn" on each of player 1\'s turns, but it didn\'t.'
    assert "Player 2's turn" in cmd, 'Expected program to print "Player 2\'s turn" on each of player 2\'s turns, but it didn\'t.'

    # Scores should not be zero for both players
    assert r"Player [12] score: [^0]" in cmd, 'Both players ended the game with a score of 0, even after always choosing option 4, which should be impossible'

    cmd.close()
    

def test_deck_creation_shuffle_and_display_1_pt() -> None:
    """(1 pt) for the program creating the deck object, shuffling it, and printing all the correct information"""
    cmd = Console('python game.py', timeout=10)

    assert "Player 1's turn" in cmd, 'Expected program to print "Player 1\'s turn" at the beginning of the game, but it didn\'t.'
    assert "Player 1 score: 0" in cmd, 'Expected program to print "Player 1 score: 0" at the beginning of the game, but it didn\'t.'
    assert "Player 2 score: 0" in cmd, 'Expected program to print "Player 2 score: 0" at the beginning of the game, but it didn\'t.'

    assert r'\d+ of (hearts|diamonds|clubs|spades)' in cmd, 'Expected program to print the first drawn card on the first player\'s turn in the proper format, but it didn\'t.'

    assert "Which of the following bets would you like to make?" in cmd, 'Expected program to print, "Which of the following bets would you like to make?", but it didn\'t.'
    assert "Enter your choice:" in cmd, 'Expected program to print "Enter your choice:", but it didn\'t.'

    cmd.sendline('1')

    assert r'Second drawn card: \d+ of (hearts|diamonds|clubs|spades)' in cmd, 'Expected program to print the second drawn card on the first player\'s turn in the proper format, but it didn\'t.'

    cmd.close()

    
def test_game_ends_when_deck_empty_1_pt() -> None:
    """(1 pt) for the program computing scores correctly and ending when the deck is empty"""
    cmd = Console('python game.py', timeout=30)

    # Play enough rounds to exhaust the deck
    for _ in range(30):
        cmd.sendline('4')

    # IMPORTANT: wait for program to terminate
    cmd.expect(pexpect.EOF)

    output = cmd.before.decode()

    # Must end with a winner
    assert re.search(r'Player [12] wins!', output), \
        "Expected program to end with a winner announcement in the correct format, but it didn\'t."

    # Must show feedback during play
    assert ("Correct!" in output or "Incorrect!" in output), \
        'Expected program to print "Correct!" and / or "Incorrect!" throughout the gameplay, but it didn\'t.'

    cmd.close()
