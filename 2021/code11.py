import numpy as np
import matplotlib.pyplot as plt


def read_data(inputfile):
    with open(inputfile) as file:
        map = np.array( [[char for char in line.rstrip('\n')]
                    for line in file.readlines()] ).astype(int)
    return map


def get_neighbours(map, i, j):
    ny, nx = np.shape(map)
    YN = []; XN = []
    if i > 0:
        YN.append(i-1); XN.append(j)
    if i < ny-1:
        YN.append(i+1); XN.append(j)
    if j > 0:
        YN.append(i); XN.append(j-1)
    if j < nx-1:
        YN.append(i); XN.append(j+1)
    if j > 0 and i > 0:
        YN.append(i-1); XN.append(j-1)
    if j < nx-1 and i > 0:
        YN.append(i-1); XN.append(j+1)
    if j > 0 and i < ny-1:
        YN.append(i+1); XN.append(j-1)
    if j < nx-1 and i< ny-1:
        YN.append(i+1); XN.append(j+1)
    nneighb = len(YN)
    assert nneighb > 2
    assert nneighb < 9
    return nneighb, np.array(YN), np.array(XN)


def update_map(newmap):
    ny, nx = np.shape(newmap)
    current_flashes = 0
    # first, add 1 to all
    newmap += 1
    # then, resolve the flashes
    has_flashed = np.zeros((ny,nx)).astype(bool)
    YTF, XTF = np.where( np.logical_and( newmap > 9, np.logical_not(has_flashed)))
    ntf = len(YTF)
    while ntf > 0: # while there are unresolved flashes
        for nti in range(ntf):
            i = YTF[nti]; j = XTF[nti]
            nneighb, YN, XN = get_neighbours(newmap, i, j)
            newmap[YN,XN] += 1
            has_flashed[i,j] = True
            current_flashes += 1
        YTF, XTF = np.where( np.logical_and( newmap > 9, np.logical_not(has_flashed)))
        ntf = len(YTF)
    # third step: set to zero
    newmap[newmap > 9] = 0
    return newmap, current_flashes


def main():
    # inputfile = 'test_data11.txt'
    inputfile = 'data11.txt'
    map = read_data(inputfile)
    # PART 1
    newmap = map.copy()
    nsteps = 100
    CURRENT_FLASHES = np.zeros(nsteps).astype(int)
    for st in range(nsteps):
        newmap, CURRENT_FLASHES[st] = update_map(newmap)
        # print('step # {}: current # of flashes = {}'.format(st + 1, CURRENT_FLASHES[st]))
    print('part 1: # flashes after {} steps = {}'.format(nsteps, np.sum(CURRENT_FLASHES)))
    # PART 2
    newmap = map.copy()
    cflashes = 0; mystep = 0
    while cflashes < np.size(map):
        mystep += 1
        newmap, cflashes = update_map(newmap)
        # print('step # {}: current # of flashes = {}'.format(mystep, cflashes))
    print('part 2: # flashes = {} at step # = {}'.format(cflashes, mystep))


if __name__ == '__main__':
    main()


