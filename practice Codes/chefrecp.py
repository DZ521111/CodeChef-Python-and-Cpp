'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
from copy import deepcopy
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    dict111={}
    answer=1
    current=0
    for i in a :
        if(i==current):
            dict111[i]+=1
        elif i not in dict111:
            dict111[i]=1
            current = i
        else:
            answer=0
            break
    if(answer==0):
        print("NO")
    else:
        b1=[]
        for i in dict111:
            if dict111[i] not in b1:
                b1.append(dict111[i])
            else:
                print("NO")
                break
        else:  
            print("YES")      