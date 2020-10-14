import sys
sys.setrecursionlimit(10**8)

def f(n,k):
    global score
    if score[n][k] != -1: return score[n][k]

    if k==0:
        score[n][0] = max(f(n-1,1), f(n-1,2))
    else:
        score[n][k] = f(n-1,k-1) + stair[n]

    return score[n][k]


N = int(sys.stdin.readline())
stair = [0]+[int(sys.stdin.readline()) for _ in range(N)]
score = [[-1]*3 for _ in range(N+1)]
score[1] = [0, stair[1], 0]
if N>1: score[2] = [stair[1], stair[2], stair[1]+stair[2]]

for i in range(3):
    f(N,i)

print(max(score[N][1],score[N][2]))