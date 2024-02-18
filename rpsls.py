#rock-paper-scissors-lizard-spock || YOU vs. Sheldon Cooper
import sys
import random
from enum import Enum

def rpsls(name="PLAYER"):
    total_games = 0
    tied_games = 0
    PLAYER = 0
    SHELDON = 0

    def play():

        nonlocal PLAYER
        nonlocal SHELDON
        nonlocal total_games
        nonlocal tied_games
        nonlocal name

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
        
        print(f"{name.capitalize()} chose: ".ljust(15) + f"{GAME(player_choice).name}")
        print("Sheldon chose: ".ljust(15) + f"{GAME(computer_choice).name}")

        if player_choice == computer_choice:
            tied_games += 1
            print("\n🤝 It's a tie! 🤝")
            play()

        match player_choice:
            case 1:
                if computer_choice in (3,4):
                    print(f"\n 🏆 {name.capitalize()} wins! 🏆")
                    PLAYER += 1
                else:
                    print("\n😭 Sheldon wins! 😭")
                    SHELDON += 1
            case 2:
                if computer_choice in (1,5):
                    print(f"\n 🏆 {name.capitalize()} wins! 🏆")
                    PLAYER += 1
                else:
                    print("\n😭 Sheldon wins! 😭")
                    SHELDON += 1
            case 3:
                if computer_choice in (2,4):
                    print(f"\n 🏆 {name.capitalize()} wins! 🏆")
                    PLAYER += 1
                else:
                    print("\n😭 Sheldon wins! 😭")
                    SHELDON += 1
            case 4:
                if computer_choice in (2,5):
                    print(f"\n 🏆 {name.capitalize()} wins! 🏆")
                    PLAYER += 1
                else:
                    print("\n😭 Sheldon wins! 😭")
                    SHELDON += 1
            case 5:
                if computer_choice in (1,3):
                    print(f"\n 🏆 {name.capitalize()} wins! 🏆")
                    PLAYER += 1
                else:
                    print("\n😭 Sheldon wins! 😭")
                    SHELDON += 1
        
        print("\nCurrent Score:")
        print(f"{name.upper()}".ljust(10) + f"{PLAYER}")
        print("SHELDON".ljust(10) + f"{SHELDON}")
        
        print("\nPlay again? \n")
        replay = input("Y for Yes | Enter any thing else to Quit\n")

        if replay.lower() == "y":
            return play()
        else:
            print("\n❗️FINAL SCORES❗️".center(10, " "))
            print(f"\n{name.upper()}".ljust(12).center(15, " ") + f"{str(PLAYER).rjust(2)}")
            print("\nSHELDON".ljust(12).center(15, " ") + f"{str(SHELDON).rjust(2)}")
            print("\nTIED GAMES".ljust(12).center(15, " ") + f"{str(tied_games).rjust(2)}")
            print("\nTOTAL GAMES".ljust(12).center(15, " ") + f"{str(total_games).rjust(2)}")
            sys.exit("\n🫶  Thank you for playing! 🫶\n")
    
    return play()

if __name__ == "__main__":
    rpsls()