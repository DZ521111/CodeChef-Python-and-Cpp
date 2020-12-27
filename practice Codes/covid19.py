'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
t=int(input())
maxarr=[]
minarr=[]
for i in range(t):
    n=int(input())
    a=[int(i) for i in input().split() ]
    dist=[]
    max=0
    min=999999
    
    c=0
    for j in range(len(a)-1):
        if a[j+1]-a[j]<=2:
            c+=1
           
        else:
            if max<c:
                max=c
            if min>c:
                min=c
            c=0
            
    if max<c:
        max=c
    if min>c:
        min=c 
    maxarr.append(max+1)
    minarr.append(min+1)
for i in range(t):
    print(minarr[i],maxarr[i])