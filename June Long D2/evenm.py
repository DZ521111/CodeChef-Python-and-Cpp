'''
Author : Dhruv B Kakadiya
'''

def spiralFill(m, n, a): 
    val = 1
    k, l = 0, 0
    while (k < m and l < n): 
  
        for i in range(l, n): 
            a[k][i] = val 
            val += 1
        k += 1
  
        for i in range(k, m): 
            a[i][n - 1] = val 
            val += 1
        n -= 1

        if (k < m): 
            for i in range(n - 1, l - 1, -1): 
                a[m - 1][i] = val 
                val += 1
            m -= 1
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                a[i][l] = val 
                val += 1
            l += 1 

for _ in range(int(input())):
    n = int(input())
    a = [[0 for j in range(n)] for i in range(n)] 
    spiralFill(n, n, a) 
    for i in range(n): 
        for j in range(n): 
            print(a[i][j], end=' ') 
        print('')