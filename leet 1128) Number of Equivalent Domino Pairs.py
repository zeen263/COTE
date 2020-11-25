from collections import defaultdict
import sys

class Solution:
    def numEquivDominoPairs(self, dominoes: list) -> int:
        # 도미노(i,j)가 있으면 card[i][j]와 card[j][i]에 1씩 더하기
        # 모든 도미노를 다 처리하고 나서 쭉 살펴봤을 때 2 이상인 것에 대해 nC2 조합을 구해야 함

        card = defaultdict(int)
        cnt = 0

        for block in dominoes:
            i, j = block[0], block[1]
            pair = (i, j) if i <= j else (j, i)
            card[pair] += 1

        for key in card:
            if card[key] > 1:
                n = card[key]
                cnt += n * (n - 1) // 2

        return cnt

sol = Solution()
n = eval(sys.stdin.readline())
#[[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]

print(sol.numEquivDominoPairs(n))