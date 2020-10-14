import sys

'''
앞에서부터 i까지 쭉 더해 온 값보다 i번째 값이 더 크면 앞에꺼 버리고 i부터 새로 시작하는 게 낫다 
1) 일단 앞에꺼랑 나랑 더한다 (sums에 넣어)
2) 1의 결과물이 나 자신보다 작아?
3) 그럼 sums에 넣었던 걸 자기 자신으로 대체
'''

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
sums = [x for x in seq]

for i in range(1,N):
    sums[i] += sums[i-1]
    if seq[i] > sums[i]:
        sums[i] = seq[i]

print(max(sums))