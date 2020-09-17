import sys
sys.setrecursionlimit(10**8)

def f(n,i):
    global choose

    if n <= 2: return choose[n][i]
    if choose[n][i] != 0: return choose[n][i]  #메모되어 있을 경우


    if i == 2:  #N번 잔을 2연속으로 선택 : N-1번 잔을 1연속으로 선택
        choose[n-1][1] = f(n-1, 1)
        choose[n][2] = choose[n-1][1] + wine[n]
        return choose[n][2]

    if i == 1:  #N번 잔을 1연속으로 선택 : N-1번 잔을 0연속으로 선택
        choose[n-1][0] = f(n-1, 0)
        choose[n][1] = choose[n-1][0] + wine[n]
        return choose[n][1]

    if i == 0:  # N번 잔을 0연속으로 선택 : N-1번 잔을 0연속/1연속/2연속으로 선택
        for j in range(3):
            choose[n-1][j] = f(n-1, j)
        choose[n][0] = max(choose[n-1])
        return choose[n][0]



N = int(sys.stdin.readline())
wine = [0 for _ in range(N+1)]  # 1부터 시작
choose = [[0] * 3 for _ in range(N+1)]  # choose[i][j] : i번째 포도주잔을 j연속으로 선택

for i in range(1, N+1):
    wine[i] = int(sys.stdin.readline())

choose[1] = [0, wine[1], 0]
if N>1: choose[2] = [wine[1], wine[2], wine[1]+wine[2]]

for i in range(3):
    f(N,i)

print(max(choose[N]))