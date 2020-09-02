import sys
from collections import deque
sys.setrecursionlimit(10**8)

def bfs(n):
    que = deque()
    que.append(n)
    visited[n] = True

    while que:
        front = que[0]
        que.popleft()

        for node in graph[front]:
            if not visited[node]:
                visited[node] = True
                que.append(node)

def bfscheck():
    cnt = 0
    for i in range(1,len(graph)):
        if not visited[i]:
            cnt+=1
            bfs(i)
    return cnt



V, E = map(int, sys.stdin.readline().split())
graph = [[] for x in range(V+1)]
visited = [False for x in range(V+1)]

for i in range(1,E+1):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for nodes in graph:
    nodes.sort()

res = bfscheck()
print(res)