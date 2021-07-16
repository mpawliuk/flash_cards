# This is where the main system of the flash card game will go
import sys
from card_logistics import generate_cards, handle_cards, play


def main_menu():
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("WELCOME TO THE FLASHCARD GAME")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("SELECT ONE OF THE FOLLOWING OPTIONS:")
    print("1. INSTRUCTIONS")
    print("2. PLAY THE GAME")
    print("3. EXIT THE PROGRAM")
    choice = input("Please select an option >>> ")
    if choice == "1":
        instructions()
    elif choice == "2":
        play()
    elif choice == "3":
        print("Thanks for using the program! Have a great day :)")
        sys.exit()
    else:
        print("Invalid Option! Please type \"1\", \"2\", or \"3\" ")
        main_menu()


def instructions():
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    print("INSTRUCTION OF THE GAME :)")


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

    num_cards = clean_input(
        "How many examples do you want?\n (Choose any integer) ", 1)

    cards = generate_cards(add_percent, low, high, num_cards)

    play(cards)


if __name__ == '__main__':
    main_menu()