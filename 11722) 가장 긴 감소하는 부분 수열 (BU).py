import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
D = [1 for _ in range(N)] #수열의 길이

for i in range(N):
    for j in range(i):
        if seq[i] < seq[j]: #감소하는 부분수열
            D[i] = max(D[i], D[j]+1)

print(max(D))

