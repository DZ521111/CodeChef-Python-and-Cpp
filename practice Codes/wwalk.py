'''
Author : Dhruv B Kakadiya

'''
# cook your dish here
for _ in range(int(input())):
    temp = int(input())
    Alice = list(map(int, input().split()))
    Bob = list(map(int, input().split()))
    tot_Alice = 0
    tot_Bob = 0
    total = []
    for j, k in zip(Alice, Bob):
        if (tot_Alice == tot_Bob) and (j == k):
            total.append(j)
            tot_Alice += j
            tot_Bob += k
        else:
            tot_Alice += j
            tot_Bob += k
    print(sum(total))