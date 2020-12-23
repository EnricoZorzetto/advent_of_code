import re
file = 'data16.txt'
# file = 'test16.txt'
# file = 'test16b.txt'


# blank line -> new passport
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]

myticket = []
TICKETS = []
RULES = {}
part = 0 # update at each blank line
for i in range(len(x)):
    # print(i)
    if i > 1 and x[i-1] == '':
        # print(x[i])
        pass
        # pass # DO NOT READ TITLE

    elif x[i] == '' and i > 0:
        # print('blank line number {}'.format(part))
        part += 1
        # PASSPORTS.append(mypass)
        # mypass = {}
    else:
        if part == 0:
            myx = x[i]
            # print(myx)
            myxs = re.split(': | or |-', myx)
            RULES[myxs[0]] = [int(myxs[1]), int(myxs[2]),
                              int(myxs[3]), int(myxs[4])]

        elif part == 1:
            myticket = [int(xi) for xi in x[i].split(',')]

        elif part == 2:
            TICKETS.append([int(xi) for xi in x[i].split(',')])

TSER_i = [0 for _ in TICKETS]
TSER = 0
nrules = len(RULES)
for it, tick in enumerate(TICKETS):
    for iff, field in enumerate(tick):
        print(it, tick, field)

        ISVALID = [0 for _ in range(nrules)]
        for ir, rule in enumerate(RULES.values()):
            if rule[0] <= field <= rule[1] or rule[2] <= field <= rule[3]:
                ISVALID[ir] = 1
        if max(ISVALID) == 0: # invalid field
            TSER += field
            TSER_i[it] += field

VTICKETS = [tick for it, tick in enumerate(TICKETS) if TSER_i[it] == 0]

print(len(TICKETS), len(VTICKETS))

print('The ticket scanning error rate (TSER) is = {}'.format(TSER))
            # print(rule)

        # if out of all ranges, add it to INVF

# for i in range(len(ORD_RULES)):
#     print(ORD_RULES[i])

TICKETS = VTICKETS
ORD_RULES = [[] for _ in RULES] # ordered rules, column by column
nfields = len(TICKETS[0])
for ir, rule in enumerate(RULES.values()): # LOOP ON RULES
    for iff in range(nfields):  # LOOP ON FIELDS
        ALLVALID = [0 for _ in TICKETS]
        for it, tick in enumerate(TICKETS):
            field = tick[iff]
            if rule[0] <= field <= rule[1] or rule[2] <= field <= rule[3]:
                ALLVALID[it] = 1
        if min(ALLVALID) == 1: # all rules are satisfied:
            ORD_RULES[iff].append(list(RULES.keys())[ir])

# for each fields, rules that are met
print(ORD_RULES)

# now remove the double

maxlen = max(len(li) for li in ORD_RULES)

# ORD_RULES2 = [i for i in ORD_RULES]

rulenames = list(RULES.keys())
# ORD_RULES_UN = [i for i in ORD_RULES]

# for ir, rule in enumerate(rulenames):
while maxlen > 1:
    for i, myrule in enumerate(ORD_RULES):
        for ii, myfield in enumerate(myrule):
            others = [elem for ie, elem in enumerate(ORD_RULES) if ie != i]
            all_others = [item for sublist in others for item in sublist]
            # print(myfield)
            # print(all_others)
            if myfield not in all_others:
                ORD_RULES[i] = [myfield]
        maxlen = max(len(li) for li in ORD_RULES)

print(ORD_RULES)
# print(ORD_RULES_UN)

print(myticket)

myticket = [t for i, t in enumerate(myticket) if len(ORD_RULES[i]) > 0]
ORD_RULES = [i for i in ORD_RULES if len(i) > 0]

MT = {ff:vv for ff, vv in zip([i[0] for i in ORD_RULES],myticket)}

PROD = 1
for key, item in MT.items():
    if key.split(' ')[0] == 'departure':
        print(key, item)
        PROD *= item
        print(PROD)

print('The product is = {}'.format(PROD))


# while maxlen > 1:
#     for i, rulei in enumerate(ORD_RULES2):
#         print(rulei)
#         if len(rulei) == 1:
#             myitem = rulei[0]
#             # remove rulei from all other items:
#             for j, rulej in enumerate(ORD_RULES2):
#                 print(rulej)
#                 if i != j and myitem in rulej:
#                     rulej2 = rulej.remove(myitem)
#                     ORD_RULES2[j] = rulej2

