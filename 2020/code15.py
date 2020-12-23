
INPUT = [1,2,16,19,18,0] # DATA

# INPUT = [1, 3, 2] # TEST
# INPUT = [3, 1, 2] # TEST
# INPUT = [0, 3, 6] # TEST

t0 = len(INPUT)
# NNUM = 2020
NNUM = 30000000
# NUM = [0 for _ in range(NNUM)]
IND = list(range(NNUM))

# NUM = [i for i in INPUT]
# SPOKEN = [i for i in INPUT]
SPOKEN = {i:INPUT.index(i) for i in INPUT[:-1]}


NUM = [0 for _ in range(NNUM)]
for i, inp in enumerate(INPUT):
    NUM[i] = INPUT[i]

for t in range(t0, NNUM):
    if t % 1000000 == 0:
        print('t = ', t)
    # print(SPOKEN)
    # print(NUM)
    # print(NUM[t-1])
    if NUM[t-1] not in SPOKEN:
        # numt = 0
        NUM[t] = 0
        # NUM.append(numt)
    else:
        # compute dt between two last times
        # dt = 1
        dt = t - SPOKEN[NUM[t-1]] - 1
        NUM[t] = dt
        # print('dt = {}'.format(dt))
        # NUM.append(dt)

    # add the previous number to the spoken list if not there:
    # if NUM[t-1] not in SPOKEN.keys():
    SPOKEN[NUM[t-1]] = t-1

# print(IND)
# print(NUM)
# print(SPOKEN)

print(NUM[-1])

# 30000000
len(NUM)