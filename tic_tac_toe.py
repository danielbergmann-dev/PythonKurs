field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

active_player = "X"
run = True

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])

def next_move():
    global run
    while True:
        player_move = input("Enter your move: ")
        if player_move == "q":
            print("Game aborted")
            run = False
            return
        player_move = int(player_move)
        if 1 <= player_move <= 9:
            if field[player_move] == "X" or field[player_move] == "O":
                print("Invalid move. Try again")
            else:
                return player_move
        else:
            print("Invalid move. Try again")

def change_player():
    global active_player
    if active_player == "X":
        active_player = "O"
    else:
        active_player = "X"

def check_win():
    if field[1] == field[2] == field[3]:
        return True
    if field[4] == field[5] == field[6]:
        return True
    if field[7] == field[8] == field[9]:
        return True
    if field[1] == field[4] == field[7]:
        return True
    if field[2] == field[5] == field[8]:
        return True
    if field[3] == field[6] == field[9]:
        return True
    if field[1] == field[5] == field[9]:
        return True
    if field[3] == field[5] == field[7]:
        return True
    return False

def check_draw():
    for i in range(1, 9):
        if field[i] != "X" and field[i] != "O":
            return False
    return True

def game_repeat():
    global run, field
    newStart = input("Do you want to play again? (y/n): ")
    if newStart.lower() == "y":
        field = ["",
                 "1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]
        run = True
    else:
        run = False


while run:
    print_field()
    player_move = next_move()
    if player_move != None:
        field[player_move] = active_player
        if check_win():
            print_field()
            print("Player " + active_player + " wins!")
            run = False

        if check_draw():
            print("Game over. It's a draw!")
            run = False
        change_player()
    if not run:
        game_repeat()

