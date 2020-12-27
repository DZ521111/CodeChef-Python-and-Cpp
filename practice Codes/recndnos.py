'''
Author : Dhruv B Kakadiya

'''

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    for i in range(n-1):
        if A[i] == A[i+1]:
            A[i+1] = 'x'
    y = A[0]
    count = A.count(A[0])
    for j in range(n):
        if A[j] != 'x':
            temp = A.count(A[j])
            if temp > count:
                count = temp
                y = A[j]
            elif temp == count:
                count = temp
                if y > A[j]:
                    y = A[j]
    print(y)