'''
Author : Dhruv B kakadiya

'''

# cook your dish here
T=int(input())
for T in range(1,T+1):
    N=int(input())
    S=[None]*N
    for i in range(N):
        S[i]=input()
    for i in range(N-1):
        s=int(str(S[i]),2)^int(str(S[i+1]),2)
        s='{0:b}'.format(s)
        S[i+1]=s

    count=0
    for s in S[N-1]:
        if (s=='1'):
            count=count+1
    print(count)