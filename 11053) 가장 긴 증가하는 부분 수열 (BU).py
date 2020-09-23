import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
D = [1 for _ in range(N)]
# seq[j] < seq[i]을 만족하는 경우에 한해 앞의 수열들 중 길이가 최대인 것에 seq[i] 붙이기

for i in range(N):
    seqlen = [0]
    for j in range(i):
        if seq[j] < seq[i]:
            seqlen.append(D[j])
    D[i] += max(seqlen)

print(max(D))


