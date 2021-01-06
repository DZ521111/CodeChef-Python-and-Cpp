'''
Author : Dhruv B Kakadiya

'''
# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    newa = list(set(a))
    if len(newa) == 1:
        print(newa[0] * 2)
    elif len(newa) == 2:
        print(sum(newa))
    else:
        newa.sort()
        m1 = newa.pop()
        m2 = newa.pop()
        gcd = newa[0]
        for i in range(1, len(newa)):
            gcd = math.gcd(gcd, newa[i])
            if gcd == 1:
                break
        s1 = math.gcd(gcd, m1)
        s2 = math.gcd(gcd, m2)
        print(max(s1 + m2, s2 + m1))