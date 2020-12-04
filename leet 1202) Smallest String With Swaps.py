from collections import deque


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        얘는... 그래프 문제이며 같은 연결요소 내에서는 타고 타고 가서 어떻게든 자리를 바꿀 수 있으므로
        연결요소를 찾아서 걔네를 정렬한 다음 순서에 맞게 배치하는 거라고 함...
        """
        N = len(s)
        graph = [[] for _ in range(N)]
        compo_alpha = [[] for _ in range(N)]
        compo_idx = [[] for _ in range(N)]
        res = list(s)
        visited = [False for _ in range(N)]
        q = deque()

        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        for i in range(N):
            q.append(i)

            while q:
                front = q[0]
                q.popleft()

                for node in graph[front]:
                    if not visited[node]:
                        visited[node] = True
                        q.append(node)
                        compo_alpha[i].append(s[node])
                        compo_idx[i].append(node)

        # compo_alpha : 연결요소별로 알파벳이 들어있음 [['b','d'],['c','a']]
        # compo_idx :   걔네들의 인덱스가 들어있음     [[3,0]],   [2,1]]

        for i in range(len(compo_alpha)):
            if not compo_alpha[i]: continue
            compo_alpha[i].sort()
            compo_idx[i].sort()
            for j in range(len(compo_alpha[i])):
                idx = compo_idx[i][j]
                res[idx] = compo_alpha[i][j]

        return "".join(res)


sol = Solution()
res = sol.smallestStringWithSwaps("dcab",[[0,3],[1,2]])
print(res)


