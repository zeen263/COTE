import sys
import collections


def bfs(n):
    q = collections.deque()
    q.append(n)
    
    group[n] = n
    dist[n] = 1

    while q:
        front = q[0]
        q.popleft()

        nextnode = graph[front]
        # nextnode : 내가 다음에 방문하려는 노드

        if dist[nextnode] == 0:  # 아직 방문하지 않은 노드
            dist[nextnode] = dist[front] + 1  # 방문 순서
            group[nextnode] = group[front]  # 이번 사이클에 방문하는 노드들을 같은 그룹으로 묶기
            q.append(nextnode)

        else: #다음에 방문할 노드가 방문한 적 있다!
            if group[nextnode] == group[front]: #이번 사이클에서 방문한 거라면
                return dist[nextnode]-1 #다음 노드-1명만큼? 팀이 없다

            else: #옛날에 방문한 거라면
                return dist[front] #현재 노드부터 팀이 없다


def bfsall():
    noTeam = 0
    for i in range(1, N+1):
        if dist[i] == 0:
            noTeam += bfs(i)

    return noTeam


T = int(sys.stdin.readline())
for case in range(T):
    N = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    dist = [0 for x in range(N + 1)]
    group = [False for x in range(N + 1)]

    print(bfsall())


