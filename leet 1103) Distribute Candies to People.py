import sys

'''        
65개, 사람 3명
마지막 사람까지 사탕 꽉 채워서 주는 게 하나의 루프라고 하고 루프 수를 구한다
 1  2  3 > (1+2+3) + (사람수^2)*0 = 6
 4  5  6 > (1+2+3) + (사람수^2)*1 = 15
 7  8  9 > (1+2+3) + (사람수^2)*2 = 24
다 더하면 45개로, 3번 돌릴 수 있고 11개가 남음. 그 다음 나머지 사탕을 분배

각 사람이 가진 사탕은 (루프)*(줄서있는순서) + (사람수)*sum(루프-1) = [12 15 18]
위의 예에서 루프는 3이므로 남은 사탕 25개를 털기 위해 1번째 사람에게 줘야 할 캔디는 (루프)*(사람수)+1 = 10
그것도 주고 나면 남은 사탕은 5개로, 2번째 사람이 받아야 할 11개보다 모자라지만 어쨌든 2번째 사람이 전부 가져감   
'''
candies, num_people = map(int,sys.stdin.readline().split())

loop = 0
remainCandy = candies
candyPack = num_people * (num_people + 1) / 2  # 사람들이 맨 처음 받는 사탕 수의 총합

while True:  # 사탕 몇 바퀴 돌릴 수 있는지
    candies -= candyPack + loop * (num_people ** 2)

    if candies >= 0:
        loop += 1
        remainCandy = candies
    else:
        break

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
