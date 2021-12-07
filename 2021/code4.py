# BINGO
import os
import pandas as pd
import numpy as np

# inputfile = 'test_data4.txt'
inputfile = 'data4.txt'

# read data
with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines() if line.strip()]

numbers = [int(x) for x in list(lines[0].split(','))]

tsize = 5
ntables = len(lines[1:])//tsize
nrows = tsize*ntables
tables = np.zeros((nrows, tsize)).astype(int)

ir = 1
lines[ir+1].lstrip().split(',')

for ir in range(nrows):
    ir_numbers = [int(x) for x in list(lines[ir+1].split())]
    tables[ir,:] = ir_numbers

# # fille the numbers called
# called = np.zeros((nrows, tsize)).astype(bool)
# not_winner_yet = True; i = 0
# while not_winner_yet:
#     ni = numbers[i]
#     print('bingo: calling number {}'.format(ni))
#     called[tables==ni] = True
#
#     for ir in range(nrows):
#         if np.sum(called[ir,:])==5:
#             print('we have a winning board')
#             print('row = {}'.format(tables[ir, :]))
#             not_winner_yet = False
#             # get number of the winning board and the board itself
#             it = ir // tsize
#             itr = ir % tsize
#             winner_board = tables[it*tsize:(it+1)*(tsize), :]
#             winner_marked = called[it*tsize:(it+1)*(tsize), :]
#             unmarked_num = winner_board[~winner_marked]
#             score = np.sum(unmarked_num)*ni
#             print('First board to win: the winning score is = {}'.format(score))
#     i += 1

nboards = nrows//tsize

# fille the numbers called
BOARD_HAS_WON = np.zeros(nboards).astype(bool)
WINNING_SCORE = np.zeros(nboards).astype(int)

called = np.zeros((nrows, tsize)).astype(bool)
already_called = np.zeros((nrows, tsize)).astype(bool)
# not_winner_ye t = True; i = 0
i = 0
# while not_winner_yet:
while np.sum(BOARD_HAS_WON) < np.size(BOARD_HAS_WON): # until last number is called
    ni = numbers[i]
    print('bingo: calling number {}'.format(ni))
    called[tables==ni] = True

    for it in range(nboards):
        current_board = tables[it * tsize:(it + 1) * (tsize), :].copy()
        current_marked = called[it * tsize:(it + 1) * (tsize), :].copy()

        for ic in range(tsize):
            current_row = current_marked[ic, :]
            current_col = current_marked[:, ic]
            if (np.sum(current_row) == tsize or np.sum(current_col) == tsize) and BOARD_HAS_WON[it] == False:
                print('board number {} has just won'.format(it))
                BOARD_HAS_WON[it] = True
                print('with ni = {}, winning score = {}'.format(ni, WINNING_SCORE[it]))
                WINNING_SCORE[it] = np.sum(current_board[~current_marked])*ni

                if np.sum(BOARD_HAS_WON) == 1:
                    print('first winning board = {}'.format(it))
                    print('first board to win: the winning score is = {}'.format(WINNING_SCORE[it]))

                if np.sum(BOARD_HAS_WON) == np.size(BOARD_HAS_WON):
                    print('last winning board = {}'.format(it))
                    print('last board to win: the winning score is = {}'.format(WINNING_SCORE[it]))
    i += 1
    # already_called = called.copy()

# print(BOARD_HAS_WON)



