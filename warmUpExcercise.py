game_list1 = ["-", "-", "-"]
game_list2 = ["-", "-", "-"]
game_list3 = ["-", "-", "-"]
game_list = [game_list1, game_list2, game_list3]

player_one = True


def display_game(game_list: list) -> str or list:
    print("Here is the current list")
    index = 0
    for list in game_list:
        print(index, list)
        index += 1


def position_choice():
    choice = 'wrong'
    global player_one
    while choice not in ['0', '1', '2']:
        choice = input("Player {} pick a row position 0-2: ".format("1" if player_one else "2"))
        if choice not in ['0', '1', '2']:
            print("Sorry invalid choice!")
    return int(choice)


def col_position_choice():
    choice = 'wrong'
    global player_one
    while choice not in ['0', '1', '2']:
        choice = input("Player {} pick a row position 0-2: ".format("1" if player_one else "2"))
        if choice not in ['0', '1', '2']:
            print("Sorry invalid choice!")
    return int(choice)


def replacement_choice(gameList, position, col_position):
    global player_one
    user_placement = ""
    # user_placement = input("Type a string to place at position: ")
    if gameList[position][col_position] == 'X' or gameList[position][col_position] == 'O':
        print("Sorry, That position is already taken!")
    else:
        if player_one:
            player_one = False
            user_placement = 'X'

        else:
            player_one = True
            user_placement = '0'

        gameList[position][col_position] = user_placement
    return gameList


def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input('Keep playing? (Y or N): ')
        if choice not in ['Y', 'N', 'y', 'n']:
            print("Sorry I don't understand (Y/N)? ")
    if choice == 'Y' or choice == 'y':
        return True
    else:
        return False


def check_winner(game_list):
    for list in game_list:
        if list[0] == list[1] == list[2] == 'X':
            print("Player 1 wins!")
            return False
        elif list[0] == list[1] == list[2] == 'O':
            print("Player 2 wins!")
            return False
        else:
            return True


game_on = True


def add(a, b):
    return a + b

    while game_on:
        display_game(game_list)
        position = position_choice()
        col_position = col_position_choice()
        game_list = replacement_choice(game_list, position, col_position)
        display_game(game_list)
        game_on = check_winner(game_list)
        if game_on:
            game_on = gameon_choice()
