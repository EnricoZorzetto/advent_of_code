
file = 'data11.txt'
# file = 'test11.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]
x = [list(elem) for elem in x]
ls = [len(i) for i in x]

# fill a seat if no adjacent seats are occupied
# empty if >= 4 adjacent seats are occupied
def findadj(x, i0, j0):
    nrows = len(x)
    ncols = len(x[0])
    ii = [i0 - 1, i0, i0 + 1]
    jj = [j0 - 1, j0, j0 + 1]
    ii = [i for i in ii if i >= 0 and i < nrows]
    jj = [i for i in jj if i >= 0 and i < ncols]
    neigh_idx = [(a, b) for a in ii for b in jj if (a, b) != (i0, j0)]
    return neigh_idx

# count visible seats in each direction
#  get the closest either 'L' or '#'
# add to the counter only in the second case
def countvis(x, i0, j0):
    dirs = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
    nrows = len(x)
    ncols = len(x[0])
    VISIB = []
    OCCDIR = [0 for _ in dirs]
    for id, dir in enumerate(dirs):
        vis = []
        ix = i0 + dir[0]
        jx = j0 + dir[1]
        while 0 <= ix < nrows and 0 <= jx < ncols:
            vis.append((ix, jx))
            ix += dir[0]
            jx += dir[1]
        VISIB.append(vis)

        if len(vis) > 0:
            free_view = True
            for cell in vis:
                if free_view:
                    if x[cell[0]][cell[1]] == '#':
                        OCCDIR[id] = 1
                        free_view = False
                    elif x[cell[0]][cell[1]] == 'L':
                        OCCDIR[id] = 0
                        free_view = False
                    else:
                        pass
    return OCCDIR


def update(x, fill = False, empty = False, visible = False):
    xold = [[elem for elem in xi] for xi in x]
    xnew = [[elem for elem in xi] for xi in x]
    nrows = len(xold)
    ncols = len(xold[0])
    for i in range(nrows):
        for j in range(ncols):
            if visible:
                occdir = countvis(xold, i, j)
                nbusy = sum(occdir)
                visnumber = 5
            else:
                neigh_idx = findadj(xold, i, j)
                neigh = [xold[i][j] for (i, j) in neigh_idx]
                nbusy = len([a for a in neigh if a == '#'])
                visnumber = 4
            if xold[i][j] == 'L' and fill == True and nbusy == 0:
                xnew[i][j] = '#'
            if xold[i][j] == '#' and empty == True and nbusy >= visnumber:
                xnew[i][j] = 'L'
    return xnew


def countseat(x):
    countseats = 0
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == '#':
                countseats += 1
    return countseats


xold = x
xnew = update(x, fill = True)
count = 0
convergence = False
print('Iteration | number of seats currently filled:')
print('_____________________________________________')
while not convergence:
# fill and empty
    if count % 2 == 0: # EVEN - START WITH THIS - 0, 2, 4 ...
        xnew = update(xold, fill=True, visible=True)
    else: # steps 1, 3, 5 ...
        xnew = update(xold, empty=True, visible=True)
    if xnew == xold:
        convergence = True
    xold = [[elem for elem in xi] for xi in xnew]
    # xold = xnew
    # for i in range(len(xold)):
    #     print(xold[i])
    count += 1
    print('Iter = {} | Seats = {}'.format(count, countseat(xold)))
print('_____________________________________________')
print('convergence = {}; Total number of seats filled = '
                  '{}'.format(convergence, countseat(xold)))

