class Solution:
    def firstBadVersion(self, n):
            
        left = 0
        right = n
        
        
        while left < right:
            mid = (left+right)//2
            
            isBad = isBadVersion(mid)
            
            if isBad:
                right = mid
            else:
                left = mid+1
        
        return right
                
