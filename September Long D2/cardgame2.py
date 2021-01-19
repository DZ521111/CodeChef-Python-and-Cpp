# cook your dish here
mod = 1000000007
def find_power(a, n):
    res = 1
    while(n):
        if (n & 1):
            res = (res * a % mod)
        n = n//2
        a = (a**2) % mod
    return res

def find_div(x, y):
    temp = (x % mod * (find_power(y, mod - 2) % mod)) % mod
    return temp

def temporary(n, k):
    ans = 1
    r = min(k, n - k)
    for i in range(r):
        ans = ((ans % mod) * (n - i) % mod) % mod
        ans = find_div(ans, i + 1)
    return (ans % mod)
    
for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    max_, all_max = 0, 0
    for i in range(n):
        if (max_ < num[i]):
            max_ = num[i]
    for i in range(n):
        if (max_ == num[i]):
            all_max += 1
    if (n == 1):
        print(2)
        continue
    if (all_max % 2 != 0):
        ans = find_power(2, n) % mod
    else:
        sol = (find_power(2, n) % mod) - ((find_power(2, n - all_max) % mod) * temporary(all_max, all_max // 2) % mod) % mod
        ans = sol
    if (ans < 0):
        ans = (ans + mod) % mod
    print(ans % mod)





