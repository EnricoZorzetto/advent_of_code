
import os
import sys
import string
import numpy as np
import pandas as pd


inputfile = "test_data4.txt"
# inputfile = "data4.txt"

df = pd.read_csv(inputfile, header=None, sep=',')
A = df[0].values
B = df[1].values
print(A, B)
ng = len(A)
val1 = 0
val2 = 0
for i in range(ng):
    l1 = int( A[i].split('-')[0] )
    u1 = int( A[i].split('-')[-1] )
    l2 = int( B[i].split('-')[0] )
    u2 = int( B[i].split('-')[-1] )
    if (((l1<=l2) and (u1>=u2)) or ((l2<=l1) and (u2>=u1))):
        val1=val1+1
    
    overlap = ((l1<=u2)and(u1>=l2) or (l2<=u1)and(u2>=l1))
    if overlap: 
        val2 = val2 + 1

print("Part 1 :: value = {}".format(val1))
print("Part 2 :: value = {}".format(val2))