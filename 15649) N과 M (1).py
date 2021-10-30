"""
백트래킹의 정석
"""
import sys

def track():
    global visited, selected

    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return


    for i in range(1, N+1):
        if visited[i]:
            continue

        # 고르면서 방문체크
        selected.append(i)
        visited[i] = True

        track()  # 값 출력하고 나면 여기로 돌아온다

        # 다른 것도 골라야 하니까 방금 고른 칸 비우기
        selected.pop()
        visited[i] = False


N, M = map(int, sys.stdin.readline().split())
visited = [False for _ in range(N+1)]
selected = []

track()

