# 파이썬에서 stable sorting 되는 함수가 뭐지?

import sys

N = int(sys.stdin.readline())
members = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    members.append((int(age), i, name))
members = sorted(members)

for i in members:
    print(i[0], i[2])