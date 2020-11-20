'''
끝자리 0의 개수를 세려면 곱해서 10이 되는 (2x5)의 개수를 확인하면 됨
팩토리얼 계산하지 말고 i에 2와 5가 몇 개나 들어있는지 체크
'''

import sys

def decomp25(n):
    global cnt2, cnt5
    while n:
        if not n%2:
            cnt2 += 1
            n = n//2
            continue
        if not n%5:
            cnt5 += 1
            n = n//5
            continue
        break


N = int(sys.stdin.readline())
res = cnt2 = cnt5 = 0

if N >= 5:
    for i in range(2,N+1):
        decomp25(i)

    if cnt2 > cnt5: res = cnt5
    else: res = cnt2

print(res)
