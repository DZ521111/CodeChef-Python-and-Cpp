# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:16:51 2020

@author: DHRUV
"""

import math as m

k = int(input())
for _ in range(int(input())):
    res1, res, sum_, total, half, need, ans, temp = "", "", 0, 0, 0, 0, [], 0
    n = int(input())
    if (k == 1):
        total = (n*(n+1))//2
        half = total//2
        roots = np.roots([1, 1, -2*half])
        i = m.ceil(roots[-1].real)
        sum_ = total - ((i*(i+1))//2)
        if (sum_ >= half):
            need = 0
        else:
            need = half - sum_
            sum_ += need
        res1 = "1"*(n-i)
        if (need == 0):
            res0 = "0"*(i)
        else:
            res0 = "0"*(need-1)
            res0 += "1"
            res0 += "0"*(i-need)
        res = res0 + res1
        diff = abs((total - sum_) - sum_)
        print(diff)
        print(res)