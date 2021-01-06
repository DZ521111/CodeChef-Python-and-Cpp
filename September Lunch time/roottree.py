'''
Author : Dhruv B Kakadiya

'''

for _ in range(int(input())):
    n = int(input())
    lst, set1, set2 = [], set(), set()
    for __ in range(n - 1):
        lst.append(list(map(int, input().split())))
        set1.add(lst[__][0])
        set2.add(lst[__][1])
    set1 = set1.difference(set2)
    print(len(set1) - 1)