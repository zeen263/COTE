import sys

N = int(sys.stdin.readline())

P = map(int, sys.stdin.readline().split())
P = [0] + list(P)
# 인덱스 1부터 시작하려고

memo = [0]*1001
memo[1] = P[1]

for i in range(2, N+1): # 카드 i장 팩을 고른 경우 전체 구매금액의 비교

    memo[i] = P[i]
    for j in range(1, i): # f(i), 즉 카드 i장 팩의 구매금액의 비교
        memo[i] = max(memo[i], memo[j] + memo[i-j]) # 2장을 살 때는 f(1)+f(2-1), P2 중 최대값을 선택
                                                    # 3장을 살 때는 f(1)+f(3-1), f(2)+f(3-2), P3 중 최대값을 선택

print(memo[N])

