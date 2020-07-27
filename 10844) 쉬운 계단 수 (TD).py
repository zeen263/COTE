import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())

memo = [[0]*10 for i in range(101)]
memo[1] = [0,1,1,1,1,1,1,1,1,1]

# n길이의 i로 끝나는 계단수의 개수
def f(n,i):
    if n == 1: # 탈출조건
        if i == 0: return 0
        else:      return 1

    elif memo[n][i] != 0: # 메모이제이션
        return memo[n][i]
    elif i == 0:
        return f(n-1, i+1)
    elif i == 9:
        return f(n-1, i-1)
    else:
        memo[n][i] = f(n-1,i-1) + f(n-1,i+1)
        return memo[n][i]


# 귝귝코드
# def f(n,i):
#     if n==1:
#         if i==0:
#             return 0
#         else:
#             return 1
#     ret = memo[n][i]
#
#     if ret>0:
#         return ret
#
#     if i!=0: ret += f(n - 1, i - 1)
#     if i!=9: ret += f(n - 1, i + 1)
#     return ret

# i가 변하게 해야 하니까 반복문돌려
ans = 0
for i in range(10):
    ans += f(N, i)
print(ans%1000000000)
