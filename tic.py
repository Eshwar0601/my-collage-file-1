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
    os.system("clear")
    print_borad()
    choice = int(input("please chose an empty slot"))

    board[choice] = 'x'
