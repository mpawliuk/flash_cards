# This is where the main system of the flash  card game will go
import sys

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

def play():
    #TODO:
    # 1. call the game
    # 2. interaction with user
    # 3. trigger queue (queue needs need to sort by time and user's question selection.)