import sys
from collections import deque

def bfs(r,c):
    global dist
    q = deque()
    dist[r][c] = 1
    q.append((r,c))

    while q:
        front = q[0]
        row = front[0]
        col = front[1]
        q.popleft()

        for i in range(4):
            nextrow = row + drow[i]
            nextcol = col + dcol[i]

            if nextrow >= H or nextcol >= W or nextrow < 0 or nextcol <0: continue

            if dist[nextrow][nextcol] == 0 and maze[nextrow][nextcol] == 1:
                dist[nextrow][nextcol] = dist[row][col] + 1
                # 상하좌우로 한칸씩 간 곳의 dist는 전부 같아야 함
                q.append((nextrow,nextcol))

    return dist[H-1][W-1]

dcol = (1, 0, -1, 0)
drow = (0, 1, 0, -1)

H, W = map(int, sys.stdin.readline().split())
maze = [[] for _ in range(H)]
dist = [[0]*W for _ in range(H)]
shortest = 0

for i in range(H):
    maze[i] = list(map(int, list(sys.stdin.readline()[:-1])))

for i in range(H):
    for j in range(W):
        if dist[i][j] == 0 and maze[i][j] == 1:
            shortest = bfs(i,j)

print(shortest)
