import sys
from collections import deque

# 배열에서 i가 세로 j가 가로 >> visited[y][x]가 맞음
def bfs(y,x):
    q = deque()
    visited[y][x] = True
    house = 0
    q.append((y,x))

    while q:
        house += 1
        front = q[0] # 현재 위치한 노드
        curY = front[0] # 의 x좌표
        curX = front[1] #    y좌표
        q.popleft()

        for i in range(4): # 4방향으로 다음에 갈 노드를 탐색
            nextY = curY + dy[i]
            nextX = curX + dx[i]

            if nextX >= N or nextY >= N or nextX < 0 or nextY < 0: continue  # 범위 벗어나는 경우

            if map_[nextY][nextX] == 1 and not visited[nextY][nextX]: # 다음에 갈 노드가 집이 있고 방문한 적 없는 노드라면
                visited[nextY][nextX] = True
                q.append((nextY,nextX))

    return house


N = int(sys.stdin.readline())
map_ = [[] for x in range(N)]
visited = [[] for x in range(N)]
blocks = []
dx = (1, 0, -1, 0) #cw
dy = (0, 1, 0, -1)

for i in range(N):
    line = sys.stdin.readline()[:-1]
    map_[i] = list(map(int, line))
    visited[i] = [False for x in range(N)]

# i가 세로 j가 가로
for i in range(N):
    for j in range(N):
        if map_[i][j] == 1 and not visited[i][j]:
            blocks.append(bfs(i,j))

blocks.sort()
print(len(blocks))
for house in blocks:
    print(house)