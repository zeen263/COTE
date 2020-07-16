import sys
import collections


# 큐에 0~9를 넣어놓고 시작
# 0을 만나면 0을 빼고(리스트에는 넣음) 0으로 시작하는 2자리 감소하는 수들을 만든다 (안되지만)
# 1을 만나면 1을 빼고(리스트에는 넣음) 1로 시작하는 2자리 감소하는 수들을 만든다
# 이걸 9까지 반복하면 큐에는 2자리 감소하는 수들이 들어있다
# 앞의 과정을 반복하면 3자리 감소하는 수들이 들어있겠지
# 큐가 빌 때까지 전부 돌고 나면 리스트에는 놀랍게도 감소하는 수들이 크기순으로 들어있게 된다

q = collections.deque()
descend = []

for i in range(10):
    q.append(i)


while q:
    curr = q.popleft()
    descend.append(curr)

    for i in range(curr % 10):
        q.append(curr*10 + i)


n = int(sys.stdin.readline())

if n >= len(descend):
    print(-1)
else:
    print(descend[n])
