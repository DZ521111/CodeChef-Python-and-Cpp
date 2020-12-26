'''
Author : Dhruv B Kakadiya

'''

# cook your dish here
from queue import PriorityQueue


def getpenal(par, cld, direc):
    penal = 0
    if direc == 'goup':
        brid = cld[2]
        i1 = par.index(brid)
        penal += (4-i1) % 4
    elif direc == 'godown':
        brid = cld[0]
        i1 = par.index(brid)
        penal += (2+4-i1) % 4
    elif direc == 'goleft':
        brid = cld[1]
        i1 = par.index(brid)
        penal += (3+4-i1) % 4
    elif direc == 'goright':
        brid = cld[3]
        i1 = par.index(brid)
        penal += (1+4-i1) % 4
    return penal



m, n = map(int, input().split())
col2int = {'R': 0, 'G': 1, 'B': 2, 'Y': 3}
# direc2int = {'goup':0, 'godown':1, 'goleft':2, 'goright':3}
l = [[[] for _ in range(n)] for _ in range(m)]
for j in range(m):
    for i in range(n):
        l[j][i] = list(map(lambda x: col2int[x], input().split()))

# visited = 0
dp = [[float('inf') for _ in range(n)] for _ in range(m)]
q = PriorityQueue()
# n_visited = 0
q.put((0, (0, 0)))
while q.qsize() > 0:
    penal, pos= q.get()
    y, x = pos
    orien = l[y][x]
    # print(pos)

    # n_visited = [list(l) for l in visited]
    # n_visited[y][x] = True
    # n_visited ^= (1<<ravel(x, y))
    # dp[y][x] = min(dp[y][x], penal)

    if y - 1 >= 0:# and ((n_visited >> ravel(x, y-1)) & 1 == 0):
        penal1 = getpenal(orien, l[y - 1][x], 'goup')
        penal1 += penal
        if penal1 < dp[y - 1][x]:
            dp[y - 1][x] = penal1
            q.put((penal1, (y - 1, x)))
        # penal_l, n_orien_l = getpenalorien([y - 1, x], 'goup')
        # for penal1, n_orien in zip(penal_l, n_orien_l):
        #     q.put((penal1, n_orien, (y - 1, x), n_visited))

    if x-1 >= 0:# and ((n_visited >> ravel(x-1, y)) & 1 == 0):
        penal1 = getpenal(orien, l[y][x - 1], 'goleft')
        penal1 += penal
        if penal1 < dp[y][x - 1]:
            dp[y][x-1] = penal1
            q.put((penal1, (y, x - 1)))
        
        # penal_l, n_orien_l = getpenalorien([y, x-1], 'goleft')
        # for penal1, n_orien in zip(penal_l, n_orien_l):
        #     q.put((penal1, n_orien, (y, x - 1), n_visited))

    if y+1 < m:# and ((n_visited >> ravel(x, y+1)) & 1 == 0):
        penal1 = getpenal(orien, l[y+1][x], 'godown')
        penal1 += penal
        if penal1 < dp[y + 1][x]:
            dp[y + 1][x] = penal1
            q.put((penal1, (y+1, x)))
        # penal_l, n_orien_l = getpenalorien([y+1, x], 'godown')
        # for penal1, n_orien in zip(penal_l, n_orien_l):
        #     q.put((penal1, n_orien, (y + 1, x), n_visited))

    if x+1 < n:# and ((n_visited >> ravel(x+1, y)) & 1 == 0):
        penal1 = getpenal(orien, l[y][x+1], 'goright')
        penal1 += penal
        if penal1 < dp[y][x+1]:
            dp[y][x+1] = penal1
            q.put((penal1, (y, x+1)))
        # penal_l, n_orien_l = getpenalorien([y, x+1], 'goright')
        # for penal1, n_orien in zip(penal_l, n_orien_l):
        #     q.put((penal1, n_orien, (y, x + 1), n_visited))

print(dp[-1][-1])
# print(dp)
