import sys
from collections import defaultdict

'''
n마리라고 대답한 토끼는 n+1마리가 발견될 때 까지 같은 색으로 묶는다
3마리라고 대답한 토끼가 10마리 있다면 3그룹이 나오는데,
앞의 10//(3+1)그룹은 풀방(3+1마리)이며 뒤의 1그룹은 2마리이다.
그룹 수*그룹당 토끼 수 해주면 되는데
이 때 풀방 그룹을 이루지 않은 나머지토끼가 몇 마리든 상관없이 토끼수를 곱해줘야 함 
*입력 : 각 토끼들이 자기랑 같은 색 토끼가 몇 마리 더 있는지 대답한 것 (리스트) 
'''
answers = map(int, sys.stdin.readline().split())

total = 0
rabbits = defaultdict(int)
for i in answers:
    rabbits[i] += 1

for key in rabbits:
    cnt = rabbits[key]
    group = key + 1
    remain = cnt % group

    total += cnt // group * group
    if remain: total += group
    # 위의 2줄 또는 total += cnt//group * group + (cnt%group+group-1)//(group)*group

print(total)