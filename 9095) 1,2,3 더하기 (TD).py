import sys

# f(n)을 구할 때
# 1) 맨 뒷자리에 1을 고정시켰다면 f(n-1)을 계산해야 한다
# 2) 맨 뒷자리에 2를 고정시켰다면 f(n-2)을 계산해야 한다
# 3) 맨 뒷자리에 3을 고정시켰다면 f(n-3)을 계산해야 한다
# 얘네를 다 더하면 f(n)


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 4

    if memo[n] == 0:
        res = f(n-1) + f(n-2) + f(n-3)
        return res

    else:
        return memo[n]


T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    memo = [0,1,2,4]+[0]*(N+1-4)

    print(f(N))



