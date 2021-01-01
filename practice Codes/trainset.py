'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
for i1 in range(int(input())):
    se = set()
    li = []
    di1 = {}
    di0 = {}
    c = 0
    n = int(input())
    for i in range(n):
        s = input().split()
        if(s[1] == '1'):
            if(s[0] not in di1.keys()):
                di1[s[0]] = 1
            else:
                di1[s[0]] = di1[s[0]] + 1
        if(s[1] == '0'):
            if(s[0] not in di0.keys()):
                di0[s[0]] = 1
            else:
                di0[s[0]] = di0[s[0]] + 1
    for i in di0.keys():
        if i not in di1.keys():
            di1[i] = 0
        c = c + max(di0[i], di1[i])
        di0[i] = 0
        di1[i] = 0
    for i in di1.keys():
        if i not in di0.keys():
            di0[i] = 0
        c = c + max(di0[i], di1[i])
    print(c)