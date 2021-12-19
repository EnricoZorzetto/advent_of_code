import re
from itertools import product
import numpy as np


def get_vxs(xmin, xmax):
    VX0 = []
    TMX = []
    POSX = []
    TMIN = []
    velocities_x = np.arange(1, xmax + 1)
    for vx0 in velocities_x:
        # print('vx0 = {}'.format(vx0))
        myx = 0
        vx = vx0
        t = 0
        while vx > 0 and myx <= xmax:
            myx += vx
            vx -= 1
            t += 1
            if myx >= xmin and myx <= xmax:
                VX0.append(vx0)
                TMX.append(t)
                POSX.append(myx)
                # now separately save those that go to zero -> any time!!!
                if vx == 0:
                    TMIN.append(t)
                else:
                    TMIN.append(-9999)
            # print("t = {}; x = {}; vx = {}".format(t, myx, vx))
    return np.array(VX0), np.array(TMX), np.array(POSX), np.array(TMIN)


def get_ymax(xmin, xmax, ymin, ymax):
    # cases without time limit:: where the ball stops in x in the box
    # this is the longest time it takes to stay there
    VX0, TMX, POSX, TMIN= get_vxs(xmin,xmax)
    VX0ntl = VX0[TMIN > -1]
    POSXntl = POSX[TMIN > -1]
    TMINntl = TMIN[TMIN > -1]
    TMINmax = np.min(TMINntl)
    # get the maximum of these:
    vy_min = ymin - 1 # too low, this does not enter the box
    vyall = np.arange(vy_min, 1000)
    nvy = np.size(vyall)
    maxima =[]
    vy0valid = []
    for ivy, vy0 in enumerate(vyall):
        mymaxima = 0
        myy = 0
        vy = vy0
        t = 0
        while myy >= ymin:
            myy += vy
            vy -= 1
            t += 1
            if myy > mymaxima: mymaxima = myy
            if t >= TMINmax and myy >= ymin and myy <= ymax:
                # print("t = {}; y = {}; vy = {}".format(t, myy, vy))
                # print('vy0 = {}; meeting in the box!'.format(vy0))
                maxima.append(mymaxima)
                vy0valid.append(vy0)
    # print(vyall)
    # print(maxima)
    mymax = np.argmax(maxima)
    print('part 1 :: the max height is y = {} for vy0 = {}'.format(maxima[mymax], vy0valid[mymax]))


# get the allowed x poistions
def get_number_hits(xmin, xmax, ymin, ymax):
    VX0, TMX, POSX, TMIN = get_vxs(xmin,xmax)
    uVX0 = np.unique(VX0)
    uPOSX = np.unique(POSX)
    uTMX = np.unique(TMX)
    maxt = np.max(uTMX)
    VX0ntl = VX0[TMIN > -1]
    POSXntl = POSX[TMIN > -1]
    TMINntl = TMIN[TMIN > -1]
    nvx = np.size(uVX0)
    VEL = []
    vy_min = ymin - 1  # below is too low, does not enter the box
    vyall = np.arange(vy_min, 1000)
    nvy = np.size(vyall)
    vy0valid = 0
    for ivy, vy0 in enumerate(vyall):
        myy = 0
        vy = vy0
        t = 0
        while myy >= ymin :
            myy += vy
            vy -= 1
            t += 1
            if myy >= ymin and myy <= ymax:
                for telem1, myvx in zip(TMX, VX0):
                    if t == telem1:
                        current_couple = (myvx, vy0)
                        if current_couple not in VEL:
                            VEL.append( current_couple)
                for telem2, myvx in zip(TMINntl, VX0ntl):
                    if t > telem2:
                        current_couple = (myvx, vy0)
                        if current_couple not in VEL:
                            VEL.append(current_couple)
    # print(vy0valid)
    # print(len(VEL))
    print("part 2 :: The number of allowed velocities is = {}".format(len(VEL)))
    return



if __name__ == "__main__":

    # data_string = 'target area: x=20..30, y=-10..-5' # test data
    data_string = 'target area: x=241..275, y=-75..-49' # real data
    data = re.split(r"=|\.\.|,", data_string)
    xmin = int(data[1]); xmax=int(data[2]); ymin=int(data[4]); ymax=int(data[5])
    # print(data)
    # print(xmin, xmax, ymin, ymax)
    # PART 1
    get_ymax(xmin, xmax, ymin, ymax)
    # PART 2
    get_number_hits(xmin, xmax, ymin, ymax)



