#!/usr/bin/python3
import itertools as it
def check_win(board):
    if (board[0]==board[1]==board[2]=="X") or (board[3]==board[4]==board[5]=="X") or (board[6]==board[7]==board[8]=="X") or (board[0]==board[3]==board[6]=="X") or (board[1]==board[4]==board[7]=="X") or (board[2]==board[5]==board[8]=="X") or (board[0]==board[4]==board[8]=="X") or (board[2]==board[4]==board[6]=="X"):
        return "P1"
    elif (board[0]==board[1]==board[2]=="O") or (board[3]==board[4]==board[5]=="O") or (board[6]==board[7]==board[8]=="O") or (board[0]==board[3]==board[6]=="O") or (board[1]==board[4]==board[7]=="O") or (board[2]==board[5]==board[8]=="O") or (board[0]==board[4]==board[8]=="O") or (board[2]==board[4]==board[6]=="O"):
        return "P2"
    else:
        return "D"


def fine_tune_win(board,data):
    if len(data)>5:
        for i in range(5,len(data)):
            fill_board(board,data[:i])
            if check_win(board) == "P1":
                return "P1"
            elif check_win(board) == "P2":
                return "P2"
        return "D"
    else:
        fill_board(board,data)
        return check_win(board)
        

def show_board(board):
    # for i in len(board):
    print(f"{board[0]}|{board[1]}|{board[2]}\n------\n{board[3]}|{board[4]}|{board[5]}\n------\n{board[6]}|{board[7]}|{board[8]}")

def fill_board(board,data):
    for i in range(len(data)):
        if i%2==0:
            board[data[i]] = "X"
        elif i%2==1:
            board[data[i]] = "O"
    return board



# fill_board(board,(0,1,2,3,4,5))
# show_board(board)
countT = 0
countP1 = 0
countP2 = 0
Umoves = [0,1,2,3,4,5,6,7,8]
Pmoves = []
# winStrategy = []
board = [" "]*9
while True:
    for i in it.permutations(Umoves,9):
        countT += 1
        board2 = [" "]*9
        if list(i[:len(Pmoves)]) == Pmoves:
            fill_board(board2,i)
            # print(test_win(board))
            if fine_tune_win(board2,i) == "P1":
                countP1 += 1
                # show_board(board2)
                print("\n")
            elif fine_tune_win(board2,i) == "P2":
                countP2+=1
                # countP1 += 1
            # winStrategy.append(i)
        


    print(f"There are {countT} ways to play for first 6 times")
    print(f"Among them you can win in {countP1} times")
    print(f"and lose {countP2} times")
    print(f"draws are {countT- (countP1+countP2)}")
    print(f"Your Success rate is {(countP1/countT)*100}%")
    print(f"Your Lose rate is {(countP2/countT)*100}%")
    print(f"Your draw rate is {((countT-(countP1+countP2))/countT)*100}%")


    fill_board(board,Pmoves)
    show_board(board)
    if fine_tune_win(board,Pmoves)=="P1":
        print("You're won")
        break
    elif fine_tune_win(board,Pmoves)=="P2":
        print("You lose!")
        break
    if len(Pmoves)>=len(Umoves):
        print("Draw!")
        break
    userIn = input("your move: ")
    if userIn in Pmoves:
        print("Invalid Move, Try Again")
    else:
        if userIn == "7":
            Pmoves.append(0)
        elif userIn == "8":
            Pmoves.append(1)
        elif userIn == "9":
            Pmoves.append(2)
        elif userIn == "4":
            Pmoves.append(3)
        elif userIn == "5":
            Pmoves.append(4)
        elif userIn == "6":
            Pmoves.append(5)
        elif userIn == "1":
            Pmoves.append(6)
        elif userIn == "2":
            Pmoves.append(7)
        elif userIn == "3":
            Pmoves.append(8)
        else:
            print("please Try Again")
            break


# for i in it.permutations(Umoves,9):
#     # if 
#     countT += 1
#     board2 = [" "]*9
#     fill_board(board2,i)
#     # print(test_win(board))
#     if fine_tune_win(board2,i) == "P1":
#         countP1 += 1
#         show_board(board2)
#         print("\n")
#     elif fine_tune_win(board2,i) == "P2":
#         countP2+=1
#         # countP1 += 1
#         # winStrategy.append(i)
        


# print(f"There are {countT} ways to play for first 6 times")
# print(f"Among them you can win in {countP1} times")
# print(f"and lose {countP2} times")
# print(f"draws are {countT- (countP1+countP2)}")
# print(f"Your Success rate is {(countP1/countT)*100}%")
# print(f"Your Lose rate is {(countP2/countT)*100}%")
# print(f"Your draw rate is {((countT-(countP1+countP2))/countT)*100}%")