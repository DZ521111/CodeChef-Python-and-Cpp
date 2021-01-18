'''
Author : Dhruv B Kakadiya

'''

for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    take = []
    for i in range(len(num)):
        countL, countR = 0, 0
        tempL, tempR = num[ : i + 1], num[i + 1 : ]
        countL = sum(x > num[i] for x in tempL)
        countR = sum(y < num[i] for y in tempR)
        take.append(countR + countL + 1)
    if (n == 3):
        print(min(take), max(take))
    elif (n == 4):
        print(min(take) + 1, max(take))
    else:
        print(min(take) + 1, max(take))