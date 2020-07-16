import sys

N = int(sys.stdin.readline())

# 맨 끝에 2x1 두개를 놓거나 1x2 한개를 놓을 수 있다
# 따라서 2xn 사각형을 채우는 방법은 맨 끝에 놓은 블럭을 제외한 부분인
# 2x(n-1) 사각형 채우는 방법 + 2x(n-2) 사각형 채우는 방법

# f(0)=0, f(1)=1, f(2)=2 (3부터는 순서대로)
# 근데 f(0)을 1로 두면 더 간단하게 짤 수 있다

memo = [0, 1, 2]+[0]*(N+1-3)

for n in range(3, N+1):
    memo[n] = memo[n-1] + memo[n-2]

print(memo[N]%10007)