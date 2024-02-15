#rock-paper-scissors-lizard-spock || YOU vs. Sheldon Cooper
import sys
import random
from enum import Enum

class GAME(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LIZARD = 4
    SPOCK = 5

PLAYER = 0
SHELDON = 0

replay = True

while replay:

    print("\nChoose your move! [0 for RULES!]")
    player_input = input("\n1. ROCK 🪨\n2. PAPER 📄\n3. SCISSORS 🗡️\n4. LIZARD 🦎\n5. SPOCK 🖖\n\n")

    if (int(player_input) == 0):
        rules = '''
        Scissors cuts paper.
        Paper covers rock.
        Rock crushes lizard.
        Lizard poisons Spock.
        Spock smashes scissors.
        Scissors decapitates lizard.
        Lizard eats paper.
        Paper disproves Spock.
        Spock vaporizes rock.
        Rock crushes scissors.
        '''
        print(rules)
        continue
    elif ((int(player_input) <= 5) and (int(player_input) >= 1)):
        player_choice = int(player_input)
    else:
        sys.exit("🙏 Please enter an integer value between 0 and 5 🙏")

    computer_choice = random.randint(1,5)

    print("\nYou chose: ", GAME(player_choice).name)
    print("\nSheldon chose: ", GAME(computer_choice).name)

    if player_choice == computer_choice:
        print("\n🤝 It's a tie! 🤝")
        continue

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
    replay = input("\nPlay again? \nY for Yes | Enter any thing else to Quit\n\n")

    if replay.lower() == "y":
        continue
    else:
        print("\n❗️F I N A L  S C O R E S❗️".center(30, " "))
        print("\nP L A Y E R".ljust(26, " ") + str(PLAYER).rjust(2))
        print("\nS H E L D O N".ljust(26, " ") + str(SHELDON).rjust(2))
        print("\n🫶  Thank you for playing! 🫶\n")
        replay = False