import random


# 20x10 맵의 1,1에서 18,8까지 이동
# 1은 벽이고 0은 길, 2는 이동한 자취
# 선택지가 여러 개 생기면 랜덤하게 이동하도록 함
# 직선으로 이동하면 거리가 1, 대각선으로 이동하면 거리가 1.414
# 최단거리 구하기


def resetList():
    global visited
    for i in range(10):
        for j in range(20):
            visited[i][j] = False


maze = \
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
     [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
     [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1],
     [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
     [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
     [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
     [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

visited = [[False] * 20 for _ in range(10)]

dr = (1, 1, 0, -1, -1, -1, 0, 1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)
dist = (1, 1.414, 1, 1.414, 1, 1.414, 1, 1.414)

minDist = 9999
tries = 0
nextR = nextC = 0

for cnt in range(100000000):
    if cnt % 10000000 == 0: print("i'm alive... " + str(cnt // 10000000) + "0,000,000th tries\n")

    resetList()
    distSum = 0
    r = c = 1
    visited[r][c] = True

    while True:
        moveableCnt = 0
        moveableDir = [0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(8):  # 주변 8칸 중 방문 가능한 곳을 체크
            nextR = r + dr[i]
            nextC = c + dc[i]

            if maze[nextR][nextC] == 0 and visited[nextR][nextC] == 0:
                moveableDir[moveableCnt] = i
                moveableCnt += 1

        if moveableCnt == 0: break

        rand = random.randint(0, moveableCnt - 1)
        idx = moveableDir[rand]
        nextR = r + dr[idx]
        nextC = c + dc[idx]

        visited[nextR][nextC] = True
        distSum += dist[idx]

        r = nextR
        c = nextC

        if minDist <= distSum: break

        if r == 8 and c == 18:
            minDist = distSum
            tries = cnt

            for i in range(10):
                for j in range(20):
                    if visited[i][j]:
                        print("2 ", end=' ')
                    else:
                        print(str(maze[i][j]) + ' ', end=' ')
                print()

            print("try " + str(cnt))
            print("distance : " + str(distSum))
            print("\n")
            break

print("===============================================")
print("min distance : " + str(minDist))
print("try : " + str(tries))
print("===============================================")
