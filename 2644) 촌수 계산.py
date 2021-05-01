import sys
from collections import deque

def bfs(n1, n2):
    q = deque()
    kin_degree[n1] = 0
    q.append(n1)

    while q:
        front = q[0]
        q.popleft()

        for node in graph[front]:
            if kin_degree[node] == -1:
                kin_degree[node] = kin_degree[front] + 1
                q.append(node)


    return kin_degree[n2]


N_people = int(sys.stdin.readline())
tgt1, tgt2 = map(int, sys.stdin.readline().split())
N_graph = int(sys.stdin.readline())

graph = [[] for _ in range(N_people+1)]
kin_degree = [-1 for _ in range(N_people+1)]  # 자기 자신은 0촌이라 0으로 초기화하면 안 됨
for i in range(N_graph):
    n1, n2 = map(int, sys.stdin.readline().split())

    graph[n1].append(n2)
    graph[n2].append(n1)


res = bfs(tgt1, tgt2)
print(res)

