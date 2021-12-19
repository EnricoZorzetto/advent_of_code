

# inputfile = 'data16.txt'
# inputfile = 'test_data16.txt'
# inputfile = 'test_data16b.txt'
inputfile = 'test_data16_long.txt'
# inputfile = 'data16.txt'

with open(inputfile) as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

    myline0 = lines[0].split()
    myline1 = lines[1].split()
target area: x=241..275, y=-75..-49