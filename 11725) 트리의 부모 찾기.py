import sys
from collections import deque

def bfs(n):
    parent = [0 for _ in range(N+1)]

    q = deque()
    q.append(n)

    while q:
        front = q[0]
        q.popleft()

        for node in tree[front]:
            if not visited[node]:
                visited[node] = True
                parent[node] = front
                q.append(node)

    return parent


N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(1,N):
    n1, n2 = map(int, sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

res = bfs(1)
for i in range(2,N+1):
    print(res[i])