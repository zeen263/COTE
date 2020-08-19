import sys

T = int(sys.stdin.readline())

def calcGCD(n, m):
    if m==0: return n
    else: return calcGCD(m, n%m)



for case in range(T):
    N = list(map(int,sys.stdin.readline().split()))

    GCDsum = 0
    size = len(N)

    for i in range(1,size):
        for j in range(i+1, size):
            GCDsum += calcGCD(N[i], N[j])

    print(GCDsum)