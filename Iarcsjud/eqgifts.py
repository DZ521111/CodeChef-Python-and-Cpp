'''
Author : Dhruv B Kakadiya

'''

t=int(input())
l=[]
for i in range(t):
    a,b=map(int,input().split())
    l.append(abs(a-b))
    l.sort()
while len(l)>1:
    l[-2]-=l[-1]
    l.pop()
    l[-1]=abs(l[-1])
    l.sort()
print(l[0])
