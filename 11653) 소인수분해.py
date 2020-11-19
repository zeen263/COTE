import sys

N = int(sys.stdin.readline())
ROOT = int(N ** 0.5)
i=2

while N:
    if i>ROOT: break  # 더 이상 못 나누면 탈출

    if N%i == 0:
        print(i)
        N = N//i
    else:
        i+=1

if N > 1: print(N)  # 안 남고 잘 나눠떨어지면 몫이 1이 남아서...