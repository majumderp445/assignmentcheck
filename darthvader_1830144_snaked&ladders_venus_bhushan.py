# -*- coding: utf-8 -*-
"""DarthVader_1830144_Snaked&Ladders - VENUS BHUSHAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mSU27K51MumMGjblIiQIDzSXpJ_WgqHV
"""

## Getting 6 on 'roll' gives 1 extra 'roll' chance
## IF P1 reaches P2, P2 sent to 0 
import random
MAX=6
RNG=21
snake_ladder = {17: 7, 54: 34, 62: 19, 98: 79, 3: 38, 24: 33, 42: 93, 72: 84}
commands = ["roll"]
commands.extend([str(i) for i in range(1, RNG)])

def begin():
    print("###### Welcome to snakes and ladders ######")
    p1 = input("Enter the name of player 1 :")
    p2 = input("Enter the name of player 2 :")
    print("###### Let us start ######")

def roll():
    dice = random.randint(1, MAX)
    print("You got a:", dice)
    return dice

def command(cmd, pl, p):
    old = pl
    if cmd in commands:
        if cmd == "roll":
            temp = roll()
            pl = pl + temp
            if temp == 6:
                print(p + " got 6, one more chance for you")
                x = None
                while x != 'roll':
                    x = input(p + ":")
                temp = roll()
                pl = pl + temp
                if pl > 100:
                    pl = old

        else:
            temp = int(cmd)
            print("You got a :", temp)
            pl = pl + temp
    else:
        cmd = input(p + ":")
        pl = command(cmd, pl, p)

    if pl in snake_ladder.keys():
        pl = snake_ladder[pl]
    if pl <= 100:
        return pl
    return old

if __name__ == "__main__":

    pl_1, pl_2 = 0, 0
    begin()

    while (pl_1 < 100) and (pl_2 < 100):
        cmd_1 = input("Player 1:")
        if cmd_1 == "quit":
            pl_2 = 100
            break

        pl_1 = command(cmd_1, pl_1, "Player 1")
        if pl_1 == pl_2:
            pl_2 = 0
            print("\nPlayer 2 was cut & sent back to start\n")

        print("    Your final position is ", pl_1)

        if pl_1 < 100:
            cmd_2 = input("Player 2:")
            if cmd_2 == "quit":
                pl_1 = 100
                break

            pl_2 = command(cmd_2, pl_2, "Player 2")
            if pl_1 == pl_2:
                pl_1 = 0
                print("\nPlayer 1 was cut sent back to 0\n")
            print("Your final position is ", pl_2)

    if pl_1 == 100:
        print("Player 1 won the game")
    else:
        print("Player 2 won the game")

    print("###### Game Successfully Finished ######")

