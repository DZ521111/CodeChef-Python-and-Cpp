'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
import random
import sys
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t, n, k = map(int,input().split())
for _ in range(t):
    for printinng in range(n):
        a = ''.join(random.choice(alpha) for iter in range(10))
        print(a, flush = True)
    score = int(input())