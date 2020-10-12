import sys
sys.setrecursionlimit(10**8)

def f(n):
    global D, visited
    if n == 0: return seq[0]
    if visited[n] == True: return D[n]

    for i in range(n):
        if seq[i] < seq[n]: #증가하는 부분수열
            D[n] = max(D[n], seq[n]+f(i))
    visited[n] = True
    return D[n]


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split())) # 입력받은 수열
D = [x for x in seq] # dp 배열
visited = [False for _ in range(N)]

for i in range(1,N):
    f(i)

print(max(D))