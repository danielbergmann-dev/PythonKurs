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

while run:
    print_field()
    player_move = next_move()
    field[player_move] = active_player
    change_player()
