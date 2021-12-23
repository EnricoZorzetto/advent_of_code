import numpy as np
import matplotlib.pyplot as plt
import re


inputfile = 'test_data19.txt'
# inputfile = 'test_data19_2d.txt'
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
        # print(li)
        # lis = np.array( [int(x) for x in li.split(',')] )
        lis = [x for x in li.split(',')]
        pos[-1].append(lis)

pos = [np.array(x).astype(int) for x in pos]
####################################################################

# len(pos) # ONE FOR EACH SCANNER
# len(pos[0]) # ONE FOR EACH DETECTED BEACON
# len(pos[0][0]) # ONE FOR EACH X, Y, Z
# pos[0][0] # ONE FOR EACH X, Y, Z
#
# pos

# X1 = A * X0
rotation_lib = [
    np.array([[1, 0, 0], [0, 1, 0],   [0, 0, 1]]), ## AROUND Z UP
    np.array([[0, 1, 0], [-1, 0, 0],   [0, 0, 1]]),
    np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
    np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),

    np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]]), # AROUND Z DOWN
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]]),
    np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
    np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1]]),

    np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]),  # AROUND X UP
    np.array([[0, 0, 1], [-1, 0, 0], [0, -1, 0]]),
    np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]]),
    np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]),

    np.array([[0, 0, -1], [0, -1, 0], [-1, 0, 0]]),  # AROUND X DOWN
    np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]]),
    np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]]),
    np.array([[0, 0, -1], [-1, 0, 0], [0, 1, 0]]),

    np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]]),  # AROUND Y UP
    np.array([[0, 1, 0], [0, 0, 1],  [1, 0, 0]]),
    np.array([[-1, 0, 0], [0, 0, 1],  [0, 1, 0]]),
    np.array([[0, -1, 0], [0, 0, 1], [-1, 0, 0]]),

    np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]),  # AROUND Y DOWN
    np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]]),
    np.array([[-1, 0, 0], [0, 0, -1], [0, -1, 0]]),
    np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])

]

np.linalg.inv(rotation_lib[1])


def rotate(V, nr=0):
    # nr -> a number between 0 and 23
    A = rotation_lib[nr]
    # A = np.linalg.inv( rotation_lib[nr])
    return np.dot(V, A)


# FOR EACH SCANNER SAVE ROTATION AND TRANSLATION WITH RESPECT TO SCANNER 0


def compare_scanners(be0, be1_unr, TOTB):

    for kr in range(nrots): # LOOP ON ROTATIONS
        # print('kr = {}'.format(kr))

        if be0.shape[1] == 3:
            be1 = rotate(be1_unr, nr=kr)
        else:
            be1 = be1_unr

        nb0 = be0.shape[0] # number of beacons in the range of scanner 0
        nb1 = be1.shape[0] # number of beacons in the range of scanner 1
        for it in range(nb0):
            for jt in range(nb1):
                rbe0 = be0 - be0[it] # subtract the first row = relative positions
                rbe1 = be1 - be1[jt] # subtract the first row = relative positions

                if be0.shape[1] == 3:
                    min_ncontacts = 12
                else:
                    min_ncontacts = 3

                ncontacts = 0
                CONTACTS = np.zeros(nb1).astype(bool)
                for j in range(nb1):
                    if any((rbe1[j] == x).all() for x in rbe0):
                        ncontacts += 1
                        CONTACTS[j] = True

                # for i in range(nb0):
                #     for j in range(nb1):
                #         if np.sum(rbe0[i] == rbe1[j]) == np.size(rbe0[i]): # True, True, True
                #             ncontacts += 1

                # if ncontacts > 1:
                #     print("kr = {}; ncontacts = {}".format(kr, ncontacts))
                if ncontacts >= min_ncontacts:
                    P0 = be0[it] # these two are the same point!
                    P1 = be1[jt] # these two are the same point!
                    # EXPRESS DIFFERENCES IN COORDS:
                    DP = P0 - P1
                    # print('pos of new scanner in 0 frame = {}'.format(DP))
                    # DS = DP + P0 + P1
                    # print('Coordinate shift = {}'.format(DP)) # POS OF Scan1 wrt Scan0
                    # print('Coordinate shift = {}'.format(DS)) # POS OF Scan1 wrt Scan0
                    tbe1 = be1 + DP  # transform all beacons 1 in frame of reference 0::
                    # ORIG = []
                    for ir in range(nb1): # loop on rows
                        if CONTACTS[ir]:
                            pass
                            # print('overlap, coord #0 : {}'.format(tbe1[ir]))
                            # print('overlap, coord #1 : {}'.format(be1_unr[ir]))
                        if tbe1[ir] not in TOTB:
                            # print('adding new point to total #1 : {}'.format(be1_unr[ir]))
                            # print('TOTB: {}'.format( TOTB.shape ))
                            TOTB = np.append(TOTB, [tbe1[ir]], axis=0)
                            # ORIG = np.append(ORIG, be1[ir], axis=0)

                    return TOTB
    return TOTB




nrots = len(rotation_lib)
nscanners = len(pos)
nbeacons = [len(pos[i]) for i in range(nscanners)]
# print(nscanners, nbeacons)

sc0 = scanners[0]
sc1 = scanners[1]
be0 = pos[0]
be1 = pos[1]


# SAVE IN THE FRAME OF REF OF SCANNER 0
SCANNERS_WRT0 = []
BEACONS_WRT0 = pos[0].copy()


# BEACONS_WRT0 = np.append(BEACONS_WRT0, [[1, 2, 3]], axis=0)


# nbe0 = len(be0)
# nbe1 = len(be1)

# TN = compare_scanners(be0, be1, BE0)
# print(TN)
# print(TN.shape)

# TN = compare_scanners(be0, be1, BE0)
# compare_scanners(be0, be1)
BE0 = np.array(pos[0])
TOTB = BE0.copy()
initsize = 0
finalsize = TOTB.shape[0]
while finalsize > initsize:
    print("initsize = {}, finalsize = {}".format(initsize, finalsize))
    initsize = TOTB.shape[0]
    for i in range(nscanners):
        # for j in range(nscanners):
        print('iter = {}, new size = {}'.format(i, TOTB.shape[0]))
        # mybe0 = pos[0]
        mybe0 = TOTB
        mybe1 = pos[i]
        # TNNEW = compare_scanners(mybe0, mybe1, TN)
        TOTB = compare_scanners(mybe0, mybe1, TOTB)
    finalsize = TOTB.shape[0]

        # TN = TNNEW.copy()

# print( BEACONS_WRT0)

# total number of beacons:
# print(len(BEACONS_WRT0))

            # get those in both tbe1 and be0, and those in only one of them



        # IF more than one overlap: for now keep the first of them
        # if


# be0
# V = np.array([   7,  -33,  -71])
#
# print( any((V == x).all() for x in be0) )



# A = rbe0[i]
# B = rbe0[i]
# A == B


