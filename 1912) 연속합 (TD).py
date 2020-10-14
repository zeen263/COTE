import sys
sys.setrecursionlimit(10**8)

def f(n):
    if n==0: return seq[0]
    if visited[n]: return sums[n]

    sums[n] = max(seq[n],sums[n]+f(n-1))
    visited[n] = True
    return sums[n]

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
sums = [x for x in seq]
visited = [False for _ in range(N)]

f(N-1)
print(max(sums))
