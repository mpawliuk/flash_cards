import time
import random
from typing import List
from card import Card

def clean_input(question, a=0, b=100):
    while True:
        try:
            n = int(input(question))
        except ValueError:
            print("This is not a valid number. Try again.")
        else:
            n = int(n)
            n = min(max(a, n), b)
            return n

def unsolved_remaining(cards: List[Card])  -> bool:
    """Return True if there are any unsolved questions."""
    for card in cards:
        if not card.solved:
            return True
    # We went through all the cards and all have been solved
    return False


def generate_cards(add_percent: int, low: int, high:int, num_cards: int ) -> List[Card]:
    """Generates the flashcards to be studied"""
    card_list = List()

    for x in range(num_cards):
        a = random.randint(low, high)
        op = random.choices('+-', cum_weights=[add_percent, 100])[0]
        b = random.randint(low, high)
        # Creating a card obj and adding it to the card_list
        card_list.append(Card(a, op, b))

    return card_list


def play(cards:List(Card)) -> None:
    """Play the game and go through the flashcards.

    When a card is failed, it is pushed back by shift places.
    shift: int
    """
    while unsolved_remaining(cards):
        for card in cards:
            if not card.solved:
                card.display_card()
                r = clean_input(" (No=0, Yes=1, Exit=2.) ", 0, 2)
                card.attempts += 1
                card.confidence_score = get_q_confidence()
                shift = card.calculate_shift()
                if r == 0:
                    # Failed. Push it back by the shift
                    i = cards.index(card)
                    cards.remove(card)
                    n = len(cards)
                    cards.insert((i+shift) % n, card)
                elif r == 1:
                    # Got it correct!
                    card.solved = True
                elif r == 2:
                    # Exit
                    end_stats(cards, time.time()-start)
                    return None

    # Display stats
    end_stats(cards, time.time()-start)

def get_q_confidence() -> int:
    """Get's the user's confidence for the card"""
    response = input("How confident do you feel about being able to answer this question (from 1-10)? ")
    if response.isnumeric() & 0 < response <= 10:
        return int(response)
    else:
        print("Incorrect score value, please enter a number from 1 to 10.")
        # we call the function until it returns the appropriate value
        get_q_confidence()

# TODO: look into this? since the cards are now objects
def end_stats(cards, total_time):
    """Print relevant stats."""
    total_attempts = sum(card[3] for card in cards)
    ave_attempts = total_attempts / len(cards)
    max_attempts = max(card[3] for card in cards)
    for card in cards:
        if card[3] == max_attempts:
            hard_card = card
    print("Congratulations! All cards have been solved!")
    print("Total time: {:.1f} seconds.".format(total_time))
    print("Total attempts: {}".format(total_attempts))
    print("Average attempts per question: {:.1f}".format(ave_attempts))
    print("Most challenging question:")
    display_card(hard_card)
    print("which needed {} attempts.".format(max_attempts))
