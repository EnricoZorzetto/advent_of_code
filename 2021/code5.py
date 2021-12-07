# THERMAL VENTS
import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# inputfile = 'test_data5.txt'
inputfile = 'data5.txt'
do_only_part_1 = False

# read data
with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines() if line.strip()]

# each list, x1, y1, x2, y2
coords = np.array([    re.split(' -> |,', stri) for stri in lines]).astype(int)

ncols = max( np.max(coords[:,0]), np.max(coords[:,2])) + 1
nrows = max( np.max(coords[:,1]), np.max(coords[:,3])) + 1
numvents = np.zeros((nrows, ncols)).astype(int)

nlines = np.shape(coords)[0]
for i in range(nlines):
    print(i)
    mycoords = coords[i,:].copy()
    x1 = mycoords[0]
    y1 = mycoords[1]
    x2 = mycoords[2]
    y2 = mycoords[3]
    if x1 == x2: # vertical line:
        ymin = min(y1, y2)
        ymax = max(y1, y2) +1
        numvents[ymin:ymax, x1] = numvents[ymin:ymax, x1] + 1
    elif y1 == y2:
        xmin = min(x1, x2)
        xmax = max(x1, x2) +1
        numvents[y1, xmin:xmax] = numvents[y1, xmin:xmax] + 1
    else:
        if do_only_part_1:
            pass
        else:
            # part 2: add diagonal lines
            if x2 >= x1:
                X = np.arange(x1, x2 + 1)
            else:
                X = np.arange(x1, x2-1, -1)
            if y2 >= y1:
                Y = np.arange(y1, y2 + 1)
            else:
                Y = np.arange(y1, y2 - 1, -1)
            npoints_y = len(Y)
            npoints_x = len(X)
            assert npoints_y == npoints_x
            for ip in range(npoints_y):
                current_x = X[ip]
                current_y = Y[ip]
                numvents[current_y, current_x] += 1

noverlaps = np.size(numvents[numvents>1]    )
print('number of overlap point is = {}'.format(noverlaps))

plt.figure()
plt.imshow(numvents)
plt.colorbar()
plt.show()


