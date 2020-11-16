import sys
from math import sqrt

'''        
1) 루프 수 구하기
65개, 사람 3명
마지막 사람까지 사탕 꽉 채워서 주는 게 하나의 루프라고 하고 루프 수를 구한다
 1  2  3 > (1+2+3) + (사람수^2)*0 = 6
 4  5  6 > (1+2+3) + (사람수^2)*1 = 15  1+3 + 2+3 + 3+ 3
 7  8  9 > (1+2+3) + (사람수^2)*2 = 24
다 더하면 45개로, 3번 돌릴 수 있고 11개가 남음.

* 더 적은 반복횟수 *
나눠주는 사탕이 1개씩 늘어나니까 candies는 sum(1~n)보다 크거나 같을 것. 이 n을 알면 반복 안 돌아도 됨
1부터 n까지 더한 값을 k라고 하면 k = n*(n+1)/2 이므로 floor(sqrt(2k))은 n이거나 n+1이다.
이것과 candies 값을 비교해서 n을 구할 수 있음


2) 남은 사탕을 분배        
각 사람이 가진 사탕은 (루프)*(줄서있는순서) + (사람수)*sum(루프-1) = [12 15 18]
위의 예에서 루프는 3이므로 3루프를 돌고 나서 4번째 라운드에 남은 사탕 25개를 털기 위해 1번째 사람에게 줘야 할 사탕은
(루프)*(사람수)+(1번째) = 10

그것도 주고 나면 남은 사탕은 5개로, 2번째 사람이 받아야 할 11개보다 모자라지만 어쨌든 2번째 사람이 전부 가져감
'''
candies, num_people = map(int,sys.stdin.readline().split())

n = int(sqrt(candies * 2))
if n * (n + 1) / 2 > candies: n = n - 1
# k = n*(n+1)/2 이므로 floor(sqrt(2k))은 n이거나 n+1이다
# 사탕 50개였으면 n은 10인데 sum(1~10)은 55라서 n을 9로 잡아야 함
# n : 몇 명이 자기 몫을 받아가는가 (루프와는 다름)

loop = n // num_people  # 사탕 돌리는 횟수
remainCandy = candies - (loop * num_people) * (loop * num_people + 1) / 2

# 사탕을 돌릴 수 있는 만큼 돌렸을 때 각각 몇 개씩 들고 있는가?
if loop > 0:
    res = [loop * (i + 1) + num_people * (loop - 1) * (loop) / 2 for i in range(num_people)]
else:
    res = [0 for _ in range(num_people)]

# 남은 사탕 털기
finalDistribute = num_people * loop + 1
i = 0
while remainCandy:
    if remainCandy < finalDistribute:
        res[i] += remainCandy
        break

    remainCandy -= finalDistribute
    res[i] += finalDistribute
    i += 1
    finalDistribute += 1

print(map(int, res))

