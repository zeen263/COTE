"""
반복문 안 쓰는 백트래킹 (얘를 고르거나 고르지 않거나)
"""

import sys

def backtrack(last_pick_idx:int) -> None:
    global selected

    if len(selected) == 6:  # 6개 채운 경우
        print(' '.join(map(str, selected)))
        return

    if last_pick_idx == LEN:  # 6개를 채우지 못했는데 pool에 있는거 다 본 경우
        return

    selected.append(pool[last_pick_idx])  # 현재 인덱스를 고르고 넘어가기
    backtrack(last_pick_idx+1)
    selected.pop()
    
    backtrack(last_pick_idx+1)  # 현재 인덱스 안 고르고 넘어가기
    
    

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

