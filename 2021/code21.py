
import collections

# P 1 starting position: 4 # TEST
# P 2 starting position: 8
# P 1 starting position: 2 # REAL
# P 2 starting position: 5


# UPDATE CURRENT PL
def update(p1, f1, s1, p2, f2, s2):
    # d3vals = [3, 4, 5, 6, 7, 8, 9]
    # d3freq = [1, 3, 6, 7, 6, 3, 1]
    p1 = [x + y for x in p1 for y in d3vals] # rolls
    p1 = [ x % 10 for x in p1] # new positions, 0-9
    f1 = [x * y for x in f1 for y in d3freq]
    s1 = [ (s1[i] + ( (p1[i] + y) % 10) ) + 1 for i in range(len(s1)) for y in d3vals]
    # print(p1)
    # print(s1)
    # print(f1)
    # print(len(p1))
    # print(len(s1))
    # print(len(f1))
    # UPDATE THE OTHER
    p2 = [ x for x in p2 for y in d3vals]
    f2 = [ x*y for x in f2 for y in d3freq]
    s2 = [ x for x in s2 for y in d3vals]
    # print(p2)
    # print(s2)
    # print(f2)
    # print(len(p2))
    # print(len(s2))
    # print(len(f2))
    return p1, f1, s1, p2, f2, s2


def detroll(count):
    if count < 100:
        return count + 1
    elif count == 100:
        return 1
    else:
        raise Exception("EWrror")


def dirac(inp):
    res = []
    for ip in inp:
        res.append(ip + 1)
        res.append(ip + 2)
        res.append(ip + 3)
    return res


def dirac3(inp):
    res3 = dirac(dirac(dirac(inp)))
    resc3 = collections.Counter(res3)
    vals = list(resc3.keys())
    freq = list(resc3.values())
    return vals, freq

d3vals = [3, 4, 5, 6, 7, 8, 9]
d3freq = [1, 3, 6, 7, 6, 3, 1]


p1 = [4]; p2 = [8]  # POS TEST
# p1 = [2]; p2 = [5]# POS REAL
s1 = [0]; s2 = [0]  # SCORE
f1 = [1]; f2 = [1] # FREQUENCY OF EACH CASE
# count = 0 # INIT DIE
die_totcount = 0 # INIT DIE
p1 = [p - 1 for p in p1]; p2 = [p -1 for p in p2] # number 0 - 9 spots
turn = 0
# maxscore = 21
maxscore = 21

nw1 = 0
nw2 = 0
nuniv = 1
while nuniv > 0:
    turn += 1
    if turn % 2 == 1:
        p1, f1, s1, p2, f2, s2 = update(p1, f1, s1, p2, f2, s2)
    else:
        p2, f2, s2, p1, f1, s1 = update(p2, f2, s2, p1, f1, s1)

    print(len(p1), len(p2))
    print(sum(f1), sum(f2))
    print(len(s1), len(s2))

    nuniv = len(p1)
    print('turn = {}, nuniv = {}'.format(turn, nuniv))
    for i in range(nuniv):
        if s1[i] >= maxscore:
            nw1 += f1[i]
        elif s2[i] >= maxscore:
            nw2 += f2[i]

    shift = 0
    for i in range(nuniv):
        if s1[i-shift] >= maxscore or s2[i-shift] >= maxscore:
            _ = f1.pop(i - shift)
            _ = p1.pop(i - shift)
            _ = s1.pop(i - shift)
            _ = f2.pop(i - shift)
            _ = p2.pop(i - shift)
            _ = s2.pop(i - shift)
            shift += 1
    nuniv = len(p1)
    print('nuniv trimmed = {}'.format((nuniv)))

    print('nw1 = {}, nw2 = {}'.format(nw1, nw2))

    noverl = 0
    for i in range(nuniv):
        if p1[i] == p2[i] and s1[i] == s2[i]:
            noverl += 1
    print('turn = {}, noverl = {}'.format(turn, noverl))






