import numpy as np
import matplotlib.pyplot as plt
import re


inputfile = 'test_data19.txt'
# inputfile = 'data19.txt'

# read data
with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

scanners = []
pos = []

for li in lines:
    if li[:3] == '---':
        # print(li)
        lin = int(li.split(' ')[2])
        scanners.append(lin)
        pos.append([])
    elif li == '':
        pass
    else:
        print(li)
        lis = [int(x) for x in li.split(',')]
        # lis = [x for x in li.split(',')]
        pos[-1].append(lis)
####################################################################


# tilesize = 1000
# arr1 = np.zeros((tilesize, tilesize, tilesize))



