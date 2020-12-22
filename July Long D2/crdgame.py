'''
Author : Dhruv B Kakadiya
'''

# cook your dish here
for _ in range(int(input())):
    rounds = int(input())
    chef_p, morty_p = 0, 0
    for i in range(rounds):
        chef, morty = input().split()
        a = sum(list(map(int, chef)))
        b = sum(list(map(int, morty)))
        if (a == b):
            chef_p += 1
            morty_p += 1
        elif (a > b):
            chef_p += 1
        else:
            morty_p += 1
    else:
        if (chef_p > morty_p):
            print(0, chef_p)
        elif (chef_p < morty_p):
            print(1, morty_p)
        else:
            print(2, chef_p)