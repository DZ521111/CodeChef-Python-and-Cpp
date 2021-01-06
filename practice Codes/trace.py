'''
Author : Dhruv B Kakadiya

'''


# cook your dish here
for _ in range(int(input())):
    n = int(input())
    matrix = []
    for i in range(n):
        y = list(map(int,input().split()))
        matrix.append(y)
    r, c = n, n
    temp = []
    for i in range(r):
        temp1, temp2 = 0, 0
        for j in range(c):
            temp1, temp2 = temp1 + matrix[i + j][j], temp2 + matrix[j][i + j]
            temp.append(temp1)
            temp.append(temp2)
        c -= 1
    print(max(temp))