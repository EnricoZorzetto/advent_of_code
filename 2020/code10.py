
file = 'data10.txt'
# file = 'test10.txt'
# file = 'test10a.txt'
with open(file) as f:
    content = f.readlines()
x = [int(x.strip('\n')) for x in content]

xs = sorted(x)
n = len(xs)
maxval = max(xs)

setx = list(set(xs))
print(len(setx), len(xs)) # ok they are all different!


diffs = [0 for xs in range(n-1)]
for i in range(1, n):
    diffs[i-1] = xs[i] - xs[i-1]
diffs.append(3) # difference with my device
diffs.insert(0, xs[0]-0) # difference with my device


print(max(diffs))
print(min(diffs))

n1 = len([i for i in diffs if i == 1])
n3 = len([i for i in diffs if i == 3])
myprod = n1*n3
print('The product of joltage difference is = {}'.format(myprod))

# how many different arrangements are there?
def count_arrange(xs, startval = 0):
    mymaxval = max(xs)
    count = 0
    # init = 1
    CVALS = [startval]
    NEWVALS = [0]
    while len(NEWVALS) > 0:
        NEWVALS = []
        for cval in CVALS: # loop on current values
            NEWVALS += [i for i in xs if i - cval <= 3 and i > cval] # next possible vals
            # print(NEWVALS)
        CVALS = NEWVALS
        for cval in CVALS: # loop on current values
            if cval == mymaxval:
                count += 1 # ONE COMPLETE PATH FOUND
    return count


if file[:4] == 'test':
    print('Only for test dataset, or it takes too long')
    mycount = count_arrange(xs)
    print('The total number of combinations is = {}'.format(mycount))




count_arrange([0, 1, 2, 3, 4], startval=0)



NCOMB = []

nold = 0
iold = 0
CURR = [0]
for i in range(n+1):
    if diffs[i] == 3:
        # print(i, CURR)
        if len(CURR)>1:
            # count and append number of ways to go from beginning to end
            npaths = count_arrange(CURR, startval = CURR[0])
            # print(npaths)
            NCOMB.append(npaths)
        CURR = []
    if i<n:
        CURR.append(xs[i])
    else:
        CURR.append(xs[-1]+3)


def multlist(l):
    res = 1
    for elem in l:
        res *= elem
    return res


mycount2 = multlist(NCOMB)
print(' (FAST) The total number of combinations is = {}'.format(mycount2))

