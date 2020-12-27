'''
Author : Dhruv B Kakadiya

'''

t = int(input())
while t:
    s = input()
    if len(s) == 1:
        print('YES')
    else:
        l = list(s)
        res_l=[]
        for i in range(len(l)):
            res_l.append(l[i-1])
        res_r = l[1:]
        res_r.append(l[0])
        if res_l == res_r:
            print('YES')
        else:
            print('NO')
    t = t-1