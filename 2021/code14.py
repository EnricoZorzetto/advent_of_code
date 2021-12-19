import numpy as np
import matplotlib.pyplot as plt



def read_data(inputfile):
    with open(inputfile) as file:
        # lines = [line.rstrip('\n').split() for line in file.readlines() if line.strip()]
        lines = [line.rstrip('\n').split(',') for line in file.readlines() if line.strip()]
        # points = [l.split(' ')[-1].split('->') for l in lines if '->' in l[0]]
    points = [l[0].split(" -> ") for l in lines if '->' in l[0]]
    polymer = [l[0] for l in lines if not '->' in l[0]]
    assert len(polymer) == 1; polymer = polymer[0]
    # polymer = [p for p in polymer]
    polymer = list(polymer)
    # get array dimensions
    inivals = [p[0] for p in points] # first value x increases to the right
    endvals = [p[1] for p in points] # second value y increases to the bottom
    lookup = {ini:end for ini, end in zip(inivals, endvals)}
    return polymer, lookup


def update_poly(oldpoly, lookup):
    oldlen = np.size(oldpoly)
    newlen = oldlen * 2 -1
    newpoly = np.zeros(newlen).astype("<U1")
    for i in range(newlen):
        oldi = i // 2
        # print(oldi)
        if i % 2 == 0: newpoly[i] = oldpoly[oldi]
        else:
            mystr = oldpoly[oldi] + oldpoly[oldi+1]
            # print(mystr)
            # print("{} -> {}".format(mystr, lookup[mystr]))
            newpoly[i] = lookup[mystr]
    # print(oldpoly)
    # print(newpoly)
    return newpoly


def compute_difference(newpoly):
    uniques = np.unique(newpoly)
    nuniques = np.size(uniques)
    freqs = np.zeros(nuniques).astype(int)
    for fr in range(nuniques):
        freqs[fr] = np.size(newpoly[newpoly == uniques[fr]])
    maxind = np.argmax(freqs)
    minind = np.argmin(freqs)
    diffv = freqs[maxind] - freqs[minind]
    return diffv


def slow_update_part1(polymer, lookup, nsteps=10):
    # nsteps = 10
    oldpoly = np.array(polymer)
    for step in range(nsteps):
        newpoly = update_poly(oldpoly, lookup)
        oldpoly = newpoly.copy()
        # print('step {}'.format(step))
    # print(newpoly)
    # print(len(newpoly))
    diffv = compute_difference(newpoly)
    print('part 1:: after {} steps,  diffv = {}'.format(nsteps, diffv))


def fast_update_part2(polymer, lookup, nsteps=40):
    inivals = list(lookup.keys())
    endvals = list(lookup.values())
    COUP_COUNTS = {ini : 0 for ini in inivals}
    LETTER_COUNTS = {end : 0 for end in endvals}

    # add initial polymer
    for i, pp in enumerate(polymer):
        # print(i, pp)
        LETTER_COUNTS[pp] += 1
        if i > 0:
            couple = polymer[i-1]+polymer[i]
            COUP_COUNTS[couple] += 1
    NEW_COUP_COUNTS = COUP_COUNTS.copy()
    for step in range(nsteps):
        for coup in COUP_COUNTS.keys():
            myletter = lookup[coup]
            LETTER_COUNTS[myletter] += COUP_COUNTS[coup]
            first_c = coup[0] + myletter
            last_c = myletter + coup[1]
            NEW_COUP_COUNTS[first_c] += COUP_COUNTS[coup]
            NEW_COUP_COUNTS[last_c] += COUP_COUNTS[coup]
            NEW_COUP_COUNTS[coup] -= COUP_COUNTS[coup]
        COUP_COUNTS = NEW_COUP_COUNTS.copy()
    diffv = np.max(list(LETTER_COUNTS.values())) - np.min(list(LETTER_COUNTS.values()))
    print('part 2 :: differnce after {} steps = {}'.format(nsteps, diffv))


if __name__ == '__main__':

    # inputfile = 'test_data14.txt'
    inputfile = 'data14.txt'
    polymer, lookup = read_data(inputfile)

    slow_update_part1(polymer, lookup, nsteps=10)
    fast_update_part2(polymer, lookup, nsteps=40)


