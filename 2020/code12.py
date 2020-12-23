
file = 'data12.txt'
# file = 'test12.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]

DIR = [elem[0] for elem in x]
VAL = [int(elem[1:]) for elem in x]

# POS0 = (0,0) # EAST (+), NORTH (+)
POS = [0,0]

VALsLR = [val for iv, val in enumerate(VAL) if DIR[iv] in ['L', 'R']]

# N -> move north
# S -> move south
# E -> move east
# W -> move west
# L -> turn left ** degrees (90, 180, 270)
# R -> turn right ** degrees
# F -> move forward in current direction



def rotate_right(mydir, angle):
    DIRS = ['S', 'W', 'N', 'E']
    myindex = DIRS.index(mydir)
    newindex = myindex + angle // 90
    if newindex > 3:
        newindex = newindex - 4
    newdir = DIRS[newindex]
    return newdir


def rotate_waypoint_right(WAYP, val):
    WDIR = [0, 0]
    ROTATED_WAYP = [0, 0]
    if WAYP[0] > 0:
        WDIR[0] = 'E'
    else:
        WDIR[0] = 'W'
        WAYP[0] = -WAYP[0]
    if WAYP[1] > 0:
        WDIR[1] = 'N'
    else:
        WDIR[1] = 'S'
        WAYP[1] = -WAYP[1]

    # rotate the two components separately:
    R0 = rotate_right(WDIR[0], val)
    R1 = rotate_right(WDIR[1], val)

    if R0 == 'N':
        ROTATED_WAYP[1] = WAYP[0]
    elif R0 == 'S':
        ROTATED_WAYP[1] = -WAYP[0]
    elif R0 == 'E':
        ROTATED_WAYP[0] = WAYP[0]
    elif R0 == 'W':
        ROTATED_WAYP[0] = -WAYP[0]

    if R1 == 'N':
        ROTATED_WAYP[1] = WAYP[1]
    elif R1 == 'S':
        ROTATED_WAYP[1] = -WAYP[1]
    elif R1 == 'E':
        ROTATED_WAYP[0] = WAYP[1]
    elif R1 == 'W':
        ROTATED_WAYP[0] = -WAYP[1]

    return ROTATED_WAYP






mydir = 'E'
for i, (val, dir) in enumerate(zip(VAL, DIR)):

    if dir == 'L':
        dir = 'R'
        val = 360 - val

    if dir == 'R':
        # print('before', mydir, 'rotate', val)
        mydir = rotate_right(mydir, val)


    else:
        if dir == 'F':
            dir = mydir # change in with the current dir

        if dir == 'E':
            POS[0] += val
        elif dir == 'W':
            POS[0] += -val
        elif dir == 'N':
            POS[1] += val
        elif dir == 'S':
            POS[1] += -val
        else:
            print('WARNING: Invalid direction!')
    # print(dir)
    # print(POS)
print('Manhattan distance is = {}'.format(abs(POS[0]) + abs(POS[1])))




# PART2: Follow the waypoint:
POS2 = [0,0]
WAYP = [10, 1] # EAST (+)
for i, (val, dir) in enumerate(zip(VAL, DIR)):

    if dir == 'L':
        dir = 'R'
        val = 360 - val

    if dir == 'R':
        # rotate the waypoint
        WAYP = rotate_waypoint_right(WAYP, val)

    if dir == 'F':
        # moves along the waypoint
        POS2[0] += val*WAYP[0]
        POS2[1] += val*WAYP[1]

    # move the waypoint
    if dir == 'E':
        WAYP[0] += val
    elif dir == 'W':
        WAYP[0] += -val
    elif dir == 'N':
        WAYP[1] += val
    elif dir == 'S':
        WAYP[1] += -val

    print(WAYP)
    print(dir)
    print(POS2)
print('(*NEW*) Manhattan distance is = {}'.format(abs(POS2[0]) + abs(POS2[1])))


