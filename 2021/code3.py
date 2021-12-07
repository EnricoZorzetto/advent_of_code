import os
import pandas as pd
import numpy as np

# inputfile = 'test_data3.txt'
inputfile = 'data3.txt'


with open(inputfile) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

lenn = np.array( [list(str(li)) for li in lines])
numvec, numlen = np.shape(lenn)
mid = numvec // 2

gamma_rate_bin = np.zeros(numlen).astype(int)
epsilon_rate_bin = np.zeros(numlen).astype(int)
for i in range(numlen):
    A = lenn[:,i].astype(int)
    if np.sum(A) > mid:
        gamma_rate_bin[i] = 1
    if np.sum(A) < mid:
        epsilon_rate_bin[i] = 1
    # if they are equal what happens??? not accounted for her

def bin_to_dec(bin):
    dec = 0
    # bins = str(bin)
    ndig = len(bin)
    for i in range(ndig):
        exp = ndig - 1 - i
        dec = dec + int(bin[i]) * 2**exp
    return int(dec)

epsilon_rate = bin_to_dec(epsilon_rate_bin)
gamma_rate = bin_to_dec(gamma_rate_bin)
prod = gamma_rate * epsilon_rate
print("res part1:: their product is = {}".format(prod))


# find OGR
# gamma_rate_bin = np.zeros(numlen).astype(int)
# epsilon_rate_bin = np.zeros(numlen).astype(int)
mcv = np.zeros(numlen).astype(int)
nleft = lenn.copy()
i = 0
while i < numlen and np.shape(nleft)[0] > 1:
    # for i in range(numlen):
    # mid1 = nleft.shape[0] // 2
    A = nleft[:,i].copy().astype(int)

    n1 = np.sum(A)
    n0 = np.size(A) - n1
    if n1 >= n0:
        mcv[i] = 1 # most common values is 1, or same number
    else:
        mcv[i] = 0 # most common values is 1, or same number

    # find the most common number; set to 1 if equal
    # if np.sum(A) >= np.size(A)//2:
    #     mcv[i] = 1 # most common values is 1, or same number
    # else:
    #     mcv[i] = 0 # most common value is 0
    # cond = np.where(nleft[:,i].astype(int) == mcv[i])
    cond = nleft[:,i].astype(int) == mcv[i]
    print('cond', cond)
    nleft_reduced = nleft[cond].copy()
    nleft = nleft_reduced.copy()
    print(nleft_reduced.shape)
    i = i + 1 # update position counter
assert(np.shape(nleft)[0]==1)
OGR = bin_to_dec(np.ravel(nleft))

lcv = np.zeros(numlen).astype(int)
nleft2 = lenn.copy()
i = 0
while i < numlen and np.shape(nleft2)[0] > 1:
    # for i in range(numlen):
    mid2 = nleft2.shape[0] // 2
    A = nleft2[:, i].copy().astype(int)

    n1 = np.sum(A)
    n0 = np.size(A) - n1
    if n1 >= n0:
        lcv[i] = 0
    else:
        lcv[i] = 1

    cond2 = nleft2[:, i].astype(int) == lcv[i]
    nleft_reduced2 = nleft2[cond2].copy()
    nleft2 = nleft_reduced2.copy()
    print(nleft_reduced2.shape)
    i = i + 1  # update position counter

assert(np.shape(nleft2)[0]==1)
CSR = bin_to_dec(np.ravel(nleft2))

print('part2:: CSR * OGR = {}'.format(CSR * OGR))



