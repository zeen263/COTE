# why??

from collections import deque, defaultdict


class Solution:
    def cutOffTree(self, forest):
        # 아이디어 : (높이, row, col) 정보를 갖고 잇는데 이걸 높이순으로 정렬
        #            일단 정렬하고 나면 높이 순서대로 (row,col)에 방문하면서 거리체크(bfs)

        q = deque()

        dr = (1, 0, -1, 0)
        dc = (0, 1, 0, -1)

        n = len(forest)  # row
        m = len(forest[0])  # col

        trees = defaultdict(tuple)
        distMap = [[-1] * m for _ in range(n)]
        distMap[0][0] = 0
        dist = 0

        for i in range(n):
            for j in range(m):
                height = forest[i][j]
                if height > 1:
                    trees[height] = (i, j)

        cutOrder = sorted(trees.items()) # 베어야 할 나무의 좌표가 (height, (r, c)) 형태의 튜플로 들어있음
        choppedTrees = 0
        q.append((0, 0))
        print(cutOrder)
        for target in cutOrder:
            while q:
                row = q[0][0]
                col = q[0][1]
                q.popleft()

                if (row,col) == target[1]:
                    choppedTrees += 1
                    dist += distMap[row][col]
                    print('chop chop', choppedTrees, 'trees chopped, dist :', distMap[row][col])
                    distMap = [[-1] * m for _ in range(n)]
                    distMap[0][0] = 0
                    q.clear()
                    q.append((row,col))
                    print(row,col,target[1])
                    break

                for i in range(4):
                    nextr = row + dr[i]
                    nextc = col + dc[i]
                    if nextr >= 0 and nextr < n and nextc >= 0 and nextc < m:
                        if forest[nextr][nextc] != 0 and distMap[nextr][nextc] == -1:
                            distMap[nextr][nextc] = distMap[row][col] + 1
                            q.append((nextr, nextc))


        if choppedTrees == len(cutOrder):
            return dist
        else:
            return -1


sol = Solution()
inputData = [[545, 640, 243, 691],
             [863, 613, 687, 797],
             [  6, 921, 898, 947],
             [839, 227, 462, 475],
             [890, 189, 254, 608]]
inputData = [[1,2,3],
             [0,0,4],
             [7,6,5]]
print('distance :', sol.cutOffTree(inputData))
