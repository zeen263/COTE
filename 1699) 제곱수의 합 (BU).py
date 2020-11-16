import sys, math

'''
D[n] = 제곱수를 최소로 모아 n을 만드는 경우의 수
D[n-k] = 제곱수를 최소로 모아 n-k를 만드는 경우의 수

D[n] = min(D[n-k]) + 1  * 이 때 k는 1부터 sqrt(n)의 제곱들까지 선택가능
(k는 제곱수)
'''

N = int(sys.stdin.readline())
D = [99 for _ in range(N+1)]

D[1] = 1

for i in range(1, N+1):
    for j in range(1, int(math.sqrt(N))):
        pass
        # 1번째 칸에 올 수 있는 수는 1^2부터 sqrt(n)^2까지?
        # 맞나?


