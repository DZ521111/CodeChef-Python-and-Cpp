'''
Author : Dhruv B Kakadiya

'''

from sys import stdin, stdout
from math import ceil


def solve():
    twopow = {}
    for i in range(34):
        twopow[i] = pow(2, i)

    for _ in range(int(input())):
        n = int(stdin.readline())
        ans = (n-1)//2
        if not n & (n - 1):
            print(-1)
            continue

        i = 2
        while i < n:
            ans += ((n - i) // (2 * i) + 1) * i
            i <<= 1
        print(ans)


if __name__ == "__main__":
    solve()
