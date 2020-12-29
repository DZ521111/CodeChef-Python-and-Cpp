'''
Author : Dhruv B Kakadiya

'''

tt = int(input())
while tt:
    s = input()
    if len(s) == 1:
        print('YES')
    else:
        l = list(s)
        res_l = []
        for i in range(len(l)):
            res_l.append(l[i - 1])
        res_r = l[1 : ]
        res_r.append(l[0])
        if res_l == res_r:
            print('YES')
        else:
            print('NO')
    tt = tt - 1