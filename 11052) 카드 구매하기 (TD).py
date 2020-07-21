import sys

N = int(sys.stdin.readline())

P = map(int, sys.stdin.readline().split())
P = [0] + list(P)

memo = [0]*1001
memo[1] = P[1]

def f(n):
    if memo[n]: return memo[n]

    else:
        memo[n] = P[n]
        for i in range(1, n):
            memo[n] = max(memo[n], f(i)+f(n-i))

        return memo[n]


res = f(N)
print(res)
