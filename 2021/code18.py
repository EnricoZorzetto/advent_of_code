

# inputfile = 'data18.txt'
# inputfile = 'test_data18.txt'
inputfile = 'test_data18_long.txt'
# inputfile = 'data18.txt'

with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

    myline0 = lines[0].split()
    myline1 = lines[1].split()
target area: x=241..275, y=-75..-49