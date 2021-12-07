# FISHES
import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# inputfile = 'test_data7.txt'
inputfile = 'data7.txt'

# read data
with open(inputfile) as file:
    # lines = [line.rstrip('\n').split() for line in file.readlines() if line.strip()]
    lines = [line.rstrip('\n').split(',') for line in file.readlines() if line.strip()][0]
POS =  np.array( [int(i) for i in lines] )

np.mean(POS)
minx = np.min(POS)
maxx = np.max(POS)
xi = np.arange(minx, maxx)
nx = np.size(xi)

totd = np.zeros(nx)
totd2 = np.zeros(nx)

ncrabs = np.size(POS)
for i in range(nx):
    print(i)
    myxi = xi[i]
    dists = np.abs( POS - myxi )
    dists2 = np.zeros(ncrabs)
    for k in range(ncrabs):
        dists2[k] = np.sum( np.arange(1, dists[k]+1))
    totd[i] = np.sum(dists)
    totd2[i] = np.sum(dists2)

    # dists = np.zeros(ncrabs)
    # for j in range(ncrabs):

# plt.figure()
# plt.plot(xi, totd, 'o')
# plt.show()

bestpos = np.argmin(totd)
bp_totd = totd[bestpos]
bestpos2 = np.argmin(totd2)
bp_totd2 = totd2[bestpos2]
print('part1:: position with minimum distance is = {}, total dist = {}'.format(bestpos, bp_totd))
print('part2:: position with minimum distance is = {}, total dist = {}'.format(bestpos2, bp_totd2))



