board = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
def printboard(board):
    print(board['1'] + '  |'+board['2']+'  |'+board['3'])
    print('---|---|---')
    print(board['4'] + '  |'+board['5']+'  |' + board['6'])
    print('---|---|---')
    print(board['7'] + '  |'+board['8']+'  |' + board['9'])
printboard(board)

import random

jucator = ["Human", "Robot"]

print(random.choice(jucator))
if random.choice(jucator) == jucator[0]:
    print("Jucatorul alege prima mutare")
else:
    print("Robotul alege prima mutare")

def winner(comb, player):
    win_comb = [
        [comb[0], comb[1], comb[2]],
        [comb[3], comb[4], comb[5]],
        [comb[6], comb[7], comb[8]],
        [comb[0], comb[3], comb[6]],
        [comb[1], comb[4], comb[7]],
        [comb[2], comb[5], comb[8]],
        [comb[0], comb[4], comb[8]],
        [comb[2], comb[4], comb[6]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def main(board)
    while len(empty(board)) > 0 and not game_over(board):
        human_turn(board)
        AI_Move()
        if winner(board, "X"):
            print("Ai castigat!")
            return 0
        elif winner(board, "0"):
            print("Ai pierdut!")
            return 0
        else:
            print("Remiza")
            return 0

def empty(board):
    result = []
    for i, j in enumerate(board):
        if j == " ":
            restult.append(i)
    return result

if name == "main":
    while True:
        main(board)
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        again = input("Vrei sa joci din nou? [y/n]:")
        if again == "n":
            print("Jocul s-a incheiat!")
            break
