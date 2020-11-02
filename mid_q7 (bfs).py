from collections import deque
from time import sleep


# 20x10 맵의 1,1에서 18,8까지 이동
# 1은 벽이고 0은 길, 2는 이동한 자취
# 선택지가 여러 개 생기면 랜덤하게 이동하도록 함
# 직선으로 이동하면 거리가 1, 대각선으로 이동하면 거리가 1.414
# 최단거리 구하기


def display():
    for i in range(10):
        for j in range(20):
            print('%5s' % str(round(maze[i][j], 1)), end=' ')
        print()
    print()
    print()
    sleep(2.5)


maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(10):
    for j in range(20):
        if maze[i][j] == 1:
            maze[i][j] = -1  # 거리 계산을 위해 벽을 임의로 -1로 바꿈

drow = (1, 1, 0, -1, -1, -1, 0, 1)
dcol = (0, -1, -1, -1, 0, 1, 1, 1)
dist = (1, 1.414, 1, 1.414, 1, 1.414, 1, 1.414)

# 해당 위치까지 도달하는 데 걸린 거리를 미로 맵에 저장해두고 최단거리만 남긴다
# nextr, nextc = 다음에 갈 곳의 인덱스
# row, col = 현재 로봇의 위치
row = 1;
col = 1
q = deque()
q.append((row, col))

while q:
    row = q[0][0]
    col = q[0][1]
    q.popleft()

    for i in range(8):
        nextr = row + drow[i]
        nextc = col + dcol[i]

        if maze[nextr][nextc] < 0:
            continue  # -1은 벽

        elif maze[nextr][nextc] == 0:
            maze[nextr][nextc] = maze[row][col] + dist[i]
            # 여기까지 오기 위한 거리 + 다음 위치로 가는 데 필요한 거리

            q.append((nextr, nextc))
        # 거리를 계산한 다음에는 로봇(maze[row][col])을 움직여야 함

        else:
            maze[nextr][nextc] = min(maze[nextr][nextc], maze[row][col] + dist[i])
        # 갔던 곳이라서 거리가 기록되어 있는 경우 거리가 더 짧은 쪽을 저장

    # display()

print('min distance :', round(maze[8][18], 5))

display()