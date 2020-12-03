import sys
from collections import deque

# preorder : 방문 > 왼쪽자식 프리오더 > 오른쪽자식 프리오더
def preOrder():
    q = deque()
    q.append(0)
    order = ""
    while q:
        idx = q[0]
        order += node[idx]  # 방문

        if tree[idx][0] != '.':  # 오른쪽 자식








def inOrder():
    pass

def postOrder():
    pass


N = int(sys.stdin.readline())
tree = [["",""] for _ in range(N)]
node = ["" for _ in range(N)]

for i in range(N):
    node[i], tree[i][0], tree[i][1] = sys.stdin.readline().split()

print(preOrder())
print(inOrder())
print(postOrder())