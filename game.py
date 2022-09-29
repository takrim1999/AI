#!/usr/bin/python3
def print_board(board):
    print(f"{board[0][0]}||{board[0][1]}||{board[0][2]}")

board = [[None]*3]*3
print(board)
for i in range(3):
    for j in range(3):
        print(board[i][j])

