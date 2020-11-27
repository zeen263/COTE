import sys

N = int(sys.stdin.readline())
cards = [0]*N

for i in range(N):
    cards[i] = int(sys.stdin.readline())

cards.sort()
num, cnt = cards[0], 1
maxcnt = 1
for i in range(N-1):
    if cards[i] == cards[i+1]:
        cnt += 1
        if cnt > maxcnt:
            maxcnt = cnt
            num = cards[i]
    else:
        cnt = 1
print(num)