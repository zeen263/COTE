import sys
sys.setrecursionlimit(10**8)

def dfs(n):
    next = graph[n]

    if dist[next] == 0:  # 다음 노드도 방문 안 한 노드인 경우
        dist[next] = dist[n]+1  # 0도 아니고 -1도 아니면 현재 탐색에서 방문함
        ret = dfs(next)

    elif dist[next] == -1: # 다음 노드가 예전의 탐색에서 방문한 노드인 경우
        ret = dist[n]

    else:  # 다음 노드가 이번 탐색에서 방문한 노드일 경우
        ret = dist[next]-1

    dist[n] = -1
    return ret


def dfsall():
    noTeam = 0
    for i in range(1, N+1):
        if dist[i] == 0:
            dist[i] = 1  # 탐색의 첫 번째 노드에 대한 방문체크 (잊지마)
            noTeam += dfs(i)
    return noTeam


T = int(sys.stdin.readline())
for case in range(T):
    N = int(sys.stdin.readline())
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    dist = [0 for x in range(N + 1)]

    print(dfsall())

