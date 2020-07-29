import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())

memo = [[0]*10 for i in range(N+1)]
memo[1] = [1,1,1,1,1,1,1,1,1,1]
# memo[n][i] : 길이 n이며 i로 끝나는 오르막 수의 개수

def f(n, i):  # 점화식, 탈출조건, 메모이제이션
    if n == 1:
        return 1

    if memo[n][i] != 0:
        return memo[n][i]

    else:
        for j in range(i+1):
            memo[n][i] += f(n-1,j)
        return memo[n][i]

ans = 0
for i in range(10):
    ans += f(N,i)

print(ans%10007)


