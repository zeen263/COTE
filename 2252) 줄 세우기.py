"""
위상 정렬

연결 관계 그래프와 노드별 indegree 정보를 따로 저장하기
indegree가 0인 놈들을 찾아서 큐에 넣는다

큐에서 하나씩 꺼내서 그놈과 다른 노드를 연결하는 간선 전부 삭제
해당 작업으로 인해 indegree가 0이 된 놈을 큐에 넣는다
큐가 빌 때까지 반복
"""

import sys, collections

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for i in range(M):
    from_, to_ = map(int, sys.stdin.readline().split())
    graph[from_].append(to_)  # 각 노드가 어떤 노드로 이어지는지
    indegree[to_] += 1  # 각 노드로 들어오는 간선 수

q = collections.deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    front = q[0]  # 노드 번호
    q.popleft()

    for node in graph[front]:
        indegree[node] -= 1  # 큐에서 꺼낸 노드에 연결된 놈들의 간선 제거
        if indegree[node] == 0:  # 진입차수 0 되면 큐에 넣어
            q.append(node)

    print(front, end=' ')