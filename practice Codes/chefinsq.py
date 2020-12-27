'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int,input().split()))
    l.sort()
    e = l[k-1]
    l1 = l[k:]
    n = l.count(e)
    r = n-l1.count(e)
    c = math.factorial(n) // (math.factorial(r)*math.factorial(n-r))
    print(c)