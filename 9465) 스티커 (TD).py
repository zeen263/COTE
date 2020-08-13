import sys

sys.setrecursionlimit(10**8)


def f(i, j):

    if j == 0: return 0
    if j == 1: return arr[i][1]

    if memo[i][j] != -1:
        return memo[i][j]

    else:
        memo[i][j] = max( f(3-i, j-1), f(3-i, j-2) ) + arr[i][j]
        return memo[i][j]



T = int(sys.stdin.readline())

memo = [[-1] * (100001) for n in range(3)]  # 1부터 시작하려고
arr = [[0] * (100001) for n in range(3)]

for t in range(T):
    N = int(sys.stdin.readline())

    for i in range(1,3): # 초기화
        lst = [0] + list(map(int, sys.stdin.readline().split()))

        for j in range(N+1):
            memo[i][j] = -1
            arr[i][j] = lst[j]


    res = max(f(1,N), f(2,N), f(1, N-1), f(2, N-1))
    print(res)