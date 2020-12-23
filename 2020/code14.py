
file = 'data14.txt'
# file = 'test14.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]
