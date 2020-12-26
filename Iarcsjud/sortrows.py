'''
Author : Dhruv B Kakadiya

'''

n=int(input())
l=[]
for _ in range(n):
    m=list(map(int,input().split()))
    l.append(m)

l.sort()
for i in range(n):
    l[i].remove(-1)
for i in range(n):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
    print()