'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    if(sum(num) == 0):
        print("YES")
    else:
        if sum(num) >= 0:
            print("YES")
        else:
            print("NO")