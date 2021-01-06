'''
Author : Dhruv B Kakadiya

'''


from collections import deque
from sys import stdin, stdout
def II(): return int(stdin.readline())
def MI(): return map(int, stdin.readline().split())
def LI(): return list(map(int, stdin.readline().split()))

class tree:
    def __init__(self,V):
        self.nodes = V
        self.adj = [[] for i in range(V)]
        self.parent = [-1]*V
        self.level = [-1]*V

def addEdge(ta, v, w):
    ta.adj[v].append(w)
    ta.adj[w].append(v)

def BFS(ta, s):
    queue = deque([s])
    ta.level[s] = 0
    while queue:
        x = queue.popleft()
        for i in ta.adj[x]:
            if ta.level[i] == -1:
                ta.level[i] = ta.level[x] + 1
                ta.parent[i] = x
                queue.append(i)

def readUV():
    u, v = MI()
    u, v = u - 1, v - 1
    return u, v

def solve1(ta, a, b, aa):
    if ta.level[a] < ta.level[b]:
        a, b = b, a
    vals = set()
    while ta.level[b] != ta.level[a]:
        if aa[a] in vals:
            stdout.write("0\n")
            return
        vals.add(aa[a])
        a = ta.parent[a]
    while (b != a):
        if (aa[a] in vals):
            print(0)
            return
        vals.add(aa[a])
        if (aa[b] in vals):
            stdout.write("0\n")
            return
        vals.add(aa[b])
        a, b = ta.parent[a], ta.parent[b]

    if aa[a] in vals:
        stdout.write("0\n")
        return
    vals.add(aa[a])
    ans,x = 101,len(vals)
    vals = list(vals)
    vals.sort()
    for j in range(1, x):
        ans = min(ans, (vals[j] - vals[j - 1]))
        if ans == 1:
            break
    stdout.write(str(ans) + "\n")

def solve():
    t = II()
    for _ in range(t):
        n, q = MI()
        aa = LI()
        atree = tree(n)
        for i in range(n - 1):
            u,v = readUV()
            addEdge(atree, u, v)
        BFS(atree, 0)
        for i in range(q):
            a, b = readUV()
            solve1(atree, a, b, aa)

if __name__ == "__main__":
    solve()
