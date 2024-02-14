#rock-paper-scissors-lizard-spock
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

if ((int(player_input) <= 5) and (int(player_input) >= 0)):
    player_choice = int(player_input)
else:
    sys.exit("🙏 Please enter an integer value between 0 and 5 🙏")

computer_choice = random.randint(1,5)

print("You chose: ", GAME(player_choice).name)
print("Sheldon chose: ", GAME(computer_choice).name)

