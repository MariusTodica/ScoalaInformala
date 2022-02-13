board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

print("Alegi primul!")
active_game = True
move = ""
tie = False

def winner():
    global active_game
    if board[0] == board[1] == board[2] != "-" or board[3] == board[4] == board[5] != "-"\
            or board[6] == board[7] == board[8] != "-":
        active_game = False
    elif board[0] == board[3] == board[6] != "-" or board[1] == board[4] == board[7] != "-" \
            or board[2] == board[5] == board[8] != "-":
        active_game = False
    elif board[0] == board[4] == board[8] != "-" or board[2] == board[4] == board[6] != "-":
        active_game = False


def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("--|---|--")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("--|---|--")
  print(board[6] + " | " + board[7] + " | " + board[8])

display_board()

while active_game:
    if "-" in board:
        jucator = input("Alege un numar intre 1 si 9: ")
        if jucator not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            continue
        else:
            index = int(jucator) - 1
            if board[index] == "-":
                board[index] = "X"
                move = "X"
                winner()
                if not active_game:
                    display_board()
                    break

                positions = [4, 0, 2, 6, 8, 1, 3, 5, 7]
                for i in positions:
                    if board[i] == "-":
                        board[i] = "O"
                        move = "O"
                        display_board()
                        winner()
                        break
            else:
                print("Pozitia este deja ocupata.")
                display_board()
                continue
    else:
        display_board()
        print("Egalitate!")
        tie = True
        break

if tie is False:
    if move == "O":
        print("Ai pierdut!")
    else:
        print("Ai castigat!")