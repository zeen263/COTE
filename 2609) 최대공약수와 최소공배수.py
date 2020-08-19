import sys

a, b = map(int, sys.stdin.readline().split())

def calcGCD(n,m):
    if m==0: return n
    else:
        return calcGCD(m, n%m)


GCD = calcGCD(a,b)
LCM = int(a*b / GCD)

print(GCD)
print(LCM)

