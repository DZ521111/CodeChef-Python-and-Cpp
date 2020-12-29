'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split()]
    x, y, s = [int(x) for x in input().split()]
    if x>0:
        xarr = [int(x) for x in input().split()]
    else:
        xarr=[]
    xarr.append(n+1)
    xarr.insert(0,0)
    if y>0:
        yarr = [int(x) for x in input().split()]
    else:
        yarr=[]
    yarr.append(m+1)
    yarr.insert(0,0)
    X = 0
    for j in range(1,x+2):
        a = xarr[j] - xarr[j-1] - 1
        if a>=s:
            X += a//s
    Y = 0
    for j in range(1,y+2):
        a = yarr[j] - yarr[j-1] - 1
        if a>=s:
            Y += a//s
    print(X*Y)