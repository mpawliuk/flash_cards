def play(cards:List(Card), shift=2):
    """Play the game and go through the flashcards.
    
    When a card is failed, it is pushed back 2 places.
    shift: int
    """
    while unsolved_remaining(cards):
        for card in cards:
            if not card.solved:
                card.display_card()
                r = clean_input(" (No=0, Yes=1, Exit=2.) ", 0, 2)
                if r == 0:
                    # Failed. Push it back 2 places
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
                # Increase attempt counter
                card.attempts += 1

    # Display stats
    end_stats(cards, time.time()-start)
