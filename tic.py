import os
import time
import random

board = [" "," "," "," "," "," "," "," "," "," "]


def print_borad():
    print("       |             |       ")
    print("       |             |       ")
    print("    ",board[1],"| ","    ",board[2],"    | ",board[3])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")
    print("    ",board[4],"| ","    ",board[5],"    | ",board[6])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")
    print("    ",board[7],"| ","    ",board[8],"    | ",board[9])
    print("=============================")
    print("       |             |       ")
    print("       |             |       ")



while True:
    print_borad()
    choice = int(input("please chose an empty slot"))


    if board[choice] == ' ':
        board[choice] ='x'
    else:
        print("sorry please select an empty slot")

    #chweack for win
    if(board[1]=='x' and board[2]== 'x' and board[3]=='x'):
        print_borad()
        print("x wins!!!")
        break
    
