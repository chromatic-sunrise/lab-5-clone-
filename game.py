from cards.card import Card
from cards.deck import Deck, create_deck, shuffle, draw
# TODO Import Deck and Card classes appropriately, as well as create_deck(),
# shuffle(), and draw()

MENU = '''Which of the following bets would you like to make?
1. The next card drawn will have a higher rank
2. The next card drawn will have a lower rank
3. The next card drawn will have the same suit
4. The next card drawn will have a different suit'''

def print_scores(player_scores: list[int]) -> None:
    print(f'Player 1 score: {player_scores[0]}')
    print(f'Player 2 score: {player_scores[1]}')

def higher_rank(first_card: Card, second_card: Card) -> bool:
    if first_card.rank > second_card.rank:
        return True
    else:
        return False

def same_suit(first_card: Card, second_card: Card) -> bool:
    if first_card.suit == second_card.suit:
        return True
    else:
        return False

def bet_score(choice: int, first_card: Card, second_card: Card) -> int:
    if choice == 1 and higher_rank(first_card, second_card):
        return 1
    elif choice == 2 and higher_rank(second_card, first_card):
        return 1
    elif choice == 3 and same_suit(first_card, second_card):
        return 3
    elif choice == 4 and not same_suit(first_card, second_card):
        return 1
    return 0

def run_turn(the_deck: Deck) -> int:
    first_card = draw(the_deck) 
    
    print(f"First drawn card: {first_card.rank} of {first_card.suit}")
    
    print(MENU)
    choice = int(input('Enter your choice: '))
    
    second_card = draw(the_deck) 

    print(f"Second drawn card: {second_card.rank} of {second_card.suit}")
    
    return bet_score(choice, first_card, second_card)

def print_winner(player_scores: list[int]) -> None:
    if player_scores[0] > player_scores[1]:
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

def main() -> None:
    the_deck = create_deck()
    
    shuffle(the_deck)

    player_scores = [0, 0]
    player_turn = 1

    while len(the_deck.cards) > 0:
        print(f'Player {player_turn}\'s turn')
        print_scores(player_scores)
        turn_score = run_turn(the_deck)

        if turn_score > 0:
            print('Correct!')
        else:
            print('Incorrect!')
        print()

        player_scores[player_turn - 1] += turn_score
        player_turn = (player_turn % 2) + 1

    print_winner(player_scores)
        

if __name__ == '__main__':
    main()
