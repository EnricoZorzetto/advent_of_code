import numpy as np
import matplotlib.pyplot as plt

file = 'data17.txt'
# file = 'test17.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]
x = [list(xi) for xi in x]
nsteps = 6 # number of steps to simulate


def evolve_cell(myval, nuan):
    # evolve CELL myval, with nuan (NUMBER OF ACTIVE NEIGHBOURS)
    if myval == True:
        if nuan in [2,3]:
            nextval = True
        else:
            nextval = False
    else:
        if nuan == 3:
            nextval = True
        else:
            nextval = False
    return nextval


def countneigh(Domain0, i, j, k):
    # count number of neighbours, and check whether cell is alive
    localdom = Domain0[i-1:i+2, j-1:j+2, k-1:k+2]
    alive = Domain0[i, j, k] # whether current cell is alive or dead
    nuan = np.sum(localdom) - alive # number of alive neighbours
    return nuan, alive


def countneigh_4D(Domain0, i, j, k, l):
    # count number of neighbours, and check whether cell is alive
    localdom = Domain0[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2]
    alive = Domain0[i, j, k, l] # whether current cell is alive or dead
    nuan = np.sum(localdom) - alive # number of alive neighbours
    return nuan, alive


def evolve_dom(mat):
    newmat = np.zeros(mat.shape, dtype = bool)
    for i in range(newmat.shape[0]):
        for j in range(newmat.shape[1]):
            for k in range(newmat.shape[2]):
                nuan, alive = countneigh(mat, i, j, k)
                newmat[i, j, k] = evolve_cell(alive, nuan)
    return newmat


def evolve_dom_4D(mat):
    newmat = np.zeros(mat.shape, dtype = bool)
    for i in range(newmat.shape[0]):
        for j in range(newmat.shape[1]):
            for k in range(newmat.shape[2]):
                for l in range(newmat.shape[3]):
                    nuan, alive = countneigh_4D(mat, i, j, k, l)
                    newmat[i, j, k, l] = evolve_cell(alive, nuan)
    return newmat


def init_domain(x, domain_offset = 10):
    nrows0 = len(x)
    ncols0 = len(x[0])
    Domain0 = np.zeros((domain_offset + nrows0 + domain_offset,
                        domain_offset + ncols0 + domain_offset,
                        domain_offset + 1 + domain_offset), dtype = bool)
    print('-------------------------------------------------------------------')
    print('3D Domain shape is = {}'.format(Domain0.shape))
    for i in range(nrows0):
        for j in range(ncols0):
            if x[i][j] == '#':
                Domain0[domain_offset+i, domain_offset+j, domain_offset] = 1
    return Domain0


def init_domain_4D(x, domain_offset = 10):
    nrows0 = len(x)
    ncols0 = len(x[0])
    Domain0 = np.zeros((domain_offset + nrows0 + domain_offset,
                        domain_offset + ncols0 + domain_offset,
                        domain_offset + 1 + domain_offset,
                        domain_offset + 1 + domain_offset), dtype = bool)
    print('-------------------------------------------------------------------')
    print('4D Domain shape is = {}'.format(Domain0.shape))
    for i in range(nrows0):
        for j in range(ncols0):
            if x[i][j] == '#':
                Domain0[domain_offset+i, domain_offset+j,
                        domain_offset, domain_offset] = 1
    return Domain0


# EVOLVE 3D domain
Domain0 = init_domain(x, domain_offset=nsteps + 5)
OLDDOM = Domain0
print('----------------------------------------------------------------------')
print('Inital number of steps in 4D domain is = {}'.format(np.sum(Domain0)))
print('----------------------------------------------------------------------')
for i in range(nsteps):
    NEWDOM = evolve_dom(OLDDOM)
    OLDDOM = NEWDOM.copy()
    # print(i)
    print('Number of cubes after {} steps in 3D domain = {}'.format(i+1,
                                  np.sum(NEWDOM)))
#


plot = False
if plot:
    localdom = NEWDOM[:, :, nsteps+2]
    plt.figure()
    plt.imshow(localdom)
    plt.show()



# EVOLVE 4D domain
Domain0_4D = init_domain_4D(x, domain_offset=nsteps + 5)
OLDDOM = Domain0_4D
print('----------------------------------------------------------------------')
print('Inital number of steps in 4D domain is = {}'.format(np.sum(Domain0_4D)))
print('----------------------------------------------------------------------')
for i in range(nsteps):
    NEWDOM = evolve_dom_4D(OLDDOM)
    OLDDOM = NEWDOM.copy()
    # print(i)
    # print(np.sum(NEWDOM))
    print('Number of cubes after {} steps in 4D domain = {}'.format(i+1,
                                                        np.sum(NEWDOM)))
