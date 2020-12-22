'''
Author : Dhruv B Kakadiya
'''

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    strings = list(map(int, input().split()))
    sum_ = 0
    i = 1
    while (i < n):
        sum_ += (abs(strings[i] - strings[i-1]) - 1)
        i += 1
    print(sum_)