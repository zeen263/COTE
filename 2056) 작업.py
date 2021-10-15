"""
선행 작업이 여러 개라면 더 오래 걸리는 것 기준으로 후행작업 완료 시간을 계산해야 함
큐에 넣을 때 작업시간을 계산하지 말고 주변 노드를 훑어볼 때 작업시간을 미리 계산해두기
"""

import sys, collections

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
time_ = [0 for _ in range(N+1)]
time_completed = [0 for _ in range(N+1)]

for i in range(1, N+1):
    time_cur, num_prior, *priors = map(int, sys.stdin.readline().split())
    time_[i] = time_completed[i] =  time_cur
    indegree[i] = num_prior
    
    # 그래프 구성
    for work in priors:
        graph[work].append(i)

# indegree 체크
q = collections.deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    front = q[0]
    time_front = time_completed[front]
    q.popleft()
    
    # front에 연결된 노드 간선 하나 끊기
    for node in graph[front]:
        indegree[node] -= 1
        time_completed[node] = max(time_completed[node], time_front + time_[node])
        # 연결된 노드들의 작업시간 계산(선행작업 누적)
        # 선행작업이 여러 개라서 작업시간이 이미 계산된 경우에는 더 오래 걸리는 선행작업을 기준으로 완료시간 산정

        if indegree[node] == 0:
            q.append(node)

print(max(time_completed))