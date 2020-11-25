# (x, y) 좌표들을 y 기준으로 정렬

import sys

N = int(sys.stdin.readline())
pos = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pos.append((y, x))

pos = sorted(pos)

for i in pos:
    print(i[1], i[0])  # 뒤집어 출력