import numpy as np
import matplotlib.pyplot as plt
import re
import numba as nb
from numba import njit


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

# A = [1,2,3]
# B = rotate(A, nr = 3)
# C = inv_rotate(B, nr = 3)
# print(A, B, C)

# A = np.array([1,2,3])
# B = np.array([1,2,3])
# diff = np.subtract.outer(A, B)
# print(diff)

# @nb.jit(nb.typeof((1.0,1.0))(nb.double),nopython=True)
# def f(a):
#   return a,a

# @nb.jit('Tuple((b1, int64[:], int64))(int64[:,:], int64[:,:])',nopython=True)
# @nb.jit(nb.typeof((Tr, nb.double[:], nb.int32))(nb.double[:], nb.double[:]),nopython=True)
def compare_scanners(be0, be1_unr):
    # FOR EACH SCANNER SAVE ROTATION AND TRANSLATION WITH RESPECT TO SCANNER 0



    transl0 = be0[0] - be1_unr[0]
    nb0 = be0.shape[0]  # number of beacons in the range of scanner 0
    nb1 = be1_unr.shape[0]  # number of beacons in the range of scanner 1
    for kr in range(nrots): # LOOP ON ROTATIONS
        # print('kr = {}'.format(kr))
        be1 = rotate(be1_unr, nr=kr)
        # be1 = rotation_lib[kr]
        # diffx0 = np.subtract.outer(be0[:,0], be0[:,0])
        # diffx1 = np.subtract.outer(be1[:,0], be1[:,0])
        # overlx = diffx0 == diffx1
        #
        # diffy0 = np.subtract.outer(be0[:,1], be0[:,1])
        # diffy1 = np.subtract.outer(be1[:,1], be1[:,1])
        # overly = diffy0 == diffy1
        #
        # diffz0 = np.subtract.outer(be0[:,2], be0[:,2])
        # diffz1 = np.subtract.outer(be1[:,2], be1[:,2])
        # overlz = diffz0 == diffz1
        #
        # overla = overlz & overlx & overly
        # ncontacts = np.sum(overla)

        # print("number of overlaps = {}".format(np.sum(overla)))
        # noverlaps = np.sum(diff0 == diff1)
        min_ncontacts = 12
        for it in range(nb0):
            for jt in range(nb1):
                rbe0 = be0 - be0[it] # subtract the first row = relative positions
                rbe1 = be1 - be1[jt] # subtract the first row = relative positions
                # rdiff = np.sum( np.abs(rbe0 - rbe1), axis=0)
                # ncontacts = rdiff[rdiff  < 1].shape[0]
                ncontacts = 0
                for j in range(nb1):
                    if any((rbe1[j] == x).all() for x in rbe0):
                        ncontacts += 1
                if ncontacts >= min_ncontacts:
                    transl = be0[it] - be1[jt]
                    enough_overlap = True
                    rot_ind = kr
                    return enough_overlap, transl, rot_ind
    enough_overlap = False
    # transl = np.array([0,0,0])
    rot_ind = 0
    return enough_overlap, transl0, rot_ind



# inputfile = 'test_data19.txt'
# inputfile = 'test_data19_2d.txt'
inputfile = 'data19.txt'
pos, scanners = read_data(inputfile)


nrots = len(rotation_lib)
nscanners = len(pos)
nbeacons = [len(pos[i]) for i in range(nscanners)]


# scanners
TRANSL = [[[] for j in scanners] for i in scanners] # TRANSL [i][j]
ROTIND = np.zeros((nscanners, nscanners)).astype(int)
HAS_OVERLAP = np.zeros((nscanners, nscanners)).astype(bool)
# OVERL_ALL = [[[] for j in scanners] for i in scanners] # TRANSL [i][j]


# COMPUTE THE RELATIVE ROTATIONS AND TRANSLAATIONS BETWEEN SCANNERS
for i in range(nscanners):
    for j in range(nscanners):
        print(i,j)
        mybe0 = pos[i]
        mybe1 = pos[j]
        # has_overlap, beac, relpos, rot_ind, OVERL = compare_scanners_old(mybe0, mybe1)
        # resall = compare_scanners(mybe0, mybe1)
        has_overlap, relpos, rot_ind = compare_scanners(mybe0, mybe1)
        if has_overlap:
            HAS_OVERLAP[i,j] = True
            # HAS_OVERLAP[j, i] = True
            TRANSL[i][j] = relpos
            # TRANSL[j][i] = - relpos
            ROTIND[i, j] = rot_ind
            # OVERL_ALL[i][j] = OVERL



FOR = [x for x in range(nscanners)] # current frome of reference of each
BEAC_POS = [a.copy() for a in pos]
OLD_POS = [a.copy() for a in pos]
while np.sum(FOR)>0:
    for i in range(nscanners-1):
        iinv = nscanners-i-1 # start from the end
        # print(iinv)
        if FOR[iinv] >0:
            j = FOR[iinv]
            fullrow = np.where(HAS_OVERLAP[:,j])[0]
            firstrow = fullrow[0]
            if firstrow == j:
                firstrow = fullrow[1]
            print('iinv = {}; j = {}, firstrow = {}'.format(iinv, j, firstrow))
            # if j > firstrow:
            BEAC_POS[iinv] = rotate( BEAC_POS[iinv], nr = int(ROTIND[firstrow][j]) ) + TRANSL[firstrow][j]
            # else:
            #     BEAC_POS[iinv] = inv_rotate(BEAC_POS[iinv], nr=int(ROTIND[j][firstrow])) - TRANSL[j][firstrow]
            FOR[iinv] = firstrow
        print('FORs = {}'.format(FOR))


BP = np.vstack(BEAC_POS).astype(int)
FINAL = []
count = 0
for ir in range(BP.shape[0]):
    if any((BP[ir,:] == x).all() for x in FINAL):
        pass
    else:
        count +=1
        FINAL.append(BP[ir,:])
print(count)
print("part 1 :: the total number of beacons is = {}".format(len(FINAL)))
