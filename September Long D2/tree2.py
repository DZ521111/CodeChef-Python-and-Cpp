# cook your dish here
for _ in range(int(input())):
    n = int(input())
    sticks = list(map(int, input().split()))
    if (0 in sticks):
        print(len(set(sticks)) - 1)
    else:
        print(len(set(sticks)))