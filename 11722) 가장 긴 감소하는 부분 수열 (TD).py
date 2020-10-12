import sys
sys.setrecursionlimit(10**8)

def f(n):
    if n == 0: return 1
    if D[n] != 1: return D[n]

    for i in range(n):
        if seq[n] < seq[i]: #감소하는 부분 수열
            D[n] = max(D[n], D[i]+1)
    return D[n]


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
D = [1 for _ in range(N)]

for i in range(1,N):
    f(i)

print(max(D))