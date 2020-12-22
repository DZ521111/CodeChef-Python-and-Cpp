'''
Author : Dhruv B Kakadiya
'''

from collections import Counter, defaultdict
for _ in range(int(input())):
    n = int(input())
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))
    c1, c2 = Counter(seq1), defaultdict(int)
    temp1, temp2, flag1, flag2 = min(seq1), min(seq2), 0, 0
    temp_list1, temp_list2 = [], []
    cost = 0
    for i in seq2:
        if c1[i]:
            c1[i] -= 1
        else:
            c2[i] += 1
    min_ = min(temp1, temp2)
    for i in c1:
        if (c1[i] % 2 == 1):
            flag1 = 1
            print(-1)
            break
    if(flag1 == 1):
        continue
    for i in c2:
        if (c2[i] % 2 == 1):
            print(-1)
            flag2 = 1
            break
    if(flag2 == 1):
        continue
    for i in c1:
        if (c1[i] > 0):
            for _ in range(c1[i] // 2):
                temp_list1.append(i)
    for i in c2:
        if (c2[i] > 0):
            for _ in range(c2[i] // 2):
                temp_list2.append(i)
                
    if (len(temp_list1) != len(temp_list2)):
        print(-1)
    else:
        temp_list1.sort()
        temp_list2.sort(reverse = True)
        for i in range(len(temp_list1)):
            cost += min(temp_list1[i], temp_list2[i], 2 * min_)
        print(cost)