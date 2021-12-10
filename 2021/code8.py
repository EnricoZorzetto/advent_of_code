import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# inputfile = 'test_data8b.txt'
# inputfile = 'test_data8.txt'
inputfile = 'data8.txt'



# read data
with open(inputfile) as file:
    # lines = [line.rstrip('\n').split() for line in file.readlines() if line.strip()]
    lines = [line.rstrip('\n').split(',') for line in file.readlines()]
# inp =  np.array( [int(i) for i in lines] )


# how many times 1,4,7,8 appear (2, 3, 4, 7)

sec = [f[0].split('|')[1].split() for f in lines]
bef =  [f[0].split('|')[0].split() for f in lines]
all = [s+b for s, b in zip(sec, bef)]

nn = len(sec)
nd = len(sec[0])
count = 0
for ni in range(nn):
    for di in range(nd):
        print(ni, di)
        print(  sec[ni][di] )
        if len( sec[ni][di] ) in [2, 3, 4, 7]:
            count += 1
print('part1: result = {}'.format(count))


# part 2: decode signal:



# myvalues = np.zeros((nn, nd)).astype(int)
nn = len(sec)
MYVAL = np.zeros(nn).astype(int)
# ni = 0
for ni in range(nn):

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    LETTERS = ['' for _ in letters]

    bef0 = bef[ni]
    nb = len(bef0)
    num0 = 10 * np.ones(nb).astype(int)
    eight = None; four = None; seven = None; one = None
    for bi, bin in enumerate(bef0):
        if len(bin) == 2:
            one = bin; num0[bi] = 1
        if len(bin) == 3:
            seven = bin; num0[bi] = 7
        if len(bin) == 4:
            four = bin; num0[bi] = 4
        if len(bin) == 7:
            eight = bin; num0[bi] = 8

    # reamining:



    # FIRST LETTER
    for ile, let in enumerate(letters):
        if let in seven and let not in one:
            print(let)
            LETTERS[ile] = 'A'
            print(letters[ile])

    # # SECOND LETTER
    bef1 = [ bef0[iib] for iib in range(len(bef0)) if num0[iib] > 9]
    for ile, let in enumerate(letters):
        count1 = 0
        for bel in bef1:
            if let in bel and LETTERS[ile] == '': count1 += 1
        print(count1)
        if count1 == len(bef1):
            LETTERS[ile] = 'G'


    # THIRD LETTER: D IS IN ALL EXCEPT 3, G IS THE SAME BUT ALREADY GONE
    for ile, let in enumerate(letters):
        count1 = 0
        for bel in bef0:
            if let in bel and LETTERS[ile] == '': count1 += 1
        print(count1)
        if count1 == len(bef0)-3:
            LETTERS[ile] = 'D'


    for ile, let in enumerate(letters):
        count1 = 0
        for bel in bef0:
            if let in bel and LETTERS[ile] == '': count1 += 1
        print(count1)
        if count1 == len(bef0)-2:
            LETTERS[ile] = 'E' # C


    for ile, let in enumerate(letters):
        count1 = 0
        for bel in bef0:
            if let in bel and LETTERS[ile] == '': count1 += 1
        print(count1)
        if count1 == len(bef0)-1:
            LETTERS[ile] = 'F'


    for ile, let in enumerate(letters):
        count1 = 0
        for bel in bef0:
            if let in bel and LETTERS[ile] == '': count1 += 1
        print(count1)
        if count1 == len(bef0)-6:
            LETTERS[ile] = 'C' # E


    for ile, let in enumerate(letters):
        count1 = 0
        for bel in bef0:
            if let in bel and LETTERS[ile] == '': count1 += 1
        print(count1)
        if count1 == len(bef0)-4:
            LETTERS[ile] = 'B'


    # the remaining must be Gs
    # for ile, let in enumerate(letters):
    #     if LETTERS[ile] =='':
    #         LETTERS[ile]='G'

    LETTERS  = [a.lower() for a in LETTERS]




    # nn0 = tran('ab', letters, LETTERS)
    print(letters)
    print(LETTERS)
    # print(nn0)

    def sorts(a_string):
        sorted_characters = sorted(a_string)
        return "".join(sorted_characters)


    # sorts("che")

    def tran(orig, letters0, LETTERS0):
        orig = list(orig)
        new0 = [None for _ in orig]
        # print(new, len(new))
        for nix in range(len(new0)):
            for lix in range(len(letters0)):
                if orig[nix] == letters0[lix]:
                    new0[nix] = LETTERS0[lix].lower()
        return "".join(new0)


    original_values = {
        sorts('abcdefg'): 8,
        sorts('abdfg'): 5,
        sorts('aedcg'): 2,
        sorts('aedfg'): 3,
        sorts('aef'): 7,
        sorts('aefdbg'): 9,
        sorts('abcdfg'): 6,
        sorts('bdef'): 4,
        sorts('abcgfe'): 0,
        sorts('ef'): 1
    }

    print(ni)
    sec0 = sec[ni]
    nd = len(sec0)
    orig_strings = [sorts(f) for f in original_values.keys() ]
    orig_values = [ f for f in original_values.values() ]
    # new_strings = [sorts(tran(f, letters, LETTERS)) for f in original_values.keys() ]
    new_strings = [sorts(tran(f, LETTERS, letters)) for f in original_values.keys() ]

    # tran('ef', LETTERS, letters)
    # bef0 = bef[ni]
    # new_bef0 = [sorts(tran(f, letters, LETTERS)) for f in bef0 ]
    # val_bef0 = [original_values[ sorts(tran(f, letters, LETTERS)) ] for f in bef0 ]
    new_sec0 = [sorts(tran(f, letters, LETTERS)) for f in sec0 ]
    val_sec0 = [original_values[ sorts(tran(f, letters, LETTERS)) ] for f in sec0 ]
    MYVAL[ni] = int( val_sec0[0])*1000 + int( val_sec0[1])*100 + int( val_sec0[2])*10 + int( val_sec0[3])

print('part2: sum of all output values is = {}'.format(np.sum(MYVAL)))
