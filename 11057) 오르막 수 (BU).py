import sys

N = int(sys.stdin.readline())

memo = [[0]*10 for i in range(N+1)]
memo[1] = [1,1,1,1,1,1,1,1,1,1]
# memo[n][i] : 길이 n이며 i로 끝나는 오르막 수의 개수

for n in range(2,N+1): # 자릿수
    for i in range(10): # i로 끝나는 수
        for j in range(i+1): # memo[n][i]는 memo[n-1][0]부터 memo[n-1][i-1]까지의 합
            memo[n][i] += memo[n-1][j]

ans = 0
for n in memo[N]:
    ans += n
print(ans%10007)