'''
버블소트 하면 앞에있던 큰 수는 1스텝만에 뒤로 쭉 가는데
뒤에있던 작은 수는 1스텝에 한칸씩 앞으로 온다
> 정렬한거랑 안정렬한거 비교해서 인덱스 차이가 가장 큰 게 스텝 수
# 뒤에있던게 얼마나 앞으로 오냐를 보고 싶은 거니까
# 동일 값에 대해서 (정렬 전 인덱스 - 정렬 후 인덱스)를 체크
'''
import sys

N = int(sys.stdin.readline())
nums= [(0,0)] * (N + 1)


for i in range(1, N + 1):
    nums[i] = (int(sys.stdin.readline()),i) # 뒤에서 .index() 안 쓰려면 여기서 인덱스 달고 가야 함

nums.sort()
steps = 0

for i in range(1, N + 1):
    idxDiff = nums[i][1] - i  # nums는 정렬됐지만 앞에서 달아뒀던 정렬 전의 인덱스가 남아있음
    if steps < idxDiff:
        steps = idxDiff

print(steps+1)
# 문제에 주어진 코드에서는 i가 1부터 시작함
