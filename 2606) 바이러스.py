import sys
from collections import deque

def bfs(n):    
    q = deque()
    q.append(n)
    visited[n] = True
    cnt = 0
    while q:
        front = q[0]
        q.popleft()
        
        for node in graph[front]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                cnt += 1
                
    return cnt

N = int(sys.stdin.readline())
connected = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(connected):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

res = bfs(1)
print(res)
