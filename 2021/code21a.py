

# P 1 starting position: 4 # TEST
# P 2 starting position: 8
# P 1 starting position: 2 # REAL
# P 2 starting position: 5


def detroll(count):
    if count < 100:
        return count + 1
    elif count == 100:
        return 1
    else:
        raise Exception("EWrror")

# p1 = 4; p2 = 8  # POS TEST
p1 = 2; p2 = 5# POS REAL
s1 = 0; s2 = 0  # SCORE
count = 0 # INIT DIE
die_totcount = 0 # INIT DIE
p1 = p1 - 1; p2 = p2 -1
turn = 0
maxscore = 1000
while s1 < maxscore and s2 < maxscore:
    turn += 1
    if turn % 2 == 1: # ODD< P1
        count = detroll(count)
        die_totcount += 1
        p1 += count
        count = detroll(count)
        die_totcount += 1
        p1 += count
        count = detroll(count)
        die_totcount += 1
        p1 += count
        p1 = p1 % 10
        s1 += p1 + 1
        print('pl1 turn = {}'.format(turn))
        print('p1 = {}, s1 = {}'.format(p1, s1))
        if s1 >= maxscore:
            print('end; s1 won; s2 = {}'.format(s2))
            print('die totcount = {}'.format(die_totcount))
            print('die totcount * lose = {}'.format(die_totcount*s2))

    if turn % 2 == 0: # ODD< P1
        count = detroll(count)
        die_totcount += 1
        p2 += count
        count = detroll(count)
        die_totcount += 1
        p2 += count
        count = detroll(count)
        die_totcount += 1
        p2 += count
        p2 = p2 % 10
        s2 += p2 + 1

        if s2 >= maxscore:
            print('end; s2 won; s1 = {}'.format(s1))
            print('die totcount = {}'.format(die_totcount))
            print('die totcount * lose = {}'.format(die_totcount*s1))

        print('pl2 turn = {}'.format(turn))
        print('p2 = {}, s2 = {}'.format(p2, s2))








