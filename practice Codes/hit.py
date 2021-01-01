'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
try:
    for t in range(int(input())):
        n = int(input())
        l = list(map(int,input().split()))
        l.sort()
        x = n // 4
        a = l[x * 1]
        b = l[x * 2]
        c = l[x * 3]
        if l.index(a) != x or l.index(b) - l.index(a) != x or l.index(c) - l.index(b) != x or n-l.index(c) != x:
            print(-1)
        else:
            print(a, b, c)
except:
    pass