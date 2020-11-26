'''
matrix = 
  [[ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]]
   
   k = 5인 경우 5번째로 작은 수인 11 반환
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        numlist = sum(matrix, [])
        numlist.sort()
        
        return numlist[k-1]
