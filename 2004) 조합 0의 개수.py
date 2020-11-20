'''
nPr = n! / (n-r)!
nCr = nPr / r!
'''
import sys

N, R = map(int, sys.stdin.readline().split())
res = cnt2 = cnt5 = 0


# nCr : (n! / r!) / (n-r)!
if N >= 5:

    i, j = 2, 5
    while i <= N:  # (n! / r!) 부분 : R~N 범위에서 2와 5의 갯수 세어 더하기 (2^k, 5^k도 포함)
        cnt2 += (N//i - R//i)
        cnt5 += (N//j - R//j)
        i *= 2
        j *= 5

    i, j = 2, 5
    while i <= (N-R):  # 1 / (n-r)! 부분 : 1~(N-R) 범위에서 2와 5의 갯수 세어 빼기 (2^k, 5^k도 포함)
        cnt2 -= (N - R) // i
        cnt5 -= (N - R) // j
        i *= 2
        j *= 5

    if cnt2 > cnt5: res = cnt5
    else: res = cnt2

print(res)
