
file = 'data13.txt'
# file = 'test13.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]

mytime = int(x[0]) # earliest timestamp I could depart on a bus
L1 = x[1].split(',') # buses in service
# OTHER TESTS
# L1 = [7,13,'x','x',59,'x',31,19]
# L1 = [17,'x',13,19]
# L1 = [1789,37,47,1889]
BUSES = [int(i) for i in L1 if i != 'x']

# Earliest bus I can take to the airport?
COUNT = [0 for _ in BUSES]
for ib, bus in enumerate(BUSES):
    count = 0
    while count < mytime:
        count += bus
    COUNT[ib] = count

mintime = min(COUNT)
busindex = COUNT.index(mintime)
mybus = BUSES[busindex]
print('(PART 1) The requested product is = {}'.format(mybus*(mintime - mytime)))



# when do they all arrive in sequence?
IND_0 = list(range(len(L1))) # bus indices
IND = [i for i in range(len(IND_0)) if L1[i] != 'x']
print(IND)
print(BUSES)

ZIPPED = list(zip(BUSES, IND))
# S1 = list(zip(*sorted(ZIPPED, reverse=True)))

# sorted values (tuples)
BUS, INT = zip(*sorted(ZIPPED, reverse=True))


count = 0
match = False
iter = 0
increment = BUS[0]
ALREADY_INC = [0 for _ in range(len(BUS))]
while not match and iter < 10E10:
    count += increment
    # count += BUS[0]
    print('iter = {} | count = {}'.format(iter, count))
    MATCH = [0 for _ in range(1, len(BUS))]
    for i in range(1, len(BUS)):
        if (count + INT[i] - INT[0]) % BUS[i] == 0:
            MATCH[i-1] = 1
            if not ALREADY_INC[i]:
                ALREADY_INC[i] = 1
                increment *= BUS[i]
    if min(MATCH) > 0:
        match = True
    iter += 1
# print(count)
time = count - INT[0]
print(time)





