#closure

def game(player, points):
    def play_game():
        nonlocal points
        points -= 1

        if points > 1:
            print("\n" + player + " has " + str(points) + " points")
        elif points == 1:
            print("\n" + player + " has " + str(points) + " point")
        else:
            print("\n" + player + " has no points")
    return play_game


player_1 = game("Harsh ", 3)
player_2 = game("Krish", 5)

player_1()
player_1()
player_1()
player_1()
player_2()
player_2()