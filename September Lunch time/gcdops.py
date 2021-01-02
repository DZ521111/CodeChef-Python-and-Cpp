'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    B = list(map(int, input().split()))
    flag = True
    for __ in range(n):
        if ((__ + 1) % B[__]):
            print("NO")
            flag = False
            break
    if(flag):
        print("YES")