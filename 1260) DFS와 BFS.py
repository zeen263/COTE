import sys
from collections import deque

def dfs(n):
    visited[n] = True
    print(n, end=' ')

    for node in graph[n]: # 1번 정점에 연결된 정점들을 방문
        if not visited[node]: # 방문 안 했으면
            dfs(node)


def bfs(n):
    que = deque()
    visited[n] = True
    print(n, end=' ')
    que.append(n)

    while que:
        front = que[0]
        que.popleft()

        for node in graph[front]:
            if not visited[node]:
                visited[node] = True
                print(node, end=' ')
                que.append(node)


N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for x in range(N+1)]
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for nodes in graph: # 작은 숫자부터 방문하기 위해 정렬
    nodes.sort()


visited = [False for x in range(N+1)]
dfs(V)
print()
visited = [False for x in range(N+1)]
bfs(V)

