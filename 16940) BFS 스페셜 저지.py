"""
set 이용해서 맞는지 비교해나가면?
먼저 방문한 노드에 연결된 노드들 중에서는 순서가 어떻든 상관없으니까
set(연결된 노드들)-set(주어진 루트에서 방문한 노드들) 했을 때 공집합이 남아야 함

set끼리 차집합 구했을 때 이미 방문했던 노드가 남아버리면 안 되니까 단방향 그래프처럼 생각하면 되겠다

중요!
1 3 2 순으로 방문했으면 2의 자식보다 3의 자식을 더 먼저 방문해야 함
"""
# 미완성!!!


import sys, collections
READ = sys.stdin.readline

N = int(READ())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    n1, n2 = map(int, READ().split())
    graph[n1].append(n2)

route = collections.deque(map(int, READ().split()))
nodes = set(range(1, N+1))

res = 1
while route:
    front = route[0]  # 방문한 노드 계속 왼쪽에서 빼버리고 항상 0번만 보려고 큐 사용
    route.popleft()

    connected = graph[front]  # front에 연결된 노드 전부
    LEN = len(connected)

    route_slice = list(route)[:LEN]

    if set(connected) - set(route_slice):  # 공집합 아니라는 건 잘못 방문했다는 거지
        res = 0
        break


print(res)

"""
7
1 2
1 3
2 4
2 5
3 6
3 7
1 3 2 4 5 6 7

10
1 2
2 3
2 4
3 5
1 7
7 10
6 8
6 9
1 6
1 7 6 2 10 9 8 4 3 5

"""