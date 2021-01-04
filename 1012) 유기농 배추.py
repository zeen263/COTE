import sys
from collections import deque

def bfs(pos):
    global visited
    
    q = deque()
    q.append(pos)
    visited[pos[0]][pos[1]] = True

    dr = (0, -1, 0, 1)
    dc = (1, 0, -1, 0)

    while q:
        front = q[0]
        q.popleft()
        
        row = front[0]
        col = front[1]
        
        for i in range(4):
            nextR = row + dr[i]
            nextC = col + dc[i]

            if 0 <= nextR and nextR < N and 0 <= nextC and nextC < M:
                if not visited[nextR][nextC] and farm[nextR][nextC] == 1:
                    visited[nextR][nextC] = True
                    q.append((nextR, nextC))



T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # 배추밭 : N x M  배추 수 : K
    farm = [[0]*M for __ in range(N)]
    visited = [[False]*M for __ in range(N)]
    cabbages = [() for __ in range(K)]
    
    for i in range(K):
        c,r = map(int, sys.stdin.readline().split()) # 입력에서 c,r 뒤집어서 줌
        farm[r][c] = 1
        cabbages[i] = (r,c)

    worm = 0
    for (r,c) in cabbages:
        if not visited[r][c]:
            worm += 1
            bfs((r,c))
            
    print(worm)
