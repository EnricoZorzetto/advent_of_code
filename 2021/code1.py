import os
import pandas as pd
import numpy as np

d = np.loadtxt("data1.txt")
# d = np.loadtxt("test_data1.txt")
# print(len(d))



# count the number of steps with increasing slope
d2 = d[1:]
d1 = d[:-1]

dd = d2 - d1
npos = np.size(dd[dd>0])
print('part1: the number of increasing steps is = {}'.format(npos))

# now do the same with the number of triplets
npos2 = 0
n = np.size(d)
for i in range(n-3):
    A = np.sum( d[i:i+3] )
    B = np.sum( d[i+1:i+4] )
    # print(A, B)
    if B > A:
        npos2 +=1

print('part2: the number of increasing steps is = {}'.format(npos2))

