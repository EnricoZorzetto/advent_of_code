# FISHES
import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# inputfile = 'test_data6.txt'
inputfile = 'data6.txt'

# read data
with open(inputfile) as file:
    # lines = [line.rstrip('\n').split() for line in file.readlines() if line.strip()]
    lines = [line.rstrip('\n').split(',') for line in file.readlines() if line.strip()][0]
oldfishes =  [int(i) for i in lines]


def number_of_sons(oldfishes, deltat = 0):
    # deltat = 18
    myfishes = oldfishes.copy()
    finalt = deltat + 1  # number of simulation days
    for t in range(finalt):
        nf = len(myfishes)
        # print('time = {}, nf = {}, fishes = {}'.format(t, nf, myfishes))
        print('time = {}, nf = {}'.format(t, nf))
        myfishes = [i - 1 for i in oldfishes]
        for i in range(nf):
            if myfishes[i] < 0:
                myfishes[i] = 6
                myfishes.append(8)
        if t < finalt - 1:
            oldfishes = myfishes
    return nf, oldfishes

# do_part_1 = True
# if do_part_1:
deltat1 = 128
nft, finfishes = number_of_sons(oldfishes, deltat = deltat1)
print('part 1: number of fishes after {} days is = {}'.format(deltat1, nft))

# deltat = 256
# ncomp = 4
# deltati = deltat // ncomp
# assert deltat % ncomp == 0
# finfishes = oldfishes.copy() # starting point
# for ic in range(ncomp):
#     oldfishes_vec = np.array(finfishes)
#     uniquef = np.unique(oldfishes_vec).astype(int)
#     numf = [len(oldfishes_vec[oldfishes_vec == fish]) for fish in list(uniquef)]
#     nuniques = len(uniquef)
#     sons = np.zeros(nuniques)
#     finfishes = []
#     for fi in range(nuniques):
#         parent = [uniquef[fi]]
#         sons[fi], ff2 = number_of_sons(parent, deltat=deltati)
#         finfishes += ff2
# totfishes = np.sum(sons * numf).astype(int)
# print('part 2: number of fishes after {} days is {}'.format(deltat, totfishes))

deltat2 = 256
deltat_remain = deltat2 - deltat1
oldfishes_vec = np.array(finfishes)
uniquef = np.unique(oldfishes_vec).astype(int)
numf = [len(oldfishes_vec[oldfishes_vec==fish]) for fish in list(uniquef)]
nuniques = len(uniquef)
sons = np.zeros(nuniques)
for fi in range(nuniques):
    parent = [uniquef[fi]]
    sons[fi], ff2 = number_of_sons(parent, deltat=deltat_remain)
totfishes = np.sum(sons*numf).astype(int)
print('part 2: number of fishes after {} days is {}'.format(deltat2, totfishes))
