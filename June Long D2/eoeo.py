'''
Author : Dhruv B Kakadiya
'''

for _ in range(int(input())):
    ts = int(input())
    temp = 0
    if(ts % 2 != 0):
        temp = ts // 2
    else:
        while((ts % 2 == 0) and ts > 1):
            ts //= 2
        temp = ts // 2
    print(temp)
