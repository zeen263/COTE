import sys

def preOrder(i):
    if i == N: return
    print(chr(i+65), end="")  # 방문
    if tree[i][0] != -19:
        preOrder(tree[i][0])  # 왼쪽 자식
    if tree[i][1] != -19:
        preOrder(tree[i][1])  # 오른쪽 자식

def inOrder(i):
    if i == N: return
    if tree[i][0] != -19:
        inOrder(tree[i][0])  # 왼쪽 자식
    print(chr(i + 65), end="")  # 방문
    if tree[i][1] != -19:
        inOrder(tree[i][1])  # 오른쪽 자식

def postOrder(i):
    if i == N: return
    if tree[i][0] != -19:
        postOrder(tree[i][0])  # 왼쪽 자식
    if tree[i][1] != -19:
        postOrder(tree[i][1])  # 오른쪽 자식
    print(chr(i + 65), end="")  # 방문


N = int(sys.stdin.readline())
tree = [["",""] for _ in range(N)]
order = ""

for i in range(N):
    idx, tree[idx][0], tree[idx][1] = map(lambda x:ord(x)-65, sys.stdin.readline().split())


preOrder(0); print()
inOrder(0); print()
postOrder(0)
'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
ABDCEFG
DBAECFG
DBEGFCA
'''
