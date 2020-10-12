import sys
sys.setrecursionlimit(10**8)

def f(n):
    global D
    if n==1: return 1
    if D[n] != 0: return D[n]

    seqlen = [1]
    for i in range(1,n):
        if seq[n] > seq[i]:
            seqlen.append(f(i)+1)

    D[n] = max(seqlen)
    return D[n]


N = int(sys.stdin.readline())
seq = [0]+list(map(int, sys.stdin.readline().split()))
D = [0 for _ in range(N+1)]
D[1] = 1
# seq[j] < seq[i]을 만족하는 경우에 한해 앞의 수열들 중 길이가 최대인 것에 seq[i] 붙이기

for i in range(1,N+1):
    f(i)
print(max(D))