import sys
from collections import deque

def bfs(n):
    q = deque()
    visited[n] = True
    q.append(n)

    while q:
        front = q[0]
        q.popleft()

        # front가 1일 경우) permu[front]의 값(방문할 노드) 확인 > 그걸 방문한 적 있는지 확인
        nxt = permu[front]
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)


def cyclecheck(n):
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            cnt+=1
            bfs(i)
    return cnt


T = int(sys.stdin.readline())
for case in range(T):
    size = int(sys.stdin.readline())

    permu = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False for x in range(size+1)]


    print(cyclecheck(size))
