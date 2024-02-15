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

print("Choose your move! [0 for RULES!]")
player_input = input("1. ROCK 🪨\n2. PAPER 📄\n3. SCISSORS 🗡️\n4. LIZARD 🦎\n5. SPOCK 🖖\n")

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
    sys.exit(rules)
elif ((int(player_input) <= 5) and (int(player_input) >= 1)):
    player_choice = int(player_input)
else:
    sys.exit("🙏 Please enter an integer value between 0 and 5 🙏")

computer_choice = random.randint(1,5)

print("You chose: ", GAME(player_choice).name)
print("Sheldon chose: ", GAME(computer_choice).name)

if player_choice == computer_choice:
    sys.exit("It's a tie!")

match player_choice:
    case 1:
        print("You win!") if computer_choice in (3,4) else print("You lose!")
    case 2:
        print("You win!") if computer_choice in (1,5) else print("You lose!")
    case 3:
        print("You win!") if computer_choice in (2,4) else print("You lose!")
    case 4:
        print("You win!") if computer_choice in (2,5) else print("You lose!")
    case 5:
        print("You win!") if computer_choice in (1,3) else print("You lose!")