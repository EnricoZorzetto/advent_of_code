
import os

file = 'data7.txt'
# file = 'test7b.txt'
# read file
# space OR newline -> new field
# blank line -> new passport
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]
nb = len(x)
# separate
ob = [xi.split(' contain ')[0].rsplit(' ', 1)[:-1][0] for xi in x]
innlist = [xi.split(' contain ')[-1][:-1].split(', ') for xi in x]
innum = [xi.split(' contain ')[-1][:-1].split(', ') for xi in x]

for i, listi in enumerate(innlist):
    nelem = len(listi)
    for j, elemj in enumerate(innlist[i]):
        innum[i][j] = elemj.split(' ')[0]
        innlist[i][j] = ' '.join(elemj.split(' ')[1:3])

# iteratively find all the bags which can contain at least a shiny gold bag
ALLBAGS = []
NEWBAGS = ['shiny gold']
# mycolor = 'shiny gold'
# NEWBAGS = []

added = 1
while added > 0:
    NEWBAGS0 = []
    for nbag in NEWBAGS:
        for i, listi in enumerate(innlist):
            if nbag in listi:
                NEWBAGS0.append(ob[i])
    NEWBAGS = [b for b in NEWBAGS0 if b not in ALLBAGS]
    if len(NEWBAGS) > 0:
        for newj in NEWBAGS:
            if newj not in ALLBAGS:
                ALLBAGS.append(newj)
    added = len(NEWBAGS)

print('Total number of bags is = {}'.format(len(ALLBAGS)))

# FIND OUT HOW MANY BAG MUST BE WITHIN A SHINY GOLD


CONTAINED = []
NUMBER = []
NEWC = []
mycolor = 'shiny gold'
added = 1
for i, listi in enumerate(innlist):
    if ob[i] == mycolor:
        for j in range(len(listi)):
            if len(listi[j]) > 0 and innum[i][j] != 'no': # append contained
                CONTAINED.append(listi[j])
                NUMBER.append(innum[i][j])
                NEWC.append(listi[j])
                added = len(NEWC)


CONTAINED = []
NUMBER = []
OLDC = ['shiny gold']
OLDNUMBER = [1]
# mycolor = 'shiny gold'
added = 1
while added > 0:
    NEWC = []
    NEWNUMBER = []
    for mycolor, myoldnumber in zip(OLDC, OLDNUMBER):
        for i, listi in enumerate(innlist):
            if ob[i] == mycolor:
                for j in range(len(listi)):
                    if len(listi[j]) > 0 and innum[i][j] != 'no': # append contained
                        CONTAINED.append(listi[j])
                        NUMBER.append(int(innum[i][j])*myoldnumber)
                        NEWC.append(listi[j])
                        NEWNUMBER.append(int(innum[i][j]) * myoldnumber)
    OLDC = NEWC
    OLDNUMBER = NEWNUMBER
    added = len(NEWC)
    print('added', added)

res = sum([int(iii) for iii in NUMBER])

print('total number of bags contained is {}'.format(res))

# # count = 0
#
# # mycolor = 'shiny gold'
# NEWC = ['shiny gold']
# added = 1
# while added > 0:
#     for mycolor in NEWC:
#         for i, listi in enumerate(innlist):
#             if ob[i] == mycolor:
#                 for j in range(len(listi)):
#                     CONTAINED.append(listi[j])
#                     NUMBER.append(innum[i][j])
#                     NEWC.append(listi[j])
#
#
#
