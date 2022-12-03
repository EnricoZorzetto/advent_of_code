
import os
import sys
import string
import numpy as np


# inputfile = "test_data3.txt"
inputfile = "data3.txt"

let = list(string.ascii_lowercase) + list(string.ascii_uppercase)
num = list(range(1, len(let)+1)) 
letters = {key:val for key, val in zip(let, num)}


with open(inputfile) as f:
    mylist = f.read().splitlines() 

# PART 1: intersections
npacks = len(mylist)
values1 = []
for i in range(npacks):
    leni = len(mylist[i])
    if (leni % 2 != 0):
        sys.exit('Odd number of elements in pack # {}'.format(i))
    p1 = mylist[i][:leni//2]
    p2 = mylist[i][leni//2:]
    inters = ''.join(set(p1).intersection(p2))
    if (len(inters) != 1):
        sys.exit('Number of intersections is not one!')
    values1.append(letters[inters])

print("Part 1 :: The result is = {}".format(np.sum(values1)))

# PART 2: intersections between groups of 3
ngr = npacks//3
values2 = []
for i in range(ngr):
    myp = mylist[ (i)*3  : (i+1)*3  ]
    inters0 = ''.join(set(myp[0]).intersection(myp[1]))
    inters = ''.join(set(inters0).intersection(myp[2]))
    values2.append(letters[inters])

print("Part 2 :: The result is = {}".format(np.sum(values2)))



