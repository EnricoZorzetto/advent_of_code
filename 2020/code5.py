import os

file = 'data5.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content][:-1]
ns = len(x)

fb = [xi[:7] for xi in x]
lr = [xi[7:] for xi in x]

# convert from binary
def str_2_base10(mystring, one='B'):
    # given a string compute base-
    base10 = 0
    n = len(mystring)
    for i in range(n):
        if mystring[i] == one:  # one!
            base10 = base10 + 2 ** (n - i - 1)
    return base10

seatID = []
for i in range(ns):
    row = str_2_base10(fb[i], one='B')
    col = str_2_base10(lr[i], one='R')
    seatID.append(row*8+col)

print('The maximum seat ID is {}'.format(max(seatID)))

sseat = sorted(seatID)
ls = list(range(sseat[0], sseat[-1]+1))

print(sseat[0], ls[0])
print(sseat[-1], ls[-1])
print(len(sseat), len(ls))

uniques = [elem for elem in ls if elem not in sseat]

print('My seat is = {}'.format(uniques))

# # TEST
# mystring = 'BFFFBBF'
# mystring2 = 'RRR'
# row = str_2_base10(mystring, one='B')
# col = str_2_base10(mystring2, one='R')
#
# seatID = row*8 + col
#
# print(row, col, seatID)



