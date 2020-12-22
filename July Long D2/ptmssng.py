'''
Author : Dhruv B Kakadiya
'''

from collections import Counter
for _ in range(int(input())):
    n = int(input())
    res = []
    x = [0] * (4*n - 1)
    y = [0] * (4*n - 1)
    for i in range(4*n - 1):
        x[i], y[i] = map(int,input().split())
    counter1 = Counter(x)
    counter2 = Counter(y)
    for k,v in counter1.items():
        if v % 2 == 1:
            res.append(k)
    for k,v in counter2.items():
        if v % 2 == 1:
            res.append(k)
    print(*res)