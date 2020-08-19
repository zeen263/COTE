import sys

N = int(sys.stdin.readline())

basenega2 = ""
mod = 0

if N==0: basenega2 = "0"

while N:
    # N이 홀수인 경우 양수/음수 상관없이 N-1의 몫을 계산하고 나머지는 1로 둔다
    mod = N%2
    basenega2 += str(mod)

    if mod: N = (N-1) // -2
    else: N = N//-2


print(basenega2[::-1])