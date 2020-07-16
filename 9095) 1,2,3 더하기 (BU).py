import sys

# f(n)을 구할 때
# 1) 맨 뒷자리에 1을 고정시켰다면 f(n-1)을 계산해야 한다
# 2) 맨 뒷자리에 2를 고정시켰다면 f(n-2)을 계산해야 한다
# 3) 맨 뒷자리에 3을 고정시켰다면 f(n-3)을 계산해야 한다
# 얘네를 다 더하면 f(n)

T = int(sys.stdin.readline())

for i in range(T):

    N = int(sys.stdin.readline())

    memo = [0,1,2,4]+[0]*(N+1-4)

    for n in range(4,N+1):
        picked1 = memo[n-1]
        picked2 = memo[n-2]
        picked3 = memo[n-3]

        memo[n] = picked1 + picked2 + picked3

    print(memo[N])

