
import os
import copy

# inputfile = "test_data5.txt"
inputfile = "data5.txt"

def chunks(s, l):
    return list(s[0+i:l+i] for i in range(0, len(s), l))

with open(inputfile) as f:
    mylist = f.read().splitlines() 

# process initial stack
for il, l in enumerate(mylist):
    if l=='':
        len1 = il # length of first chunk
        len2 = len(mylist)-(il+1)
# print(len1, len2)
stack0  = mylist[:len1]
stack3 = [st.replace(' ', '.')+'.' for st in stack0]
nchunks = len(stack3[0])//4
assert(len(stack3[0])%4==0)
stack4 = [chunks(st,4) for st in stack3]

STACK = {i:[] for i in range(1, nchunks+1)}
for il in range(len(stack4)-2,-1,-1):
    # print(il)
    mylevel = stack4[il]
    for ic in range(len(mylevel)):
        item = mylevel[ic].replace('.', '')
        if item != '':
            # print('Adding item = {}'.format(item))
            STACK[ic+1].append(item)

# process orders
orders = mylist[len1+1:]
numb = [int(ord.split(' ')[1]) for ord in orders]
orig = [int(ord.split(' ')[3]) for ord in orders]
dest = [int(ord.split(' ')[5]) for ord in orders]

# move stuff around
def mover(STACK0, part1=True):
    STACK = copy.deepcopy(STACK0)
    for il in range(len(numb)):
        passed =  STACK[orig[il]][-numb[il]:]
        STACK[orig[il]] = STACK[orig[il]][:-numb[il]]
        if part1:
            STACK[dest[il]] = STACK[dest[il]] + passed[::-1] 
        else:
            STACK[dest[il]] = STACK[dest[il]] + passed 
    return STACK

STACK1 = mover(STACK, part1 = True)
STACK2 = mover(STACK, part1 = False)

msg1 = ''.join([STACK1[il][-1][1] for il in STACK1.keys()])
msg2 = ''.join([STACK2[il][-1][1] for il in STACK2.keys()])
print('Part 1 :: The message is = {}'.format(msg1))
print('Part 2 :: The message is = {}'.format(msg2))