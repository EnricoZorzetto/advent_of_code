import numpy as np
import matplotlib.pyplot as plt
import re


def read_data(inputfile):
    with open(inputfile) as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    scanners = []
    pos = []
    for li in lines:
        if li[:3] == '---':
            lin = int(li.split(' ')[2])
            scanners.append(lin)
            pos.append([])
        elif li == '':
            pass
        else:
            lis = [x for x in li.split(',')]
            pos[-1].append(lis)
    pos = [np.array(x).astype(int) for x in pos]
    return pos, scanners


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


def rotate(V, nr=0):
    # nr -> a number between 0 and 23
    A = rotation_lib[nr]
    return np.dot(V, A)


def inv_rotate(V, nr=0):
    # nr -> a number between 0 and 23
    A = np.linalg.inv( rotation_lib[nr])
    return np.dot(V, A)


def compare_scanners(be0, be1_unr):
    # FOR EACH SCANNER SAVE ROTATION AND TRANSLATION WITH RESPECT TO SCANNER 0
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
                    transl = P0 - P1
                    # print('pos of new scanner in 0 frame = {}'.format(DP))
                    # DS = DP + P0 + P1
                    # print('Coordinate shift = {}'.format(DP)) # POS OF Scan1 wrt Scan0
                    # print('Coordinate shift = {}'.format(DS)) # POS OF Scan1 wrt Scan0
                    tbe1 = be1 + transl  # transform all beacons 1 in frame of reference 0::
                    # ORIG = []
                    OVERL = []
                    for ir in range(nb1): # loop on rows
                        if CONTACTS[ir]:
                            OVERL.append(be1_unr[ir])
                            # pass
                            # print('overlap, coord #0 : {}'.format(tbe1[ir]))
                            # print('overlap, coord #1 : {}'.format(be1_unr[ir]))
                        # if tbe1[ir] not in OVERL:
                            # print('adding new point to total #1 : {}'.format(be1_unr[ir]))
                            # print('TOTB: {}'.format( TOTB.shape ))
                            # OVERL = np.append(OVERL, [be1_unr[ir]], axis=0)
                            # ORIG = np.append(ORIG, be1[ir], axis=0)


                    # JUST RETURN SCANNER AND BEACONS POSITIONS (1) IN THE FRAME OF REFERENCE (0)
                    enough_overlap = True
                    rot_ind = kr
                    return enough_overlap, tbe1, transl, rot_ind, OVERL
    enough_overlap = False
    return enough_overlap, None, None, None, None



inputfile = 'test_data19.txt'
# inputfile = 'test_data19_2d.txt'
# inputfile = 'data19.txt'
pos, scanners = read_data(inputfile)

# len(pos) # ONE FOR EACH SCANNER
# len(pos[0]) # ONE FOR EACH DETECTED BEACON
# len(pos[0][0]) # ONE FOR EACH X, Y, Z
# pos[0][0] # ONE FOR EACH X, Y, Z

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


mybe0 = pos[0]
mybe1 = pos[1]

# scanners
TRANSL = [[[] for j in scanners] for i in scanners] # TRANSL [i][j]
# ROTIND = [[[] for j in scanners] for i in scanners] # TRANSL [i][j]
ROTIND = np.zeros((nscanners, nscanners))
HAS_OVERLAP = np.zeros((nscanners, nscanners)).astype(bool)
OVERL_ALL = [[[] for j in scanners] for i in scanners] # TRANSL [i][j]


# SCAN_POS = [[] for x in range(nscanners)]
# BEAC_POS = [[] for x in range(nscanners)]


# has_overlap, beac, relpos, rot_ind, OVERL = compare_scanners(pos[0], pos[1])
# OVERL1 = np.array([list(ove) for ove in OVERL])
# OVERL0 = rotate(OVERL1, nr = int(ROTIND[0][1])) + TRANSL[0][1]
# print(OVERL0.shape)
# print(OVERL0[0], OVERL1[0])
#
#
# has_overlap1, beac1, relpos1, rot_ind1, OVERL3 = compare_scanners(pos[1], pos[4])
# relpos2 = rotate(relpos1, nr = int(ROTIND[0][1])) + TRANSL[0][1]
# OVERL3 = rotate( rotate(OVERL3, nr = int(ROTIND[1][4])),  nr = int(ROTIND[0][1])) + relpos2
# print(OVERL3)
# ############## OK UNTIL HERE!!!! #########


for i in range(nscanners):
    print(i)
    for j in range(nscanners):
        mybe0 = pos[i]
        mybe1 = pos[j]
        has_overlap, beac, relpos, rot_ind, OVERL = compare_scanners(mybe0, mybe1)
        if has_overlap:
            HAS_OVERLAP[i,j] = True
            TRANSL[i][j] = relpos
            ROTIND[i, j] = rot_ind
            OVERL_ALL[i][j] = OVERL

            # FOR[j] = i # CONVERTED j-TH SCANNER TO i-TH FRAME OF REFERENCE
            # SCAN_POS[j] = relpos
            # BEAC_POS[j] = beac


FOR = [x for x in range(nscanners)] # current frome of reference of each
BEAC_POS = [a.copy() for a in pos]
OLD_POS = [a.copy() for a in pos]
# OVERL_ALL_0 = [a.copy() for a in OVERL_ALL]
# for i in range(nscanners):
while np.sum(FOR)>0:
    for i in range(nscanners-1):
        iinv = nscanners-i-1 # start from the end
        print(iinv)
        # print("current frame of reference::", FOR[iinv])
        if FOR[iinv] >0:
            j = FOR[iinv]
        # for j in range(nscanners):
        #     if FOR[j] == iinv and FOR[j] > 0:
            # print('must reduce to first nonzero')
            fullrow = np.where(HAS_OVERLAP[:,j])[0]
            # fullrow = np.where( np.logical_not(np.isnan(ROTIND[:,iinv])) )[0]
            firstrow = fullrow[0]
            if firstrow == j:
                firstrow = fullrow[1]

            print('j = {}, firstrow = {}'.format(j, firstrow))

            # print('firstrow = {}'.format(firstrow))
            # TRANSFORM BEACONS POS
            # TRANSFORM SCANNER POS
            BEAC_POS[iinv] = rotate( BEAC_POS[iinv], nr = int(ROTIND[firstrow][j]) ) + TRANSL[firstrow][j]
            # OVERL_ALL_0[iinv] = rotate( OVERL_ALL[iinv], nr = int(ROTIND[firstrow][iinv]) ) + TRANSL[firstrow][iinv]
            # OVERL3 = rotate( rotate(OVERL3, nr = int(ROTIND[1][4])),  nr = int(ROTIND[0][1])) + relpos2
            # BEAC_POS[iinv] = rotate( OLD_POS[iinv], nr = int(ROTIND[firstrow][iinv]) ).copy() + TRANSL[firstrow][iinv]
            FOR[iinv] = firstrow
        print('FORs = {}'.format(FOR))
    # OLD_POS = [a.copy() for a in BEAC_POS]

# BEAC_POS[2] = rotate(BEAC_POS[2], nr=int(ROTIND[1][4])) + TRANSL[1][4]
# BEAC_POS[2] = rotate(BEAC_POS[2], nr=int(ROTIND[0][1])) + TRANSL[0][1]

# OLD_POS[1][0,1] = 999

print(BEAC_POS[1][0,:])
# print(OLD_POS[1][0,:])
print(pos[1][0,:])


BEAC_POS[4]

# BEAC_POS = [BEAC_POS[i] for i in range(len(BEAC_POS)) if  i != 2]

len(BEAC_POS)
BEAC_POS[0].shape

BP = np.vstack(BEAC_POS).astype(int)
print(BP.shape)

FINAL = []
count = 0
for ir in range(BP.shape[0]):
    # if BP[ir,:] not in FINAL:
    if any((BP[ir,:] == x).all() for x in FINAL):
        pass
    else:
        count +=1
        FINAL.append(BP[ir,:])
print(count)
print(len(FINAL))



# now transform all scanners in frame of reference 0
# for i in range(nscanners):

# transf beacons back in FOR 1:: TRANSL 0 -> 1
# beac_1 = inv_rotate( beac - relpos, nr = rot_ind) # INVERSE TRANSFORM ( 0 -> 1 )
# beac_0 = rotate( beac_1, nr = rot_ind) + relpos # DIRECT TRANSFORM (1 -> 0 )
# assert np.allclose( beac_0, beac )
#
#
# print(has_overlap)
# print(beac.shape)
# print(relpos)

# while finalsize > initsize:
#     print("initsize = {}, finalsize = {}".format(initsize, finalsize))
#     initsize = TOTB.shape[0]
#     for i in range(nscanners):
#         # for j in range(nscanners):
#         print('iter = {}, new size = {}'.format(i, TOTB.shape[0]))
#         # mybe0 = pos[0]
#         mybe0 = TOTB
#         mybe1 = pos[i]
#         # TNNEW = compare_scanners(mybe0, mybe1, TN)
#         TOTB = compare_scanners(mybe0, mybe1, TOTB)
#     finalsize = TOTB.shape[0]

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


