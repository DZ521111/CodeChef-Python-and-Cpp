'''
Author : Dhruv B Kakadiya

'''

for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if min(arr) == m:
        print(n - arr.count(m))
        continue
    temp = min(arr)
    flg = 0
    arrkaset = set(arr)
    for i in range(temp, m):
        if i in arrkaset:
            pass
        else:
            flg = 1
            break
    if flg == 1:
        print(-1)
    else:
        print(n - arr.count(m))