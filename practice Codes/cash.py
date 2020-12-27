'''
Author : Dhruv B Kakadiya

'''
for _ in range(int(input())):
    n, k = map(int, input().split())
    coins = [int(x) for x in input().split()]
    sumc=0
    for i in coins:
        sumc += i % k
    print(sumc % k)