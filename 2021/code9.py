import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# inputfile = 'test_data9.txt'
inputfile = 'data9.txt'

def splits(word):
    return [char for char in word]

with open(inputfile) as file:
    lines = [splits(line.rstrip('\n')) for line in file.readlines()]
map = np.array(lines).astype(int)


def get_neighb(map, i, j):
    nx, ny = np.shape(map)
    vneighb = []
    ineighb = []
    jneighb = []
    if i > 0:
        npo = map[i - 1, j]
        vneighb.append(npo)
        ineighb.append(i-1)
        jneighb.append(j)
    if i < nx - 1:
        sp = map[i + 1, j]
        vneighb.append(sp)
        ineighb.append(i + 1)
        jneighb.append(j)
    if j > 0:
        wp = map[i, j - 1]
        vneighb.append(wp)
        ineighb.append(i)
        jneighb.append(j-1)
    if j < ny - 1:
        ep = map[i, j + 1]
        vneighb.append(ep)
        ineighb.append(i)
        jneighb.append(j+1)
    assert len(vneighb) > 1 # all points have at least 2 neighbours
    return vneighb, ineighb, jneighb


def lowest_neighb(map, i, j):
    vneighb, ineighb, jneighb = get_neighb(map,i,j)
    minpos = np.argmin( np.array(vneighb))
    vmin = vneighb[minpos]
    imin = ineighb[minpos]
    jmin = jneighb[minpos]
    return vmin, imin, jmin


def find_pits(map):
    nx, ny = np.shape(map)
    vpits = []
    ipits = []
    jpits = []
    for i in range(nx):
        for j in range(ny):
            neighb, _, _ = get_neighb(map,i,j)
            min_neighb = min(neighb)
            if map[i,j]<min_neighb:
                vpits.append(map[i,j])
                ipits.append(i)
                jpits.append(j)
    return vpits, ipits, jpits

# DO PART 1
vpits, ipits, jpits = find_pits(map)
risk_levels = [x+1 for x in vpits]
tot_rl = sum(risk_levels)
print("part 1:: the total risk level is = {}".format(tot_rl))

# DO PART 2
nbasins = len(vpits)
BASIN_SIZES = np.zeros(nbasins)
for ib in range(nbasins):
    nx, ny = np.shape(map)
    oldbasin0 = np.zeros((nx,ny)).astype(bool)
    oldbasin0[ipits[ib],jpits[ib]] = True # init current basin from the pit
    # while new points were added to the basin
    OLDPOINTS = [(x,y) for x in range(nx) for y in range(ny) if oldbasin0[x,y]]
    counter = 0
    while len(OLDPOINTS)>0:
        newbasin0 = oldbasin0.copy()
        # get neighbours of current point
        NEWPOINTS = []
        for (ip, jp) in OLDPOINTS:
            vneighb, ineighb, jneighb = get_neighb(map, ip, jp) # get only external neighb????
            for ine, jne in zip(ineighb, jneighb):
                vx, ix, jx = lowest_neighb(map, ine, jne) # get lowest neighb
                # print(vx, ix, jx)
                if oldbasin0[ix,jx] and map[ine,jne] < 9: # if lowest neight point is in the basin
                    if not oldbasin0[ine, jne]: # if the point was not already in the basin
                        newbasin0[ine,jne] = True # add the external neighbour to the basin
                        NEWPOINTS.append((ine, jne))
        # print('NEWPOINTS', NEWPOINTS)
        added_points = np.logical_and(newbasin0, np.logical_not(oldbasin0))
        # update for next iteration:
        oldbasin0 = newbasin0.copy()
        OLDPOINTS = [op for op in NEWPOINTS]
        counter += 1
        # plt.figure()
        # plt.imshow(newbasin0)
        # # plt.imshow(added_points)
        # plt.title('iter = {}'.format(counter))
        # plt.show()
    BASIN_SIZES[ib] = np.sum(newbasin0)

BASIN_SIZES_SORT = np.sort(BASIN_SIZES)
print('part 2:: the product of the largest 3 basin sizes is = {}'.format(np.prod(BASIN_SIZES_SORT[-3:])))




