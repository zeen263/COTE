import sys
sys.setrecursionlimit(10**8)

def increase(n, seq, lst):
    if n == 0: return 1
    if lst[n] > 1: return lst[n]

    for i in range(n):
        if seq[n] > seq[i]:
            lst[n] = max(lst[n], lst[i]+1)
    return lst[n]


N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
rseq = seq[::-1]
inc = [1 for _ in range(N)]
dec = [1 for _ in range(N)]

for i in range(N):
    inc[i] = increase(i,seq,inc)
    dec[i] = increase(i,rseq,dec)
dec.reverse()

print(max([x+y-1 for x,y in zip(inc,dec)]))
