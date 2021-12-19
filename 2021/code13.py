import numpy as np
import matplotlib.pyplot as plt


# inputfile = 'test_data13.txt'
inputfile = 'data13.txt'

# read data
with open(inputfile) as file:
    # lines = [line.rstrip('\n').split() for line in file.readlines() if line.strip()]
    lines = [line.rstrip('\n').split(',') for line in file.readlines() if line.strip()]
    folds = [l[0].split(' ')[-1].split('=') for l in lines if l[0][:4]=='fold']
    points = [l for l in lines if l[0][:4] != 'fold']

# get array dimensions
xvals = [int(p[0]) for p in points] # first value x increases to the right
yvals = [int(p[1]) for p in points] # second value y increases to the bottom
nx = np.max(xvals) + 1
ny = np.max(yvals) + 1
npoints = len(xvals)
print('nx = {}, ny = {}, npoints = {}'.format(nx, ny, npoints))

F = np.zeros((ny, nx)).astype(bool)
for ip in range(npoints):
    F[yvals[ip], xvals[ip]] = True


def folder(F, fold):
    if fold[0] == 'y':
        fold1 = int(fold[1])
        # FV = F[:fold1+1, :].copy()
        FV = F[:fold1, :].copy()
        FB = np.flipud(F[fold1+1:, :].copy())
        # FV[:fold1,:] = np.logical_or(FV[:-1, :], FB)
        FV[:,:] = np.logical_or(FV[:, :], FB)
        print(F.shape, FV.shape, FB.shape)
    elif fold[0] == 'x':
        fold1 = int(fold[1])
        # FV = F[:, :fold1+1].copy()
        FV = F[:, :fold1].copy()
        FB = np.fliplr(F[:, fold1+1:].copy())
        print(F.shape, FV.shape, FB.shape)
        # FV[:, :fold1] = np.logical_or(FV[:, :-1], FB)
        FV[:, :] = np.logical_or(FV[:, :], FB)
    else:
        raise Exception('invalid fold was specified!')
    return FV

# after the first fold only::
F1 = folder(F, folds[0])
print('part 1 :: {} dots are visible!'.format( np.sum(F1)))


nfolds = len(folds)
FOLD = F
for ff in folds:
    FNEW = folder(FOLD, ff)
    FOLD = FNEW

plt.figure()
plt.imshow(FNEW)
plt.show()

print('part 2 :: {} dots; see figure for solution!'.format( np.sum(FNEW)))


