file = 'data18.txt'
# file = 'test18.txt'
with open(file) as f:
    content = f.readlines()
x = [x.strip('\n') for x in content]

# + and * have the same precedence. (right to left)


# TEST(S)
x0 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
# x0 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'


class coolInt(int):

    def __mul__(self, other):
        return coolInt(int(other) * int(self))

    def __sub__(self, other):
        return coolInt(int(other) * int(self))

    def __add__(self, other):
        return coolInt(int(other) + int(self))

    def __pow__(self, other):
        return coolInt(int(other) + int(self))


def update_operation(x0, priority_add = False):
    if not priority_add:
        xnew = x0.replace('*', '-')
    else:
        xnew = x0.replace('+', '**')
    # xnew = xnew.replace('(', 'coolInt(')
    for i in range(10):
        # print(str(i))
        xnew = xnew.replace(str(i), 'coolInt({})'.format(i))
    # print(xnew)
    return xnew


res0 = eval(x0)
xnew1 = update_operation(x0, priority_add=False)
xnew2 = update_operation(x0, priority_add=True)
res1 = eval(xnew1)
res2 = eval(xnew2)
print('TEST: result with ordinary math = {}'.format(res0))
print('TEST: result with same order of operations = {}'.format(res1))
print('TEST: result with addition prioritized = {}'.format(res2))

SUM = 0
SUM2 = 0
for i in x:
    inew = update_operation(i, priority_add=False)
    inew2 = update_operation(i, priority_add=True)
    SUM += eval(inew)
    SUM2 += eval(inew2)

print('The result sum with same order '
      'of operations is = {}'.format(SUM))
print('Instead when the addition has priority '
      'the result is = {}'.format(SUM2))


