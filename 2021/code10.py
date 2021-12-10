import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# inputfile = 'test_data10.txt'
inputfile = 'data10.txt'


with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]



def get_score(ADDED):
    print('computing score for {}'.format("".join(ADDED)))
    score = 0
    for ad in ADDED:
        score *= 5
        score += get_pscores(ad)
        print(ad, score)
    return score


def flipp(string):
    if string == '(': return ')'
    elif string == '<': return '>'
    elif string == '[': return ']'
    elif string == '{': return '}'
    elif string == ')': return '('
    elif string == '>': return '<'
    elif string == ']': return '['
    elif string == '}': return '{'
    else: raise Exception('flipp: provide valid bracket')
    return


def get_pvalue(string):
    if string == '(' or string == ')': return 3
    elif string == '[' or string == ']': return 57
    elif string == '{' or string == '}': return 1197
    elif string == '<' or string == '>': return 25137
    else: raise Exception('get_pvalue: provide valid bracket')
    return


def get_pscores(string):
    if string == '(' or string == ')': return 1
    elif string == '[' or string == ']': return 2
    elif string == '{' or string == '}': return 3
    elif string == '<' or string == '>': return 4
    else: raise Exception('get_pscores: provide valid bracket')
    return

OPEN = ['(', '[', '{', '<']
CLOS = [')', ']', '}', '>']

COUPLES = ['()', '[]', '{}', '<>']
nchars = len(COUPLES)

def reduce_couples(st0):
    reduced = True
    st1 = st0
    while reduced == True:
        # st1 = st0
        for cop in COUPLES:
            st1 = st1.replace(cop, '')
            # print(st1)
        if len(st1) == len(st0): reduced = False
        st0 = st1
    return st1


nstrings = len(lines)
PVALUE = []
CORRUPTED = np.zeros(nstrings)
for iss in range(nstrings):
    # st = lines[iss]
    st = reduce_couples( lines[iss] )
    print(st)

    lest = len(st)
    opened = False
    found_error = False
    for i  in range(lest):
        # print(st[i])
        if st[i] in OPEN and not found_error:
            lastopen = st[i]
            opened = True
        elif st[i] in CLOS and i > 0 and opened and not found_error:
            # print('closing {}'.format(st[i]))
            if st[i] != flipp(lastopen):
                pvalue = get_pvalue( st[i] )
                PVALUE.append(pvalue)
                CORRUPTED[iss] = True
                found_error = True
                print('string {}, closure error! with values = {}'.format(iss, pvalue))
        # else: print('something is weird. Start with close??')
print("part 1: total error value = {}".format(sum(PVALUE)))

mylines = [ll for il, ll in enumerate(lines) if not CORRUPTED[il] ]
nmystrings = len(mylines)
print('part2:: {} strings remaining out of {}'.format(nmystrings, nstrings))

# complete the strings
TOTSCORES = np.zeros(nmystrings)
for im in range(len(mylines)):
    # im = 0
    s0 = mylines[im]
    print(s0)
    ls = len(s0)
    OPENED = []
    for il, ch in enumerate(s0):
        if ch in OPEN:
            OPENED.append(ch)
        elif ch in CLOS and ch == flipp(OPENED[-1]):
            rem = OPENED.pop()
    print(OPENED)
    # REV_OPENED = OPENED.reverse()
    ADDED = []
    nopened = len(OPENED)
    s1 = s0
    for i in range(nopened):
        add = flipp( OPENED[nopened-i-1])
        # add = flipp(OPENED[i])
        s1 = s1 + add
        ADDED.append(add)
    print(s1)
    print("".join(ADDED))
    TOTSCORES[im] = get_score(ADDED)

# print('part2:: all scores = {} '.format(TOTSCORES))


medianscore = np.median(np.array(TOTSCORES).astype(int))
print('part2:: final score = {} '.format(medianscore))


