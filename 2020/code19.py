
# file = 'data19.txt'
file = 'test19.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]