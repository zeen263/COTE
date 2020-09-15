import sys
from collections import deque

def bfs_groupping(r,c): # 그룹짓기
    global map_

    q = deque()
    q.append((r,c))


    while q:
        front = q[0]
        row = front[0]
        col = front[1]
        q.popleft()

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if nrow >= N or ncol >= N or nrow < 0 or ncol < 0: continue

            if map_[nrow][ncol] == 1 and not visited[nrow][ncol]:
                map_[nrow][ncol] = map_[row][col] #같은 색으로 칠하기
                visited[nrow][ncol] = True
                q.append((nrow,ncol))


def bfs_calcdist(q):
    global map_, dist
    ret = 999999
    while q:
        front = q[0]
        row = front[0]
        col = front[1]
        q.popleft()


        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if nrow >= N or ncol >= N or nrow < 0 or ncol < 0: continue

            if map_[nrow][ncol] == 0 and dist[nrow][ncol] == 0: #바다 건너기
                dist[nrow][ncol] = dist[row][col]+1  #거리 계산
                map_[nrow][ncol] = map_[row][col] #어떤 섬에서 출발했는지 표시
                q.append((nrow,ncol))

            if map_[nrow][ncol] != 0: #건너다가 땅(다리) 발견
                if map_[nrow][ncol] != map_[row][col]: #각각 다른 섬에서부터 뻗어나온 다리라면
                    distance = dist[nrow][ncol] + dist[row][col]
                    ret = min(ret,distance) #찾은 다리가 최소가 아닐 수도 있다

    return ret





drow = (1,0,-1,0)
dcol = (0,1,0,-1)

N = int(sys.stdin.readline())
map_ = [[] for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dist = [[0]*N for _ in range(N)]


for i in range(N):
    map_[i] = list(map(int,sys.stdin.readline().split()))

cnt = 1
for i in range(N):
    for j in range(N):
        if map_[i][j] == 1 and not visited[i][j]:
            map_[i][j] = cnt
            visited[i][j] = True
            bfs_groupping(i,j)
            cnt += 1


que = deque()
for i in range(N):
    for j in range(N):
        if map_[i][j] != 0 and dist[i][j] == 0:
            que.append((i,j))

mindist = bfs_calcdist(que)

print(mindist)

