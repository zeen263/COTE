import sys
from collections import deque, defaultdict



def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True
    timeCnt[n] = 0
    
    while q:
        front = q[0]
        q.popleft()
        dpos = (front-1, front+1, 2*front) # 수빈이의 다음 위치로 가능한 지점들

        if front == K:
            return timeCnt[front]
        
        for pos in dpos:
            if pos >= 0 and pos <= 100000 and visited[pos] == False:
                visited[pos] = True
                q.append(pos)
                timeCnt[pos] = timeCnt[front] + 1


N,K = map(int, sys.stdin.readline().split())
visited = defaultdict(bool)
timeCnt = defaultdict(int)
res = bfs(N)
print(res)
