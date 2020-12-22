'''
Author : Dhruv B Kakadiya
'''

for _ in range(int(input())):
    no_of_population, cures = map(int,input().split())
    populations = list(map(int,input().split()))
    populations.sort()
    cure_country, days = 0, 0
    while(cure_country != no_of_population):
        days += 1
        if (populations[cure_country] - cures > 0):
            cures *= 2
        else:
            cures = max(2 * populations[cure_country], cures)
            cure_country += 1
    print(days)