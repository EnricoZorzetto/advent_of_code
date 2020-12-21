import os

file = 'data6.txt'
# read file
# space OR newline -> new field
# blank line -> new passport
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]

GROUPS = []
people = []
for i in range(len(x)):
    if x[i] == '' and i > 0:
        GROUPS.append(people)
        people = []
    else:
        people.append(x[i])
# last value
if len(people) > 0:
    GROUPS.append(people)

mycount_1 = 0
mycount_2 = 0
MYCOUNT2 = [0 for x in range(len(GROUPS))]
for ig, group in enumerate(GROUPS):
    # NPEOPLE.append(len(group))
    myletters = ''.join(group)
    myuniques = set(myletters)
    mycount_1 += len(myuniques)

    # question to which everyone in a group answered yes
    myletterlist = list(myletters)
    for ue in myuniques:
        equals = [let for let in myletterlist if let == ue]
        len_equals = len(equals)
        if len_equals == len(group):
            mycount_2 += 1
            MYCOUNT2[ig] += 1



print('my count is = {}'.format(mycount_1))

print('my count is = {}'.format(mycount_2))
