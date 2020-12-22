
file = 'data10.txt'
# file = 'test10.txt'
with open(file) as f:
    content = f.readlines()
# content = content[:-1]
x = [int(x.strip('\n')) for x in content]
n = len(x)

xs = sorted(x)
maxval = max(xs)

setx = list(set(xs))
print(len(setx), len(x)) # ok they are all different!


diffs = [0 for x in range(n-1)]
for i in range(1, n):
    diffs[i-1] = xs[i] - xs[i-1]
diffs.append(3) # difference with my device
diffs.append(xs[0]-0) # difference with my device


print(max(diffs))
print(min(diffs))

n1 = len([i for i in diffs if i == 1])
n3 = len([i for i in diffs if i == 3])
myprod = n1*n3
print('The product of joltage difference is = {}'.format(myprod))

# how many different arrangements are there?
count = 0
init = 1

CVALS = [0]
NEWVALS = [0]
while len(NEWVALS) > 0:
    NEWVALS = []
    for cval in CVALS: # loop on current values
        NEWVALS += [i for i in xs if i - cval <= 3 and i > cval] # next possible vals

    CVALS = NEWVALS

    for cval in CVALS: # loop on current values
        if cval == maxval:
            count += 1 # ONE COMPLETE PATH FOUND

print('The total number of combinations is = {}'.format(count))
