"""
1부터 N까지 중복 없이 M개를 고른 수열 출력 (사전순)
* 모듈 안 쓰고 풀기
"""
import sys

def track():
    global pool

    if len(pool) == M:
        print(' '.join(map(str, pool)))
        return


    for i in range(1, N+1):
        if visited[i]:
            continue

        # 고르면서 방문체크
        pool.append(i)
        visited[i] = True

        track()  # 값 출력하고 나면 여기로 돌아온다

        # 다른 것도 골라야 하니까 방금 고른 칸 비우기
        pool.pop()
        visited[i] = False


N, M = map(int, sys.stdin.readline().split())
visited = [False for _ in range(N+1)]
pool = []

track()

