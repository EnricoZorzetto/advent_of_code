
import os
import numpy as np


# inputfile = "test_data1.txt"
inputfile = "data1.txt"

ev = [[]]
with open(inputfile) as f:
    mylist = f.read().splitlines() 

for l in mylist:
    if (l==''):
        ev.append([])
    else:
        ev[-1].append(int(l))

sums = np.sort([np.sum(np.array(i)) for i in ev])
print('Part 1 :: The largest value is = {}'.format(sums[-1]))
print('Part 2 :: The 3 largest values are = {}; sum = {}'.format(sums[-3:], np.sum(sums[-3:])))


