import numpy as np
import matplotlib.pyplot as plt
import re


def belongs_to_cube(x0c, y0c, z0c, x1c, y1c, z1c, X, Y, Z):
    # belx = X >= min(x1c, x0c) and X <= max(x1c, x0c) - 1
    # bely = Y >= min(y1c, y0c) and Y <= max(y1c, y0c) - 1
    # belz = Z >= min(z1c, z0c) and Z <= max(z1c, z0c) - 1

    belx = X >= min(x1c, x0c) and X <= max(x1c, x0c)
    bely = Y >= min(y1c, y0c) and Y <= max(y1c, y0c)
    belz = Z >= min(z1c, z0c) and Z <= max(z1c, z0c)
    bel = belx and bely and belz
    return bel


def volume_of_cube(x0c, y0c, z0c, x1c, y1c, z1c):
    dx = max(x1c, x0c) - min(x1c, x0c)
    dy = max(y1c, y0c) - min(y1c, y0c)
    dz = max(z1c, z0c) - min(z1c, z0c)
    V = dx * dy * dz
    return V


# def check_pos_vol(x0c, y0c, z0c, x1c, y1c, z1c):
#     return (x1c - x0c > 0) and (y1c - y0c > 0) and (z1c - z0c > 0)

# inputfile = 'test_data22c.txt'
inputfile = 'data22.txt'

with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

move = [line.split(" ")[0] for line in lines]
move = [True if x=='on' else False for x in move]
nmoves = len(move)
# x0 = np.array( [re.split(r"=|,|\..", line)[1] for line in lines] ).astype(int)
# x1 = np.array( [re.split(r"=|,|\..", line)[2] for line in lines] ).astype(int)
# y0 = np.array( [re.split(r"=|,|\..", line)[4] for line in lines] ).astype(int)
# y1 = np.array( [re.split(r"=|,|\..", line)[5] for line in lines] ).astype(int)
# z0 = np.array( [re.split(r"=|,|\..", line)[7] for line in lines] ).astype(int)
# z1 = np.array( [re.split(r"=|,|\..", line)[8] for line in lines] ).astype(int)

# ncon = 0
#
# x0[:2]
# x1[:2]

# XON = []

# SPLIT TWO CUBES

# x0 = np.array([1, 5])
# x1 = np.array([6, 8])
# y0 = np.array([2, 5])
# y1 = np.array([7, 9])
# z0 = np.array([-3, -2])
# z1 = np.array([-6, -8])

# PROBLEM : INCLUDE BOUNDARIES
# BUT I EXCLUDE IN CALC
# x0 = np.array([1, 1])
# x1 = np.array([3, 3])
# y0 = np.array([1, 1])
# y1 = np.array([3,3])
# z0 = np.array([1,1])
# z1 = np.array([3,6])

x0 = np.array([1, 5])
x1 = np.array([3, 8])
y0 = np.array([1, 5])
y1 = np.array([3,8])
z0 = np.array([1,5])
z1 = np.array([3,8])
x1 += 1; y1 += 1; z1 += 1
ncubes = 0
move = np.array([False, True])


# INTERSECT the two cubes and compute
i = 0
j = 1

# inters in x:

# intersx = not (max(x0[i], x1[i]) <  min(x0[j], x1[j] ) or min(x0[i], x1[i]) > max(x0[j], x1[j] ) )
# intersy = not (max(y0[i], y1[i]) <  min(y0[j], y1[j] ) or min(y0[i], y1[i]) > max(y0[j], y1[j] ) )
# intersz = not (max(z1[i], z1[i]) <  min(z0[j], z1[j] ) or min(z0[i], z1[i]) > max(z0[j], z1[j] ) )
intersx = not (max(x0[i], x1[i]) <=  min(x0[j], x1[j] ) or min(x0[i], x1[i]) >= max(x0[j], x1[j] ) )
intersy = not (max(y0[i], y1[i]) <=  min(y0[j], y1[j] ) or min(y0[i], y1[i]) >= max(y0[j], y1[j] ) )
intersz = not (max(z0[i], z1[i]) <=  min(z0[j], z1[j] ) or min(z0[i], z1[i]) >= max(z0[j], z1[j] ) )
# print(intersx, intersy, intersz)
inters = intersx and intersy and intersz
print('Intersection? {}'.format(inters))

# IF NOT INTERS, JUST ADD THE POSITIVE ONE(s) TO THE LIST

# IF INTERS, ADD ALL THE POSITIVE SUB CUBES::

xvals = [ x0[i], x1[i], x0[j], x1[j]]
yvals = [ y0[i], y1[i], y0[j], y1[j]]
zvals = [ z0[i], z1[i], z0[j], z1[j]]
xvals.sort(); yvals.sort(); zvals.sort()
print('xvals = {}'.format(xvals))


x0new = []; x1new = []
y0new = []; y1new = []
z0new = []; z1new = []

# UP TO 9 NEW CUBES
x0new += [ xvals[0], xvals[1], xvals[2], xvals[1], xvals[0], xvals[0], xvals[0], xvals[1], xvals[1],  xvals[2], xvals[1], xvals[1]   , xvals[2], xvals[1], xvals[2]]
x1new += [ xvals[1], xvals[2], xvals[3], xvals[2], xvals[1], xvals[1], xvals[1], xvals[2], xvals[2],  xvals[3], xvals[2], xvals[2]   , xvals[3], xvals[2], xvals[3]]
y0new += [ yvals[0], yvals[1], yvals[2], yvals[0], yvals[1], yvals[0], yvals[1], yvals[1], yvals[0],  yvals[2], yvals[1], yvals[2]  , yvals[1], yvals[2], yvals[1]]
y1new += [ yvals[1], yvals[2], yvals[3], yvals[1], yvals[2], yvals[1], yvals[2], yvals[2], yvals[1],  yvals[3], yvals[2], yvals[3]   , yvals[2], yvals[3], yvals[2]]
z0new += [ zvals[0], zvals[1], zvals[2], zvals[0], zvals[0], zvals[1], zvals[1], zvals[0], zvals[1],  zvals[1], zvals[2], zvals[2]   , zvals[1], zvals[1], zvals[2]]
z1new += [ zvals[1], zvals[2], zvals[3], zvals[1], zvals[1], zvals[2], zvals[2], zvals[1], zvals[2],  zvals[2], zvals[3], zvals[3]   , zvals[2], zvals[2], zvals[3]]

print(x0new)
print(x1new)
print(y0new)
print(y1new)
print(z0new)
print(z1new)

# REMOVE CUBES WITH ZERO DIMENSIONS

# SAVE THOSE BELONGING TO THE SECOND (MOST RECENT) CUBE; THE PREVIOUS WILL HAVE THE OTHER PROPERTY
nnewcubes = len(x0new)
parent_cube = np.zeros(nnewcubes).astype(bool)
cube_type = np.zeros(nnewcubes).astype(bool)
for ic in range(nnewcubes):
    parent_cube[ic] = belongs_to_cube(x0[j], y0[j], z0[j], x1[j], y1[j], z1[j], x0new[ic], y0new[ic], z0new[ic])
# cube_type[np.logical_not(parent_cube)] = move[i] # assign the type of the first cube to the remaining
cube_type[parent_cube] = move[j] # assign the type of the second cube to the 2nd cube component

# KEEP ONLY THE CUBES WHICH ARE NON ZERO VOLUME, ANB HAVE CUBE TYPE 1

has_posvol = np.ones(nnewcubes).astype(bool)
for ic in range(nnewcubes):
    # has_posvol[ic] = cube_type[ic] and check_pos_vol(x0new[ic], y0new[ic], z0new[ic], x1new[ic], y1new[ic], z1new[ic])
    if x0new[ic]==x1new[ic] or y0new[ic]==y1new[ic] or z0new[ic]==z1new[ic]:
        print(x0new[ic], y0new[ic], z0new[ic], x1new[ic], y1new[ic], z1new[ic])
        has_posvol[ic] = False

    # has_posvol[ic] = check_pos_vol(x0new[ic], y0new[ic], z0new[ic], x1new[ic], y1new[ic], z1new[ic])

print('Number of sub-cubes with positive volume: {} out of {}'.format(np.sum(has_posvol), nnewcubes))
print('number of sub-cubes with "on" property: {}'.format(np.sum(cube_type)))


VOLS = np.zeros(nnewcubes)
for ic in range(nnewcubes):
    VOLS[ic] = volume_of_cube(x0new[ic], y0new[ic], z0new[ic], x1new[ic], y1new[ic], z1new[ic])

print('total volume of all sub cubes', np.sum(VOLS))
print('volumes of single sub cubes', VOLS)
print('number of sub-cubes having positive volume', np.sum(has_posvol))
print('number of sub-cubes belonging to cube # 2 is', np.sum(parent_cube))
print('number of sub-cubes belonging to last cube with pos vol is', np.sum( np.logical_and(parent_cube, has_posvol )))



















