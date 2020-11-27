import sys

N = int(sys.stdin.readline())
numList = [0]*10001

for i in range(N):
    num = int(sys.stdin.readline())
    numList[num] += 1

for i in range(10001):
    if numList[i] > 0:
        print((str(i)+'\n')*numList[i], end = '')