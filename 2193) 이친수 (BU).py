import sys

N = int(sys.stdin.readline())

memo = [0]*91
memo[1] = 1
memo[2] = 1

for i in range(3, N+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[N])