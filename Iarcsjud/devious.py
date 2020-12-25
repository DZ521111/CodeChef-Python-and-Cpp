'''
Author : Dhruv B Kakadiya

'''

su=[]
le={}
le[0]=-1
n=int(input())
t=int(input())
su.append(t)
le[t]=0
miz=False
mizmi=0
inmiz={}
suar=0,0
for i in range(1,n):
    t=su[-1]+int(input())
    su.append(t)
    if t in le:
        miz=True
        if mizmi<abs(le[t]+1-i):
            mizmi=abs(le[t]+1-i)
            suar=t,i
        #print(le[t]+2,i+1)
        #exit()
    else:
        le[t]=i

if miz:
    print(0)
    print(le[suar[0]]+2,suar[1]+1)
    exit()
su.sort()
mi=abs(max(su))
b=0
s=n-1
for i in range(1,n):
    if abs(su[i]-su[i-1])<=mi:
        if abs(su[i]-su[i-1])==mi:
            if abs(le[b]-le[s])<abs(le[su[i]]-le[su[i-1]]):
                mi=abs(su[i]-su[i-1])
                b=su[i]
                s=su[i-1]
        else:
            mi=abs(su[i]-su[i-1])
            b=su[i]
            s=su[i-1]
if b<s:
    t=b
    b=s
    s=t
if le[b]>le[s]:
    print(mi)
    print(le[s]+2,le[b]+1)
else:
    print(-mi)
    print(le[b]+2,le[s]+1)

