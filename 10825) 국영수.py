# 정렬 순서 : 국어감소 > 영어증가 > 수학감소 > 이름사전순

import sys

N = int(sys.stdin.readline())
data = []

for i in range(N):
    name, kor, eng, math = sys.stdin.readline().split()
    data.append((-int(kor), int(eng), -int(math), name))  # -를 붙이면 절대값이 작은 수일수록 크지

data.sort()
for student in data:
    print(student[3])