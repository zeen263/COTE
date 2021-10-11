"""
위상 정렬인데 부가조건이 있어서 답이 한 가지만 나온다!
쉬운 문제부터 먼저 풀 것 > 우선순위 큐를 써서 작은 값부터 pop
"""

import sys, heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
heap = []

for i in range(M):
    from_, to_ = map(int, sys.stdin.readline().split())
    graph[from_].append(to_)
    indegree[to_] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)  # 간선 수가 0인 노드 번호를 집어넣는다

while heap:
    front = heap[0]
    heapq.heappop(heap)

    for node in graph[front]:
        indegree[node] -= 1

        if indegree[node] == 0:
            heapq.heappush(heap, node)

    print(front, end=' ')

