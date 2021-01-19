"""
Created on Thu Sep 10 18:44:28 2020

@author: DHRUV
"""

def find_xor(n):
    ans, lst = 0, []
    for i in range(1, 21):
        print(1, 2**i, flush=True)
        x = int(input())
        lst.append(x)
    lst.reverse()
    sum_ = lst[0] - n*(2**len(lst))
    for i in range(1, len(lst)):
        if (lst[i] >= sum_):
            lst[i] = ((n - (lst[i]-sum_)/(2**(len(lst)-i)))/2)
        else:
            lst[i] = (n + (sum_-lst[i])/(2**(len(lst)-i)))/2
    for i in range(1, len(lst)):
        if (lst[i]%2 != 0):
            ans += 2**(len(lst)-i)
    if (sum_%2!=0):
        ans += 1
    print(2, ans, flush=True)
    res = int(input())
    return res

for _ in range(int(input())):
    n = int(input())
    if (not find_xor(n)):
        break
    print(flush=True)