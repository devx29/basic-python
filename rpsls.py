#rock-paper-scissors-lizard-spock || YOU vs. Sheldon Cooper
import sys
import random
from enum import Enum

total_games = 0
tied_games = 0
PLAYER = 0
SHELDON = 0

def play():

    global PLAYER
    global SHELDON
    global total_games
    global tied_games

    class GAME(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        LIZARD = 4
        SPOCK = 5

    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("\nChoose your move!")
    player_input = input("\n1. ROCK 🪨\n2. PAPER 📄\n3. SCISSORS 🗡️\n4. LIZARD 🦎\n5. SPOCK 🖖\n\n")

    if player_input not in ["1", "2", "3", "4", "5"]:
        print("\n🙏 Please enter a value between 0 and 5 🙏")
        play()
    
    player_choice = int(player_input)
    computer_choice = random.randint(1,5)

    total_games += 1
    
    print("You chose: ".ljust(15), GAME(player_choice).name)
    print("Sheldon chose: ".ljust(15), GAME(computer_choice).name)

    if player_choice == computer_choice:
        tied_games += 1
        print("\n🤝 It's a tie! 🤝")
        play()

    match player_choice:
        case 1:
            if computer_choice in (3,4):
                print("\n 🏆 You win! 🏆")
                PLAYER += 1
            else:
                print("\n😭 You lose! 😭")
                SHELDON += 1
        case 2:
            if computer_choice in (1,5):
                print("\n 🏆 You win! 🏆")
                PLAYER += 1
            else:
                print("\n😭 You lose! 😭")
                SHELDON += 1
        case 3:
            if computer_choice in (2,4):
                print("\n 🏆 You win! 🏆")
                PLAYER += 1
            else:
                print("\n😭 You lose! 😭")
                SHELDON += 1
        case 4:
            if computer_choice in (2,5):
                print("\n 🏆 You win! 🏆")
                PLAYER += 1
            else:
                print("\n😭 You lose! 😭")
                SHELDON += 1
        case 5:
            if computer_choice in (1,3):
                print("\n 🏆 You win! 🏆")
                PLAYER += 1
            else:
                print("\n😭 You lose! 😭")
                SHELDON += 1

    print('\nCurrent Score: \nYOU     =>', PLAYER, '\nSHELDON =>', SHELDON)
    print("\nPlay again? \n")
    replay = input("Y for Yes | Enter any thing else to Quit\n\n")

    if replay.lower() == "y":
        return play()
    else:
        print("\n❗️F I N A L  S C O R E S❗️".center(30, " "))
        print("\nP L A Y E R".ljust(26, " ") + str(PLAYER).rjust(2))
        print("\nS H E L D O N".ljust(26, " ") + str(SHELDON).rjust(2))
        print("\nT I E D   G A M E S".ljust(26, " ") + str(tied_games).rjust(2))
        print("\nT O T A L   G A M E S".ljust(26, " ") + str(total_games).rjust(2))
        sys.exit("\n🫶  Thank you for playing! 🫶\n")

play()