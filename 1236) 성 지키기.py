import sys
from collections import defaultdict

# 가로로 빈 줄 찾기
# 가로로 빈 줄 수만큼 경비원 추가

# 세로로 빈 줄 찾기
# max(0, 세로로 빈 줄 - 가로로 빈 줄)만큼 경비원 추가


N, M = map(int, sys.stdin.readline().split())

castle = []
for i in range(N):
    line = sys.stdin.readline().strip()
    line = line.replace("X", "1")
    line = line.replace(".", "0")
    
    line = list(map(int, list(line)))
    
    castle.append(line)



rows = defaultdict(int)
cols = defaultdict(int)

for i in range(N):
    for j in range(M):
        tile = castle[i][j]
        
        rows[i] += tile
        cols[j] += tile

row = 0
for k, v in rows.items():
    if v == 0:
        row += 1
        
col = 0        
for k, v in cols.items():
    if v == 0:
        col += 1


  
result = row + max(0, col-row)

print(result)
