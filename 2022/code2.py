
import os
import numpy as np
import pandas as pd


# inputfile = "test_data2.txt"
inputfile = "data2.txt"

def compare(elf0, me0):
    score = 0
    if (elf0 == 'A'): elf=1
    if (elf0 == 'B'): elf=2
    if (elf0 == 'C'): elf=3
    if (me0 == 'X'):  me=1
    if (me0 == 'Y'):  me=2
    if (me0 == 'Z'):  me=3

    score = score + me

    if ((me-elf==+1 or me-elf==-2)):
        score = score + 6 # win
    elif (elf-me == 0):
        score = score + 3 # draw
    else:
        score = score + 0 # loss

    print(elf,me,score)
    return score

def compare2(elf0, me0):
    score = 0
    if (elf0 == 'A'): elf=1
    if (elf0 == 'B'): elf=2
    if (elf0 == 'C'): elf=3
    if (me0 == 'X'):  score = 0 # lose
    if (me0 == 'Y'):  score = 3 # draw
    if (me0 == 'Z'):  score = 6 # win

    if score == 3: # need to draw, so use same shape
        score = score + elf
    elif score == 6: # need to win
        if elf == 3:
            score = score + elf - 2
        else:
            score = score + elf + 1
    elif score == 0: # need to lose
        if elf == 1:
            score = score + elf + 2
        else:
            score = score + elf - 1
    return score

df = pd.read_csv(inputfile, header=None, sep='\s+')
print(df)
Elf = df[0].values
Me = df[1].values
print(Elf, Me)
nt = len(Elf)
scores = np.zeros(nt, dtype=int)
scores2 = np.zeros(nt, dtype=int)
for i in range(nt):
    scores[i] = compare(Elf[i], Me[i])
    scores2[i] = compare2(Elf[i], Me[i])

print('Part 1 :: My total score is = {}'.format(np.sum(scores)))
print('Part 2 :: My total score is = {}'.format(np.sum(scores2)))




