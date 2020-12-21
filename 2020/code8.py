
file = 'data8.txt'
# file = 'test8a.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]

n = len(x)

already_executed = [0 for i in x]

iter = 0
accumulator = 0

# mycommand = x[0]

# com, val = mycommand.split(' ')


while max(already_executed) < 2:

    mycommand = x[iter]
    com, val = mycommand.split(' ')
    print(com, val)

    if com == 'acc':
        accumulator += int(val)
        iter += 1
    elif com == 'jmp':
        iter += int(val)
    elif com == 'nop':
        iter += 1
    else:
        print('WARNING: Invalid command')

    already_executed[iter] += 1

print('Value of the accumulator is = {}'.format(accumulator))



def runprog(x):
    # run the program and tells me if it is finite, and accumulator value
    iter = 0
    accumulator = 0
    n = len(x)
    already_executed = [0 for i in x]
    while max(already_executed) < 2 and iter < n:

        mycommand = x[iter]
        com, val = mycommand.split(' ')
        # print(com, val)
        # print('exec line = {}'.format(iter))

        if com == 'acc':
            accumulator += int(val)
            iter += 1
        elif com == 'jmp':
            iter += int(val)
        elif com == 'nop':
            iter += 1
        else:
            print('WARNING: Invalid command')
        if iter < n:
            already_executed[iter] += 1

    if max(already_executed) == 2:
        isfinite = False
    elif iter == n:
        isfinite = True
    else:
        isfinite = 0
        print('WARNING: Something went wrong!')
    return isfinite, accumulator



# change one instruction so that the loop is finite:

isfinite = False
i = 0
while not isfinite:
    # print('#######################################')
    xtemp = x.copy()
    com = x[i].split(' ')[0]
    val = x[i].split(' ')[1]
    if com == 'nop':
        xtemp[i] = ' '.join(['jmp', val])
        isfinite, accval = runprog(xtemp)
    elif com == 'jmp':
        xtemp[i] = ' '.join(['nop', val])
        isfinite, accval = runprog(xtemp)
    else:
        pass
    i += 1
print('isfinite = {}, accumulator value = {}'.format(isfinite, accval))

