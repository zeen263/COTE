'''
3kg 봉투와 5kg 봉투
Nkg에서 3을 뺀 경우와 5를 뺀 경우로 나눠서 계산
d[n] = d[n-3]과 d[n-5] 중 작은 값 + 1
'''

import sys

LARGE = 9999
N = int(sys.stdin.readline())
d = [LARGE for _ in range(N+3)] # 3kg짜리 주문들어오면 d[5]가 없어서 인덱스에러남... 그거 방지용
d[3], d[5] = 1, 1

for i in range(6, N+1):
    d[i] = min(d[i-3], d[i-5]) + 1
    # 5kg 봉투를 고르면 d[1]과 d[3]을 비교하게 될텐데 d[1]을 0이나 -1로 초기화하면 걔네가 선택되기 때문에 초기화를 엄청 큰 값으로


if d[N] >= LARGE:
    print(-1)
else:
    print(d[N])