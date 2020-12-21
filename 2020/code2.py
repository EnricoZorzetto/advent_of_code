import os
import pandas as pd

file = 'data2.txt'

df = pd.read_csv(file, sep='\s+', header = None,
                 names = ['bounds', 'letter', 'pass'] )
df['lb'] = df['bounds'].apply(lambda x: int(x.split('-')[0]))
df['ub'] = df['bounds'].apply(lambda x: int(x.split('-')[-1]))
df['letter'] = df['letter'].apply(lambda x: x[0])

# pw = df['pass'][0]
# lt = df['letter'][0]
# ub = df['ub'][0]
# lb = df['lb'][0]

# first interpretation of the policy
def isvalid1(lb, ub, lt, pw):
    pwlist = list(pw)
    no = len([x for x in pwlist if x == lt])
    if no >= lb and no <= ub:
        isval = True
    else:
        isval = False
    return isval

df['isval1'] = df.apply(lambda x: isvalid1(
       x['lb'], x['ub'], x['letter'], x['pass']), axis = 1)


number1 = df[df['isval1']].shape[0]
print('first interpretation of the policy: \n the '
      'number of valid passwords is {}'.format(number1))



# second interpretation of the policy

def isvalid2(lb, ub, lt, pw):

    # # first check that the password contains the two positions
    lenp = len(pw)
    if lb > lenp or ub > lenp:
        isval = False
    else:
        test1 =  pw[lb-1] == lt
        test2 = pw[ub-1] == lt
        if test1 + test2 == 1: # if only one is true
            isval = True
        else:
            isval = False
    return isval


df['isval2'] = df.apply(lambda x: isvalid2(
    x['lb'], x['ub'], x['letter'], x['pass']), axis = 1)


number2 = df[df['isval2']].shape[0]
print('second interpretation of the policy: \n the '
      'number of valid passwords is {}'.format(number2))





