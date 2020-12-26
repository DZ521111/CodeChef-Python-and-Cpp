'''
Author : Dhruv B Kakadiya

'''

def dfs(v):
    visited.add(v)
    parents.append(v)
    for u in parents:
        desc[v][u] = True
    for u in graph[v]:
        if u not in visited:
            dfs(u)
            val[v] += val[u]
    parents.pop()


n = int(input())
cost,graph,val = {},{},{}
# val(i) is sum of cost of descendants of i
for i in range(1,n+1):
    cost[i] = int(input())
    graph[i] = []
    val[i] = cost[i]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

desc = [[False for i in range(n+1)] for i in range(n+1)]
# desc(i,j) is true if i is descendant of j
visited = set()
parents =[]   # Ancestors stack


dfs(1)
total = sum(cost.values())
best = float('inf')
for i in range(1,n):
    for j in range(i+1,n+1):
        split = 0
        s1 = val[i]
        s2 = val[j]
        if desc[i][j]:
            s2 -= val[i]
        if desc[j][i]:
            s1 -= val[j]
        s3 = total-s1-s2
        split = max(s1,s2,s3)
        best = min(best,split)
print(best)