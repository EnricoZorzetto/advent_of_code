
import re

def splitnumber(a):
    if a % 2 > 0:
        return a // 2, a // 2 + 1 # ROUNDED DOWN
    else:
        return a // 2, a // 2

assert splitnumber(10) == (5,5)
assert splitnumber(11) == (5,6)


def get_bracket(mlist):
    res0 = re.split("\[|,|\]", mlist)
    res = [x for x in res0 if x.isnumeric()]
    return res[0], res[1]


# SCAN FOR INNERMOST COUPLE
def explode(num):
    countb = 0
    lenn = len(num)
    # print(lenn)
    for i in range(lenn-4):
        # if num[i].isnumeric() and num[i+1].isnumeric():
        #     raise Exception('EXPLODE:: FOUND NUMBER LARGER THAN 9 !!!!!')
        nl = -1
        nr = -1  # init missing neighbours
        # print(countb)
        if num[i] == '[': countb += 1 # count also the innermost here
        if num[i] == ']': countb -= 1
        # if num[i] == '[' and num[i+4] == ']':
        if num[i] == '[':
            is_clean = num[i+1] != '[' and num[i+2] != '[' and num[i+3] != '['
            p4 = num[i+4] == ']'
            p5 = not p4 and num[i+5] == ']'
            p6 = not (p4 or p5) and num[i+6] == ']'
            if p4: endi = 5
            if p5: endi = 6
            if p6: endi = 7
            if (p4 or p5 or p6) and is_clean:
                mynum = num[i : i + endi] # endi was 5
                # print('found an inner bracket:: {}'.format(mynum))
                n1, n2 = get_bracket(mynum)
                n1 = int(n1); n2 = int(n2)
                bef = num[:i]
                if i+endi < lenn:
                    aft = num[i+endi:]
                else:
                    aft = ''
                # print("bef = {}, num = {}, aft = {}".format( bef, mynum, aft))
                # LOOK FOR THE CLOSEST NUMBER TO THE LEF::
                ii = i
                while ii > 0 and nl < 0:
                    ii -= 1
                    if num[ii].isnumeric() and not num[ii-1].isnumeric():
                        nl = int(num[ii])
                        # print('the closest num on the left is = {}'.format(nl))
                        iil = ii
                        beff = num[:iil]
                        bef = num[iil+1:i]
                        # print("beff = {}, bef = {}, num = {}".format(beff, bef, mynum))
                    if num[ii].isnumeric() and num[ii - 1].isnumeric():
                        nl = int(num[ii-1:ii+1])
                        # print('the closest num on the left is = {}'.format(nl))
                        iil = ii
                        beff = num[:iil-1]
                        bef = num[iil + 1:i]
                        # print("beff = {}, bef = {}, num = {}".format(beff, bef, mynum))
                ii = i + endi - 1
                # print('after', num[i+4:])
                while ii < lenn-2 and nr < 0:
                    # print(ii, lenn)
                    ii += 1
                    # print(num[ii])
                    if num[ii].isnumeric() and not num[ii+1].isnumeric():
                        nr = int(num[ii])
                        # print('the closest num on the right is = {}'.format(nr))
                        iir = ii
                        aft = num[i+endi:iir]
                        aftt = num[iir+1:]

                    if num[ii].isnumeric() and num[ii + 1].isnumeric():
                        nr = int(num[ii:ii+2])
                        # print('the closest num on the right is = {}'.format(nr))
                        iir = ii
                        aft = num[i + endi:iir]
                        aftt = num[iir + 2:]
                if countb >= 5:
                    if nl >= 0:
                        new1 = n1 + nl
                        bef = beff + str(new1) + bef
                    if nr >= 0:
                        new2 = n2 + nr
                        aft = aft + str(new2) + aftt
                    newnum = bef + '0' + aft
                    did_explode = True
                    return newnum, did_explode
    did_explode = False
    return num, did_explode # NO EXPLODE

#
# # TEST EXPLODE
assert explode("[[[[[9,8],1],2],3],4]")[0] == "[[[[0,9],2],3],4]"
assert explode( "[7,[6,[5,[4,[3,2]]]]]" )[0] == "[7,[6,[5,[7,0]]]]"
assert explode("[[6,[5,[4,[3,2]]]],1]")[0] == "[[6,[5,[7,0]]],3]"
assert explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")[0] == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
assert explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")[0] == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
# #

def split(num):
    lenn = len(num)
    # print(lenn)
    for i in range(lenn-1):
        if num[i].isnumeric() and num[i+1].isnumeric(): # >= 10 for sure
            mynum = int(num[i:i+2])
            bef = num[:i]
            aft = num[i+2:]
            # print(mynum, bef, aft)
            mynum2 = splitnumber(mynum)
            mystr2 = "[{},{}]".format(mynum2[0], mynum2[1])
            # print(mystr2)
            did_split = True
            return bef + mystr2 + aft, did_split # return the lefternmost
    did_split = False
    return num, did_split # NO SPLIT


def adds(str1, str2):
    return "["+str1+","+str2+"]"


def reduce(num):
    exp_or_split = True
    while exp_or_split:
        num2, did_exp = explode(num)
        # if did_exp: print('did explode!')
        if not did_exp:
            num3, did_split = split(num2)
        else:
            did_split = False
            num3 = num2
        # if did_split: print('did split!')
        exp_or_split = did_exp or did_split
        num = num3
    return num



def magn(num):
    lenn = len(num)
    for i in range(lenn-4):
        if num[i] == '[':
            j = i+1
            nstring = ''
            while num[j] != '[' and num[j] !=']':
                nstring += num[j]
                j += 1
            if num[j]  == ']':
                # print('found a bracket: {}'.format(nstring))
                bef = num[:i]
                aft = num[j+1:]
                # print('bef = {}, aft = {}'.format(bef, aft))
                res0 = re.split("\[|,|\]", nstring)
                res = [x for x in res0 if x.isnumeric()]
                # print('split res = ', res)
                if len(res) == 1:
                    magn = res[0]
                    # print('len {} == 1'.format(res))
                elif len(res) == 2:
                    magn = str(3 * int(res[0]) + 2 * int(res[1]))
                    # print('len {} == 2'.format(res))
                else:
                    raise Exception('too long!')
                # print('magn = {}'.format(magn))
                # n1 = int(n1); n2 = int(n2)
                # magn = str( n1*3 + n2*2 )
                newnum = bef + magn + aft
                return newnum

def magnitude(num):
    while num[0] == '[':
        newnum = magn(num)
        num = newnum
        # print(num)
    return num


def summ(lines):
    sum = lines[0]
    for n in lines[1:]:
        sum = adds(sum, n)
        sum = reduce(sum)
        # print(sum)
    return sum

# MORE TESTING
string1 = "[[[[4,3],4],4],[7,[[8,4],9]]]"
string2 = "[1,1]"

res0 = adds(string1, string2)

res1 = explode(res0)[0]
res2 = explode(res1)[0]
res3 = split(res2)[0]
res4 = split(res3)[0]
res5 = explode(res4)[0]

assert res0 == "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
assert res1 == "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"
assert res2 == "[[[[0,7],4],[15,[0,13]]],[1,1]]"
assert res3 == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
assert res4 == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
assert res5 == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

print(reduce(res0))
assert reduce(res0) == res5


assert magnitude( "[[1,2],[[3,4],5]]") == "143"
assert magnitude("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]") == "1384"
assert magnitude("[[[[1,1],[2,2]],[3,3]],[4,4]]") ==  "445"
assert magnitude("[[[[3,0],[5,3]],[4,4]],[5,5]]") == "791"
assert magnitude("[[[[5,0],[7,4]],[5,5]],[6,6]]") == "1137"
assert magnitude("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]") == "3488"

# DO THE ACTUAL ANALYSIS
inputfile = 'data18.txt'
# inputfile = 'test_data18.txt'
# inputfile = 'test_data18d.txt'
# inputfile = 'test_data18_long.txt'
# inputfile = 'data18.txt'

with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]




# myres = summ(lines)
myres = magnitude(summ(lines))
# myres = reduce(mysum)
print('part 1 :: result = {}'.format(myres))


nlines = len(lines)


maxmag = []
for i in range(nlines):
    print(i)
    for j in range(nlines):
        if i != j:
            mylines = [lines[i], lines[j]]
            maxmag.append( int(magnitude(summ(mylines)) ))

import numpy as np
# print("part 2 :: result = {}".format(np.max(np.array(maxmag))))
print("part 2 :: result = {}".format(max((maxmag))))
