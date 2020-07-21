import sys

N = int(sys.stdin.readline())

memo = [0]*91
memo[1] = 1
memo[2] = 1

def f(n):
    if n == 1: return 1
    if n == 2: return 1

    if memo[n]: return memo[n]

    else:
        memo[n] = f(n-1) + f(n-2)
        return memo[n]


res = f(N)
print(res)