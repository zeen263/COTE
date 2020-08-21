import sys

def eratos(n):
    isprime = [True for x in range(n+1)]
    isprime[1] = False

    for i in range(2, int(n**0.5)+1):
        if not isprime[i]: continue

        for j in range(i*i, n+1, i):
            isprime[j] = False

    oddprime = [x for x in range(3, len(isprime), 2) if isprime[x]]
    return oddprime, isprime



oddprime, isprime = eratos(1000000)

while True:
    isGoldbachRight = False
    N = int(sys.stdin.readline())
    if N==0: break

    for prime in oddprime:
        if isprime[N-prime]:
            isGoldbachRight = True
            print("{} = {} + {}".format(N, prime, N-prime))
            break

    if not isGoldbachRight:
        print("Goldbach's conjecture is wrong.")