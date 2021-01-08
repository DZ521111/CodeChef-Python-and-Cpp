'''
Author : Dhruv B Kakadiya

'''


import atexit
import io
import sys
import math

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
def factor(n):
    while (n % 2 == 0):
        d[2] += 1
        n //= 2
    for j in range(3, int(math.sqrt(n) + 1), 2):
        if (n % j == 0):
            while (n % j == 0):
                d[j] += 1
                n //= j
    if (n > 2):
        d[n] += 1

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for j in a:
        factor(j)
    p = 1
    for j in d:
        p *= (d[j] + 1)
    print(p)

