
file = 'data14.txt'
# file = 'test14b.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]


def dec_to_binary(mynum, max_nbits = 36):
    res = mynum
    bin = []
    while res > 1:
        res = mynum // 2
        myrem = mynum % 2
        bin.append(myrem)  # from least to more significant
        mynum = res
    bin.append(res)
    bin = bin[::-1] # reverse order
    lengn = len(bin)
    if lengn < max_nbits:
        bin = [0 for _ in range(max_nbits - lengn)] + bin
    elif lengn > max_nbits:
        print('WARNING: More than {} bits needed to store '
              'this binary number!'.format(max_nbits))
    return bin


def binary_to_dec(mybin):
    mynum = 0
    nbits = len(mybin)
    powers = [nbits - i - 1 for i in range(nbits)]
    for i in range(nbits):
        mynum += mybin[i] * 2 ** powers[i]
    return mynum


def apply_mask(mybin, mymask):
    # apply mask to a 36-digits binary number
    nbits = len(mybin)
    nbits2 = len(mymask)
    newbin = [i for i in mybin]
    if nbits != nbits2:
        print('WARNING: The mask has the wrong '
              '   length for this binary number')
    for i in range(nbits):
        if mymask[i] == '0':
            newbin[i] = 0
        elif mymask[i] == '1':
            newbin[i] = 1
        else:
            pass
    return newbin


def apply_mask_2(mynum, mymask):
    mybin = dec_to_binary(mynum)
    nbits = len(mybin)
    nbits2 = len(mymask)
    newbin = [i for i in mybin]
    if nbits != nbits2:
        print('WARNING: The mask has the wrong '
              '   length for this binary number')
    for i in range(nbits):
        if mymask[i] == '0':
            pass
        elif mymask[i] == '1':
            newbin[i] = 1
        elif mymask[i] == 'X':
            newbin[i] = 'X'
        else:
            print('WARNING: invalid value in mask')
    # num_bins = len([ix for ix in newbin if ix == 'X'])
    # print(num_bins)
    return newbin


def comp_memory_spots(mynum, mymask):
    newbin = apply_mask_2(mynum, mymask)
    # compute all possible binaries and convert to base 10
    Xind = [ix for ix in range(len(newbin)) if newbin[ix] == 'X']
    Xnum = len(Xind)
    Nnum = 2**Xnum
    # print(Nnum)
    BASE_10_NUMS = list(range(Nnum))
    BASE_2_NUMS = [dec_to_binary(x, max_nbits=Xnum) for x in BASE_10_NUMS]
    # print(Xnum, Nnum)
    # span all numbers 0-Nnum-1, conv to binary and add them
    MEM_SPOTS = []
    for i in range(Nnum):
        NUMI_2 = [x for x in newbin]
        for j in range(Xnum):
            NUMI_2[Xind[j]] = BASE_2_NUMS[i][j]
        NUMI_10 = binary_to_dec(NUMI_2)
        MEM_SPOTS.append(NUMI_10)
    return MEM_SPOTS


# TEST CONVERSION FUNCTIONS:
mynum = 1716
mybin = dec_to_binary(mynum)
mynum2 = binary_to_dec(mybin)
print('{} should be equal to {}'.format(mynum, mynum))

# TEST APPLY FUNCTION:
mymask_string = '0X10110X1001000X10X00X01000X01X01101'
newbin = apply_mask(mybin, list(mymask_string))
# print(list(mymask_string))
# print(mybin)
# print(newbin)


MEM = {}
current_mask = None
for i, xi in enumerate(x):
    command, value = xi.split(' = ')
    if command == 'mask': # update the current mask used
        current_mask = list(value)
        # print(current_mask)
    if command[:3] == 'mem':
        c2 = command.replace('[', ']')
        mem_spot = int(c2.split(']')[1])
        binary_value = dec_to_binary(int(value))
        masked_value = apply_mask(binary_value, current_mask)
        base10_value = binary_to_dec(masked_value)
        MEM[mem_spot] = base10_value
# SUM ALL VALUES LEFT IN MEMORY
sumval = sum(MEM.values())
print('(PART 1) The sum of the values left in memory is = {}'.format(sumval))


MEM2 = {}
current_mask = None
for i, xi in enumerate(x):
    command, value = xi.split(' = ')
    if command == 'mask': # update the current mask used
        current_mask = list(value)
    if command[:3] == 'mem':
        c2 = command.replace('[', ']')
        mem_spot_0 = int(c2.split(']')[1])
        MEM_SPOTS = comp_memory_spots(mem_spot_0, current_mask)
        for mem_spot in MEM_SPOTS:
            MEM2[mem_spot] = int(value) # DOES NOT CHANGE
# SUM ALL VALUES LEFT IN MEMORY
sumval = sum(MEM2.values())
print('(PART 2) The sum of the values left in memory is = {}'.format(sumval))
