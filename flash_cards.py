import time
import random


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


# This method is now in card.py class 
def display_card(card):
    """Print the card nicely."""
    a, b, op = card[:3]
    result = eval(str(a) + op + str(b))
    q = "*** {} {} {} = {} ***".format(a, op, b, result)
    print("".join('*' for _ in q))
    print(q)
    print("".join('*' for _ in q))


def unsolved_remaining(cards):
    """Return True if there are any unsolved questions."""
    for card in cards:
        if not card[4]:
            return True
    else:
        return False


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


def game():
    """
    Generate some addition/subtraction problems.
    Incorrect ones are removed from the queue.
    """
    start = time.time()

    add_percent = clean_input(
        "What percentage of addition problems do you want?\n (Choose integer 0-100) ", 0, 100)

    low = clean_input(
        "What is the smallest number in the range?\n (Choose any integer) ", -1000, 1000)

    high = clean_input(
        "What is the largest number in the range?\n (Choose any integer) ", -1000, 1000)

    n = clean_input(
        "How many examples do you want?\n (Choose any integer) ", 1)

    # Card is (a,b, operation, attempts, solved?)
    cards = [
        [random.randint(low, high),
         random.randint(low, high),
         random.choices('+-', cum_weights=[add_percent, 100])[0],
         0, False]
        for _ in range(n)]

    # Play the game!
    while unsolved_remaining(cards):
        for card in cards:
            if not card[4]:
                display_card(card)
                r = clean_input(" (No=0, Yes=1, Exit=2.) ", 0, 2)
                if r == 1:
                    # Got it correct!
                    card[4] = True
                elif r == 2:
                    # Exit
                    end_stats(cards, time.time()-start)
                    return None
                # Increase attempt counter
                card[3] += 1

    # Display stats
    end_stats(cards, time.time()-start)


game()
