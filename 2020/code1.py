import urllib.request
import os

# does not work because I need to autenticate in the website
# url = 'https://adventofcode.com/2020/day/1/input'
# urllib.request.urlretrieve(url)

filename = 'data1.txt'

with open(filename) as f:
    content = f.readlines()
x = [int(x.strip('\n')) for x in content] 

n = len(x)

# find the product of the two numbers which sum is 2020
# for i in range(n):
#     for j in range(i+1, n):
#         if x[i] + x[j] == 2020:
#             print(x[i]*x[j])

# find the product of the three numbers which sum is 2020
# for i in range(n):
#     for j in range(i+1, n):
#         sumij = x[i] + x[j]
#         for k in range(n):
#             if sumij + x[k] == 2020 and k != i and k != j:
#                 print(x[i]*x[j]*x[k])
#                 print(i, j, k)
#                 print(x[i], x[j], x[k])

for i in range(n):
    for j in range(i+1, n):
        sumij = x[i] + x[j]
        for k in range(j, n):
            if sumij + x[k] == 2020:
                print(x[i]*x[j]*x[k])
                print(i, j, k)
                print(x[i], x[j], x[k])