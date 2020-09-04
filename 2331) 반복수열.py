import sys

def decompose(n,power):
    res = 0
    N = str(n)
    for ch in N:
        res += int(ch)**power
    return res

num, power = map(int, sys.stdin.readline().split())
visited = [0 for x in range(300000)]
order = 1

while True:
    if visited[num] != 0:
        break
    else:
        visited[num] = order
        order += 1
        num = decompose(num, power)


print(visited[num]-1)