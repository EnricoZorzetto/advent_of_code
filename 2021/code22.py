import numpy as np
import matplotlib.pyplot as plt
import re

inputfile = 'test_data22c.txt'
# inputfile = 'data22.txt'

with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

move = [line.split(" ")[0] for line in lines]
nmoves = len(move)
x0 = np.array( [re.split(r"=|,|\..", line)[1] for line in lines] ).astype(int)
x1 = np.array( [re.split(r"=|,|\..", line)[2] for line in lines] ).astype(int)
y0 = np.array( [re.split(r"=|,|\..", line)[4] for line in lines] ).astype(int)
y1 = np.array( [re.split(r"=|,|\..", line)[5] for line in lines] ).astype(int)
z0 = np.array( [re.split(r"=|,|\..", line)[7] for line in lines] ).astype(int)
z1 = np.array( [re.split(r"=|,|\..", line)[8] for line in lines] ).astype(int)

ncon = 0

XON = []

# for im in range(nmoves):
for im in range(nmoves):


    # FIRST APPEND NEW INTERVAL
    # XON.append( [x0[im], x1[im]] )
    newint = [x0[im], x1[im]]
    XON_NEW = [a for a in XON]
    # if move == 'ON':
    #     for i in range(ninterv):

    # THEN RESOLVE
    # resolved_all = False
    # while not resolved_all:
    #     already_found_overlap = False
    for iii, int in enumerate(XON):        # any overlap
        if x0[im] <= int[1] and x1[im] >= int[0] and not already_found_overlap:
            print('found overlap, iii = {}'.format(iii))
            print(x0[im], int[0], x1[im], int[1])
            newint = [min(x0[im], int[0]), max(x1[im], int[1])]
            _ = XON_NEW.pop(iii)
            already_found_overlap = True

        elif x0[im] < int[0] or x1[im] > int[1]: # no overlap
            print('no overlap, iii = {}'.format(iii))
            pass
        # if not already_found_overlap:
        #     resolved_all = True

    XON_NEW.append(newint)
    print('new int = ({}, {})'.format(x0[im], x1[im]))
    print('new int resolved = ({}, {})'.format(newint[0], newint[1]))
    print('XON_NEW = {}'.format(XON_NEW))
    XON = [a for a in XON_NEW]




    # ncon = np.sum(cube)
    # print('step {}, {} cubes on'.format(im, ncon))



# assert ncon == 2758514936282235
