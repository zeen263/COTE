import sys
sys.setrecursionlimit(10**8)

# k로 나눈 나머지 : (a+b) % k = ((a % k)+(b % k)) % k

N = int(sys.stdin.readline())

memo = [0]*(N+1)

def f(n):
    if n==0: return 1
    elif n==1: return 1

    if memo[n] == 0: # 비어있으면 채우기
        memo[n] = ( f(n-1) + 2*f(n-2) ) % 10007
        return memo[n]

    else: return memo[n]

res = f(N)
print(res)
