import numpy as np
import matplotlib.pyplot as plt
import re

# inputfile = 'test_data22.txt'
# inputfile = 'test_data22b.txt'
inputfile = 'data22.txt'
#
with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

move = [line.split(" ")[0] for line in lines]
nmoves = len(move)
offset = 50
x0 = np.array( [re.split(r"=|,|\..", line)[1] for line in lines] ).astype(int) + offset
x1 = np.array( [re.split(r"=|,|\..", line)[2] for line in lines] ).astype(int) + offset
y0 = np.array( [re.split(r"=|,|\..", line)[4] for line in lines] ).astype(int) + offset
y1 = np.array( [re.split(r"=|,|\..", line)[5] for line in lines] ).astype(int) + offset
z0 = np.array( [re.split(r"=|,|\..", line)[7] for line in lines] ).astype(int) + offset
z1 = np.array( [re.split(r"=|,|\..", line)[8] for line in lines] ).astype(int) + offset

nx = 101
cube = np.zeros((nx, nx, nx)).astype(bool)

for im in range(nmoves):
    print(x0[im], y0[im], z0[im])
    print(x1[im], y1[im], z1[im])
    print(np.shape(cube[x0[im]:x1[im]+1, y0[im]:y1[im]+1, z0[im]:z1[im]+1] ))
    if move[im] == 'on':
         cube[x0[im]:x1[im]+1, y0[im]:y1[im]+1, z0[im]:z1[im]+1] = True
    elif move[im] == 'off':
        cube[x0[im]:x1[im]+1, y0[im]:y1[im]+1, z0[im]:z1[im]+1] = False

    ncon = np.sum(cube)
    print('step {}, {} cubes on'.format(im, ncon))


