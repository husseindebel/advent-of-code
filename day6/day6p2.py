#!/usr/bin/python2.7

### light_board[row][column]
import re

DIMENSION = 1000 ## square board DIMENSIONxDIMENSION
INCREASE = 1
DECREASE = -1
TOGGLE = 2


string = r"(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)"

def show_board(board):
    for row in board:
        print row

def turn_lights(board, row_start, row_end, col_start, col_end, switch):
    row = int(row_start)
    while row <= int(row_end):
        col = int(col_start)
        while col <= int(col_end):
            if switch == 2:
                board[row][col] += 2
            else:
                if switch == 1:
                    board[row][col] += 1
                elif switch == -1:
                    if board[row][col] != 0:
                        board[row][col] -= 1
            col += 1
        row += 1

light_board = [[0 for i in range(DIMENSION)] for j in range(DIMENSION)]
filename = "day6_input"
with open(filename) as f:
    while True:
        instruction = f.readline().rstrip()
        if not instruction:
            break
        pattern = re.compile(string)

        action = pattern.search(instruction).group(1)

        row_start = pattern.search(instruction).group(2)
        col_start = pattern.search(instruction).group(3)

        row_end = pattern.search(instruction).group(4)
        col_end = pattern.search(instruction).group(5)

        if action == "turn off":
            turn_lights(light_board, row_start, row_end, col_start, col_end, DECREASE)
        if action == "turn on":
            turn_lights(light_board, row_start, row_end, col_start, col_end, INCREASE)
        if action == "toggle":
            turn_lights(light_board, row_start, row_end, col_start, col_end, TOGGLE)

bright_lights = 0
for row in light_board:
    for light in row:
        bright_lights += light

print bright_lights
