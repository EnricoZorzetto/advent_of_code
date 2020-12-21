import os

file = 'data3.txt'

with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]
ns = len(x)
ls = len(x[0])

# posn = [0 for x in range(ns)]

# count_trees = 0 # first spot does not have a tree
# trees = [0 for x in range(ns)]
SLOPES = [1, 3, 5, 7, 1]
nslopes = len(SLOPES)
COUNT_TREES = [0 for x in range(nslopes)]
for k, slopek in enumerate(SLOPES):
    mypos = 0  # down - left
    for i in range(1, ns):
        if k < 4 or i % 2 == 0: # if k==0 update only for even i
            mypos = mypos + SLOPES[k]
        # print(mypos)
        if mypos >= ls: # periodic boundary condition
            mypos = mypos - ls
        # print(mypos)
        if x[i][mypos] == '#' and k < 4:
            COUNT_TREES[k] += 1
            # trees[i] = 1
        if x[i][mypos] == '#' and k == 4 and i % 2 == 0:
            COUNT_TREES[k] += 1



print('total number of trees encountered is {}'.format(COUNT_TREES))

prod = 1
for i in range(nslopes):
    prod *= COUNT_TREES[i]
print('the product is {}'.format(prod))








