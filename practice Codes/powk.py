'''
Author : Dhruv B Kakadiya

'''

from collections import defaultdict as dd,deque
t = int(input())
while (t):
    pres = dd(int)
    d = dd(list)
    n = int(input())
    m = int(input())
    ind = dd(int)
    for i in range(m):
        u, v = input().split()
        if(pres[(u,v)] == 0):
            d[u].append(v)
            pres[(u,v)] == 1
            ind[v] += 1
    q = deque([])
    for i in d:
        if(ind[i] == 0):
            q.append(i)
    res = deque()
    while q:
        a = q.pop()
        res.appendleft(a)
        for i in d[a]:
            ind[i] -= 1
            if(ind[i] == 0):
                q.appendleft(i)
    if(len(res) == n):
        print("YES")
        for i in res:
            print(i)
    else:
        print("NO")
    t -= 1