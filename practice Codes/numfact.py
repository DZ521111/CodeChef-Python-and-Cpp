import atexit
import io
import sys
import math
from collections import defaultdict,Counter

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
def factor(n):
    s=d.setdefault(2,0)
    while n%2==0:
        d[2]+=1
        n//=2
    for j in range(3,int(math.sqrt(n)+1),2):
        if n%j==0:
            s=d.setdefault(j,0)
    
            while n%j==0:
                d[j]+=1
                n//=j
    if n>2:
        s=d.setdefault(n,0)
        d[n]+=1
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for j in a:
        factor(j)
    p=1
    for j in d:
        p*=(d[j]+1)
    print(p)

