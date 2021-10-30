"""
백트래킹
1 2 3과 3 2 1은 같다 > 작은 것부터 고르기
"""

import sys

def backtrack(last_pick_idx:int) -> None:
    global visited, selected

    if len(selected) == 6:
        print(' '.join(map(str, selected)))
        return

    for i in range(last_pick_idx, LEN):  # last_pick보다 큰 인덱스부터 시작하면 중복을 피할 수 있음
        if visited[i]:
            continue

        selected.append(pool[i])
        visited[i] = True

        backtrack(i)  # idx

        selected.pop()
        visited[i] = False



N = 6  # 로또라서
while True:
    s = sys.stdin.readline()
    if s[0]=="0": break

    pool = list(map(int, s.split()))
    pool.pop(0)
    LEN = len(pool)

    visited = [0 for _ in range(LEN)]
    selected = []

    backtrack(0)  # last_pick_idx = 0
    print()

