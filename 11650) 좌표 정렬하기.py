import sys
from collections import defaultdict

N = int(sys.stdin.readline())
pos = []

for i in range(N):
    pos.append(tuple(map(int, sys.stdin.readline().split())))

pos = sorted(pos)
for i in pos:
    print(i[0], i[1])


'''
# 웃기게도 이게 시간과 메모리를 더 많이 먹는다
pos = defaultdict(list)

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    pos[x].append(y)

for key in sorted(pos):
    pos[key].sort()
    for val in pos[key]:
        print(key, val)
'''