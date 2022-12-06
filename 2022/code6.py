
import os
import copy

# inputfile = "test_data6.txt"
inputfile = "data6.txt"

with open(inputfile) as f:
    mys = f.read().splitlines()[0]

first_packet = -1
first_message = -1

for i in range(4, len(mys)+1):
    myp = set(mys[i-4:i])
    if (len(myp)==4 and first_packet<0):
        first_packet = i

for i in range(14, len(mys)+1):
    myp = set(mys[i-14:i])
    if (len(myp)==14 and first_message<0):
        first_message = i


print("Part 1 :: first packet pos = {}".format(first_packet))
print("Part 2 :: first message pos = {}".format(first_message))

    