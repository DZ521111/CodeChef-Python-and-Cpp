'''
Author : Dhruv B Kakadiya

'''

for _ in range(int(input())):
    n, minx, maxx = map(int, input().split())
    odd = (maxx - minx) // 2
    if(maxx % 2 != 0 or minx % 2 != 0):
        odd += 1
    even = (maxx - minx + 1) - odd
    for i in range(n):
        w, b = map(int, input().split())
        if(w % 2 == 0 and b % 2 == 0):
            even = even + odd
            odd = 0
        elif(w % 2 == 0 and b % 2 != 0):
            odd = odd + even
            even = 0
        elif(w % 2 != 0 and b % 2 != 0):
            even, odd = odd, even
    print(even, odd)