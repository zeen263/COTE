import heapq


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = []
        dist = [[x, y] for x in range(rows) for y in range(cols)]
        heap = []

        for i, j in dist:
            d = abs(rCenter - i) + abs(cCenter - j)
            heapq.heappush(heap, (d, [i, j]))

        while heap:
            d, idx = heapq.heappop(heap)
            res.append(idx)

        return res



"""
# 더 빠르고 간단한 방법...
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dist = [[x,y] for x in range(rows) for y in range(cols)]
        res = sorted(dist, key=lambda x:abs(rCenter-x[0])+abs(cCenter-x[1]))

        return res
"""