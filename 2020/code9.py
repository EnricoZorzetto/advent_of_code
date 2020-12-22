
file = 'data9.txt'; np = 25
# file = 'test9.txt'; np = 5
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]
x = x[:-1]
nb = len(x)

# find the FIRST number which is not the sum of 2 of the previous 25
preamb = x[:5]
seq = x[5:]
nseq = len(seq)
# print(preamb)
# print(len(preamb))

for i in range(len(x)):
    if i >= np:
        previous = x[i-np:i]
        mynumber = int(x[i])
        # print(i, x[i])
        # print(previous)
        # check whether x[i] is the sum of 2 of the 5 numbers:
        sums = []
        for j in range(np):
            for k in range(j+1, np):
                sums.append(int(previous[j]) + int(previous[k]))
        if mynumber not in sums:
            print(mynumber)

# find a contiguous range of N>= 2 numbers which sum to this value
mynum = 57195069

# minval = min(x)
x = [int(xi) for xi in x if int(xi) < 57195069 ]
print(len(x))
nb = len(x)

csize = 4
# CSIZES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(csize-1, nb):
for csize in range(2, 100):
    for i in range(csize - 1, nb):
        # print(i)
        myseq = x[i-csize:i]
        # print(myseq)
        if mynum == sum(myseq):
            print(mynum)
            print(csize)
            print(myseq)
            print(min(myseq) + max(myseq))

