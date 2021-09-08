"""
주어진 순서대로 방문해 보고 그게 bfs로 방문해야 하는 경로와 일치하는지 검사

아니뭐가문제야
"""



import sys, collections, copy
READ = sys.stdin.readline

N = int(READ())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    n1, n2 = map(int, READ().split())
    graph[n1].append(n2)


route = list(map(int, READ().split()))
tmp = str(route)
q = collections.deque()

q.append(route.pop(0))
res = 1

while q:
    node = q[0]  # 현재 노드
    q.popleft()

    connected = graph[node]  # 현재 노드에 연결된 노드 전부
    LEN = len(connected)
    visit_route = route[:LEN]  # 주어진 경로에서 방문한 순서

    if not route:
        break

    elif set(connected) - set(visit_route):  # 공집합 아니라는 건 잘못 방문했다는 거지
        res = 0
        break

    else:
        for i in range(LEN):
            q.append(route.pop(0))

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
res : 0

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
res : 1

10
1 4
1 2
4 3
3 9
3 8
2 6
6 7
2 5
5 10
1 4 2 3 6 5 9 8 7 10
res : 1

10
1 4
1 2
4 3
3 9
3 8
2 6
6 7
2 5
5 10
1 4 2 6 5 3 9 8 7 10
res : 0

7
3 1
3 2
1 4
1 5
2 6
6 7
3 2 1 6 4 5 7
res : 1

12
3 1
3 2
1 6
1 7
6 9
6 10
10 12
2 4
4 5
4 8
8 11
3 1 2 6 7 4 9 10 5 8 12 11
res : 1

12
3 1
3 2
1 6
1 7
6 9
6 10
10 12
2 4
4 5
4 8
8 11
3 2 1 7 6 4 9 10 5 8 12 11
res : 0

14
1 2
1 4
1 11
2 3
3 5
3 13
4 6
4 8
6 7
8 9
8 10
11 12
11 14
1 11 2 4 12 14 3 6 8 5 13 7 10 9
res : 1

14
1 2
1 4
1 11
2 3
3 5
3 13
4 6
4 8
6 7
8 9
8 10
11 12
11 14
1 11 2 4 12 14 3 6 8 5 13 7 9 10
res : 1
"""