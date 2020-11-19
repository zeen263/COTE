import sys

def fact(n):
    if n == 1 or n == 0: return 1
    if memo[n] == 1:
        memo[n] = n*fact(n-1)
    return memo[n]

N = int(sys.stdin.readline())
memo = [1 for _ in range(N+1)]

print(fact(N))