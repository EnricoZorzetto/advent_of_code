import os
import pandas as pd
import numpy as np

# inputfile = 'test_data2.txt'
inputfile = 'data2.txt'

df = pd.read_csv(inputfile, sep='\s+', header=None, names=("move", "size"))

# print(np.unique(df["move"]))
fwd = np.sum( df[ df["move"] == 'forward']['size'].values )
up =  np.sum( df[ df["move"] == 'up']['size'].values )
dn =  np.sum( df[ df["move"] == 'down']['size'].values )

molt = fwd*(dn-up)
print("part1:: res is = {}".format(molt))

# part 2
move = df['move'].values
size = df['size'].values
n = np.size(move)
aim = 0

DISTX = 0
DISTY = 0
for i in range(n):
    if move[i] == 'down': aim += size[i]
    if move[i] == 'up': aim -= size[i]
    if move[i] == 'forward':
        DISTX += size[i]
        DISTY += size[i]*aim
molt2 = DISTX * DISTY
print("part2:: res is = {}".format(molt2))







