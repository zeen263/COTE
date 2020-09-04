import sys
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1 # 0(방문x), 1(이쪽), 2(저쪽)

    while q:
        front = q[0]
        q.popleft()

        for node in graph[front]:
            if visited[node] == 0: # 방문한적 없는 노드인데
                if visited[front] == 1: # 타고 왔던 노드가 1번(이쪽)이라면
                    visited[node] = 2   # 이 노드는 2번(저쪽)일 것
                    q.append(node)

                elif visited[front] == 2: # 타고 왔던 노드가 2번(저쪽)
                    visited[node] = 1
                    q.append(node)



def compocheck(): # 연결요소가 여러 개일 수도 있다..!
    for i in range(1,len(graph)):
        if visited[i] == 0:
            bfs(i)
    
    bipartcheck() # 모든 연결요소를 다 돌고 나서 이분그래프인지 체크
    

def bipartcheck():
    for i in range(1,V+1): # i번 노드
        for j in graph[i]: # i번과 연결된 j번 노드
            if visited[i] == visited[j]: # i-j 연결됐는데 둘다 같은쪽에 있는 경우
                print('NO')
                return

    print('YES') # 여기까지 안걸리고 왔으면 이분 그래프


T = int(sys.stdin.readline())

for case in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for x in range(V+1)]
    visited = [0 for x in range(V+1)]


    for i in range(E):
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for nodes in graph:
        nodes.sort()

    compocheck()

