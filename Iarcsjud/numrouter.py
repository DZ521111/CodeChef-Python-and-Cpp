'''
Author : Dhruv B Kakadiya

'''

from numpy.linalg import matrix_power as mp
import numpy as np

m = 42373
n = int(input())
mat = [0 for _ in range(n)]
imat = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    mat[i] = [int(w) for w in input().split()]
    imat[i][i] = 1
st,end,k = map(int,input().split())

while k:
    if k % 2:
        imat = np.dot(imat,mat)
        imat = [[ele%m for ele in i] for i in imat]
    mat = np.dot(mat,mat)
    mat = [[ele%m for ele in i] for i in mat]
    k //= 2
print(imat[st-1][end-1]%m)
