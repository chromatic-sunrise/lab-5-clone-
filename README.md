# Lab 5: Classes, Modules, and Packages

## (10 pts) Decks and Cards 

In this lab, you’ll create some packages, modules, and classes to
represent cards and decks, and then you’ll use them to implement a very
simple card game.

The lab repository comes with a single file, `game.py`. You’ll have to
modify it, but you’ll also be creating additional packages and modules.
Complete the following steps:

1.  Create a package named `cards` (don’t forget `__init__.py`).

2.  In the `cards` package, create a module named `card` (i.e., a file
    named `card.py`).

3. In the `card` module, define a POD type named `Card`
    with the following attributes:

    - `rank`. This should be an integer.

      For context, it represents the rank of a card in a deck of cards,
      and it will generally be a value between 1 and 13 (inclusive). 1
      corresponds to aces, 11 corresponds to jack, 12 corresponds to
      queen, and 13 corresponds to king. There are no jokers.

    - `suit`. This should be a string. It represents the suit of a card in a 
      deck of cards. It will be one of 'hearts', 'diamonds', 
      'clubs', or 'spades'

    The `Card` class should not have any methods---not even a constructor.

3.  In the `cards` package, create another module named `deck` (i.e., a
    file named `deck.py`). In this module, import the `random` package
    (as you did in some past assignments), and then define the following:

    - A POD type named `Deck`. This class should have an attribute named
      `cards` with a type of `list[Card]` (i.e., a list of `Card`
      objects). Don't forget to import the `Card` class appropriately.

      The `Deck` class should not have any methods---not even a constructor.

    - A function with the following header:

      `def create_deck() -> Deck:`

      Implement this function. It should create a `Deck` object, initialize
      its `cards` attribute,
      and return it. Specifically, its `cards` attribute should be a list of
      52 `Card` objects as follows:

      1.  The first 13 cards in the list should all have
          the suit `hearts`, and their values should be 1 through 13
          (in that order).

      2.  The next 13 cards in the list should all have
          the suit `diamonds`, and their values should be 1 through 13
          (in that order).

      3.  The next 13 cards in the list should all have
          the suit `clubs`, and their values should be 1 through 13
          (in that order).

      4.  The last 13 cards in the list should all have
          the suit `spades`, and their values should be 1 through 13
          (in that order).

    - The following function (just copy it, verbatim):

          def shuffle(deck: Deck) -> None:
              random.shuffle(deck.cards)

      This method shuffles the deck so that its cards are in a random
      order. It requires that the `random` package be imported, as directed
      above.

    - A function with the following header:

      `def draw(deck: Deck) -> Card:`

      Implement this function. When called,
      it should remove the last element in the given deck’s list of
      cards and return it.

4.  Finally, open `game.py` and complete the action items outlined by
    `# TODO` comments. When you’re done, you should have a program that
    fulfills the following requirements (much of this is already
    implemented for you):

    1.  Create a `Deck` object and shuffle its list of cards via the
        `shuffle()` function.

    2.  There are two players.· For each player, the program must keep
        track of their scores throughout the game (e.g., via two integer
        variables).

    3.  Alternate between the two players’ turns, starting with player
        1, until there are no more cards in the deck. On each player’s
        turn:

        - Print a message stating 1) whose turn it is, and 2) the
          current scores of <ins>both</ins> players. (This is done for you;
          don't modify the message format).

        - Draw a card from the deck via the `draw()`
          function and print a message
          to the terminal stating its rank and suit in the format:

          `First drawn card: RANK of SUIT`

          Replace RANK with the card's numeric rank (1-13),
          and replace SUIT with the card's suit. For example, "First drawn
          card: 5 of hearts", or "First drawn card: 12 of spades". The suit MUST
          be printed in all lower-case, and
          the rank MUST be printed as its numeric value (e.g., print 11
          instead of 'Jack'). 

        - Print the following prompt to the terminal:

              Which of the following bets would you like to make?
              1. The next card drawn will have a higher rank
              2. The next card drawn will have a lower rank
              3. The next card drawn will have the same suit
              4. The next card drawn will have a different suit
              Enter your choice: 

        - Read the user’s input. No error handing / input sanitization
          is required (i.e., your program may assume that the user will
          enter 1, 2, 3, or 4).

        - Draw another card from the deck via the `draw()`
          function and print a message
          to the terminal stating its rank and suit in the format:

          `Second drawn card: RANK of SUIT`

          Replace RANK with the card's numeric rank (1-13),
          and replace SUIT with the card's suit. For example, "Second drawn
          card: 11 of diamonds". Again, the suit MUST be printed in lowercase,
          and the rank MUST be printed as its numeric value.

        - If the player selected option 1 and the second drawn card has
          a higher rank than the first drawn card, then the player earns
          1 point, and the program should print “Correct!”.

          If the player selected option 2 and the second drawn card has
          a lower rank than the first drawn card, then the player earns
          1 point, and the program should print “Correct!”.

          If the player selected option 3 and the second drawn card has
          the same suit as the first drawn card, then the player earns
          <ins>3 points</ins>, and the program should print “Correct!”.

          If the player selected option 4 and the second drawn card has
          a different suit from the first drawn card, then the player
          earns 1 point, and the program should print “Correct!”.

          In all other cases (i.e., if the player’s guess was
          incorrect), then the program should print “Incorrect!”. The
          player earns no points in this case.

    4.  Print a message stating the winner (the player with the higher
        total score). If player 1 won, then it should print:

        `Player 1 wins!`

        If player 2 won, then it should print:

        `Player 2 wins!`
        
        If the scores are tied at the end of the game, then the program should
        behave as if player 1 won.

Make sure your code passes through Mypy (in strict mode) without errors,
and make sure to adhere to the course’s style and design guide.

## Example output 

When you execute your program, it might look something like this (much
of it is omitted for brevity):

    Player 1's turn.
    Player 1 score: 0
    Player 2 score: 0
    First drawn card: 5 of hearts
    Which of the following bets would you like to make?
    1. The next card drawn will have a higher rank
    2. The next card drawn will have a lower rank
    3. The next card drawn will have the same suit
    4. The next card drawn will have a different suit
    Enter your choice: 1
    Second drawn card: 12 of diamonds
    Correct!

    Player 2's turn.
    Player 1 score: 1
    Player 2 score: 0
    First drawn card: 7 of spades
    Which of the following bets would you like to make?
    1. The next card drawn will have a higher rank
    2. The next card drawn will have a lower rank
    3. The next card drawn will have the same suit
    4. The next card drawn will have a different suit
    Enter your choice: 3
    Second drawn card: 1 of spades
    Correct!

    Player 1's turn.
    Player 1 score: 1
    Player 2 score: 3
    First drawn card: 2 of hearts
    Which of the following bets would you like to make?
    1. The next card drawn will have a higher rank
    2. The next card drawn will have a lower rank
    3. The next card drawn will have the same suit
    4. The next card drawn will have a different suit
    Enter your choice: 3
    Second drawn card: 4 of clubs
    Incorrect!

    Player 2's turn.
    Player 1 score: 1
    Player 2 score: 3

  *(...Eventually, the deck will run out of cards, at which point
  the game should end and print a message stating the winner...)*

## Unit tests

Your program should pass
the unit tests that come with this repository. I will run these
tests to compute a grade. You can run them yourself by running the following
shell command in your terminal within your project's directory:

`python -m pytest tests`

## Rubric
The rubric is as follows:

 -  (1 pt) for the create_deck() function being implemented correctly 
 -  (1 pt) for the draw() function being implemented correctly 
 -  (0.5 pts) for having a cards package
 -  (0.5 pts) for having a deck module in the cards package 
 -  (1 pt) for correctly scoring a round and printing "Correct!" or "Incorrect!" 
 -  (1 pt) for the program creating the deck object, shuffling it, and printing all the correct information
 -  (1 pt) for the program computing scores correctly and ending when the deck is empty
 -  (1 pt) for correctly keeping track of both players' scores throughout the game
 -  (1 pt) for having a Card POD type with rank and suit attributes 
 -  (1 pt) for having a Deck POD type with cards attribute
 -  (1 pt) if your code passes through Mypy (in strict mode)

Possible penalties:

- (-1 pt) for any violations of the course’s style and design guide. If there
  are multiple violations, you will only be penalized -1 pt total.

  As a reminder, here's a summary of the rules:

  - Single Responsibility Principle (SRP) proxy: A
    function shouldn't have more
    than 15 logical lines of code.
  - Don't Repeat Yourself (DRY) principle: Don't copy and paste the same block
    of code several times. Instead, move it into a function and just call the
    function several times.
  - Don't use global variables (global constants, which aren't modified during
    the program's runtime after initialization, are okay).
  - A line of code shouldn't be longer than 80 characters.
  - If your code is very hard to understand, explain it with adjacent comments.

# Acknowledgements
author: Alexander Guyer (<guyera@oregonstate.edu>), CS 162
