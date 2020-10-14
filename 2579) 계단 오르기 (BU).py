import sys

'''
각 계단은 안 밟거나 1연속으로 밟거나 2연속으로 밟을 수 있음

i번째를 안 밟았으면 앞에꺼는 어쨌든 밟았음 > 점수는 score[i-1][1],score[i-1][2] 중 max값
i번째를 1연속 밟았으면 앞에껀 안 밟음 > 점수는 score[i-1][0] + stair[i]
i번째를 2연속 밟았으면 앞에꺼를 1연속으로 밟음 > 점수는 score[i-1][1] + stair[i]

마지막 계단은 반드시 밟을 것 > score[-1][1] score[-1][2] 중 큰 값이 정답
score[-1][0]은 마지막꺼를 안 밟았다는 뜻이니까
'''

N = int(sys.stdin.readline())
stair = [0]+[int(sys.stdin.readline()) for _ in range(N)]
score = [[-1]*3 for _ in range(N+1)]
score[1] = [0, stair[1], -1]

for i in range(2,N+1):
    score[i][0] = max(score[i-1][1], score[i-1][2])
    score[i][1] = score[i-1][0] + stair[i]
    score[i][2] = score[i-1][1] + stair[i]

print(max(score[N][1], score[N][2]))