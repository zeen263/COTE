import sys

M,N = map(int,sys.stdin.readline().split())
isprime = [1 for x in range(N+1)]
isprime[1] = 0

for i in range(2, int(N**0.5)+1):
    if isprime[i] == 0: continue

    for j in range(i*i, N+1, i):
        isprime[j] = 0

for i in range(M, len(isprime)):
    if isprime[i]: print(i)
